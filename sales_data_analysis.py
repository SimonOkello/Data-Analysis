# %%
import matplotlib.pyplot as plt
import os
import pandas as pd

# %% [markdown]
# ### Read a single month sales data

# %%
df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')
df.head()

# %% [markdown]
# ### List all Sales data csv files

# %%
files = [file for file in os.listdir('./Sales_Data')]
for file in files:
    print(file)

# %% [markdown]
# ### Concatenate all csv files into one Sales data file

# %%
files = [file for file in os.listdir('./Sales_Data')]
all_data_csv = pd.DataFrame()
for file in files:
    df = pd.read_csv('./Sales_Data/'+file)
    all_data_csv = pd.concat([all_data_csv, df])

all_data_csv = all_data_csv.to_csv('all_data_csv.csv', index=False)

# %% [markdown]
# ### Read all data csv file to a data frame

# %%
all_sales_data = pd.read_csv('./Sales_Data/all_data_csv.csv')
all_sales_data.head()

# %% [markdown]
# ## Clean up the data!

# %% [markdown]
# ##### Get all NaN rows in the dataframe

# %%
nan_df = all_sales_data[all_sales_data.isna().any(axis=1)]
nan_df.head()

# %% [markdown]
# ##### Drop NaN rows from the dataframe

# %%
all_sales_data = all_sales_data.dropna(how='all')
all_sales_data.head()

# %% [markdown]
# #### Find 'Or' and exclude it from the dataframe

# %%
all_sales_data = all_sales_data[all_sales_data['Order Date'].str[0:2] != 'Or']
all_sales_data.head()

# %% [markdown]
# #### Convert columns to correct data types

# %%
all_sales_data['Quantity Ordered'] = pd.to_numeric(
    all_sales_data['Quantity Ordered'])
all_sales_data['Price Each'] = pd.to_numeric(all_sales_data['Price Each'])
all_sales_data.head()

# %% [markdown]
# ## Add columns to dataframe

# %% [markdown]
# ### Add month column to dataframe

# %%
all_sales_data['Month'] = all_sales_data['Order Date'].str[0:2]
all_sales_data['Month'] = all_sales_data['Month'].astype('int32')
all_sales_data.head()

# %% [markdown]
# ### Add sales column to dataframe

# %%
all_sales_data['Sales'] = all_sales_data['Quantity Ordered'] * \
    all_sales_data['Price Each']
all_sales_data.head()

# %% [markdown]
# ## Data Analysis

# %% [markdown]
# ### 1. What was the best month for sales?. How much was earned that month?

# %%
results = all_sales_data.groupby('Month').sum(numeric_only=True)
results

# %% [markdown]
# ### 2. plot the above data

# %%

months = range(1, 13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD($)')
plt.xlabel('Months')
plt.suptitle('Sales Per Month')
plt.show()
