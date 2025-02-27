# %% [markdown]
# ### Question 5:

# %% [markdown]
# 1. Calculate the standard correlation coefficient matrix of the housing data set.

# %%
#first I have to load in the housing data set
import os
import tarfile
import urllib
import pandas as pd

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path=os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path=os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)

# execute these functions:
fetch_housing_data() # fetch the data
housing = load_housing_data()
housing # loading data into workspace

# %%
#calculate the standard correlation coefficient matrix
housing.drop("ocean_proximity", axis=1, inplace=True) #we drop this as it only contains categories rather than floats so cannot be converted to a matrix
corr_matrix = housing.corr()
corr_matrix

# %% [markdown]
# For this question this is a standard procedure. I import necessary packages that help take the data from GitHub and convert from a .tgz file to a .cvs file in order to view the 'housing' data. I then print this. Following this, I drop the 'ocean_proximity' attribute as it only contains categories and cannot be calcualatd into a correlation matrix, which is purely numerical. Then I do housing.corr() to work out the correlation matrix.

# %% [markdown]
# 2. Assume your quantity of interest is the median_income. Provide the correlation coefficient with respect to this attribute and sort them in ascending
# order.

# %%
corr_matrix['median_income'].sort_values(ascending=True)

# %% [markdown]
# I simply call on one column of the correlation matrix to view just median income attributes.
