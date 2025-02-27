# %% [markdown]
# ### Question 6:

# %% [markdown]
# In the lecture notes, we defined the following attribute combinations.

# %%
#now I have to re-load in the housing data set as each question is a different python file
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
housing = load_housing_data() # loading data into workspace

# %%
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"] = housing["population"]/housing["households"]

# %% [markdown]
# 1. Plot the scatter matrix using the following attributes, also plot a scatter plot for just attributes median_house_value over rooms_per_household.

# %%
from pandas.plotting import scatter_matrix

attributes = ["rooms_per_household", "bedrooms_per_room", "population_per_household", "median_income", "median_house_value"]

scatter_matrix(housing[attributes], figsize=(12, 8)) # LEFT

housing.plot(kind="scatter", x="median_house_value", y="rooms_per_household", alpha=0.1) # RIGHT

# %% [markdown]
# For this question I simply use pandas.plotting to plot the scatter matrix for all requested attributes, then I also plot a scatter plot for two of the requested attributes.

# %% [markdown]
# 2. As comparison, print out the standard correlation coefficients relative to median_house_value (sort them as you like). Discuss: (i) is the
# negative correlation of bedrooms_per_room to median_house_value visible in the scatter matrix; and (ii) do we see a positive correlation of
# median_house_value and rooms_per_household? What problem could impact our capability to infer from the picture such correlation?
# 

# %%
#calculate the standard correlation coefficient matrix
housing.drop("ocean_proximity", axis=1, inplace=True) #we drop this as it only contains categories rather than floats so cannot be converted to a matrix
corr_matrix = housing.corr()
corr_matrix
corr_matrix["median_house_value"].sort_values(ascending=True)

# %% [markdown]
# (i) In terms of median house value, it is definitely the most negative sloped correlation (-0.26 approx). What's more, the results are quite spread out showing weak correlation between the two attributes. But yes it is indeed visible.
# 
# (ii) It is slightly positive at a value of 0.15 approx. Unfortunately, because the scale of the graph is set from the lowest to the highest value, we see a 'zoomed-out' picture which doesn't allow us to properly view the bulk of results. This means that we are unable to see a positive gradient and almost see the graph as a straight line. This affects our ability to be able to determine that there is in fact a positive correlation. Luckily, the corr_matrix function returns the true correlation values. 

# %% [markdown]
# ![image.png](attachment:image.png)

# %% [markdown]
# Reference image taken from https://texasgateway.org/resource/interpreting-scatterplots  specifically https://d1yqpar94jqbqm.cloudfront.net/styles/media_middle/s3/images/Capture_41.PNG?itok=s04c4ENp
