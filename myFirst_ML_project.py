{
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "<p style=\"text-align:center\">\n    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01\">\n    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\"  />\n    </a>\n</p>\n\n<h1 align=\"center\"><font size=\"5\">Final Project: Classification with Python</font></h1>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>Table of Contents</h2>\n<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n    <ul>\n    <li><a href=\"https://#Section_1\">Instructions</a></li>\n    <li><a href=\"https://#Section_2\">About the Data</a></li>\n    <li><a href=\"https://#Section_3\">Importing Data </a></li>\n    <li><a href=\"https://#Section_4\">Data Preprocessing</a> </li>\n    <li><a href=\"https://#Section_5\">One Hot Encoding </a></li>\n    <li><a href=\"https://#Section_6\">Train and Test Data Split </a></li>\n    <li><a href=\"https://#Section_7\">Train Logistic Regression, KNN, Decision Tree, SVM, and Linear Regression models and return their appropriate accuracy scores</a></li>\n</a></li>\n</div>\n<p>Estimated Time Needed: <strong>180 min</strong></p>\n</div>\n\n<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "# Instructions\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In this notebook, you will  practice all the classification algorithms that we have learned in this course.\n\n\nBelow, is where we are going to use the classification algorithms to create a model based on our training data and evaluate our testing data using evaluation metrics learned in the course.\n\nWe will use some of the algorithms taught in the course, specifically:\n\n1. Linear Regression\n2. KNN\n3. Decision Trees\n4. Logistic Regression\n5. SVM\n\nWe will evaluate our models using:\n\n1.  Accuracy Score\n2.  Jaccard Index\n3.  F1-Score\n4.  LogLoss\n5.  Mean Absolute Error\n6.  Mean Squared Error\n7.  R2-Score\n\nFinally, you will use your models to generate the report at the end. \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "# About The Dataset\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "The original source of the data is Australian Government's Bureau of Meteorology and the latest data can be gathered from [http://www.bom.gov.au/climate/dwo/](http://www.bom.gov.au/climate/dwo/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01).\n\nThe dataset to be used has extra columns like 'RainToday' and our target is 'RainTomorrow', which was gathered from the Rattle at [https://bitbucket.org/kayontoga/rattle/src/master/data/weatherAUS.RData](https://bitbucket.org/kayontoga/rattle/src/master/data/weatherAUS.RData?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01)\n\n\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "This dataset contains observations of weather metrics for each day from 2008 to 2017. The **weatherAUS.csv** dataset includes the following fields:\n\n| Field         | Description                                           | Unit            | Type   |\n| ------------- | ----------------------------------------------------- | --------------- | ------ |\n| Date          | Date of the Observation in YYYY-MM-DD                 | Date            | object |\n| Location      | Location of the Observation                           | Location        | object |\n| MinTemp       | Minimum temperature                                   | Celsius         | float  |\n| MaxTemp       | Maximum temperature                                   | Celsius         | float  |\n| Rainfall      | Amount of rainfall                                    | Millimeters     | float  |\n| Evaporation   | Amount of evaporation                                 | Millimeters     | float  |\n| Sunshine      | Amount of bright sunshine                             | hours           | float  |\n| WindGustDir   | Direction of the strongest gust                       | Compass Points  | object |\n| WindGustSpeed | Speed of the strongest gust                           | Kilometers/Hour | object |\n| WindDir9am    | Wind direction averaged of 10 minutes prior to 9am    | Compass Points  | object |\n| WindDir3pm    | Wind direction averaged of 10 minutes prior to 3pm    | Compass Points  | object |\n| WindSpeed9am  | Wind speed averaged of 10 minutes prior to 9am        | Kilometers/Hour | float  |\n| WindSpeed3pm  | Wind speed averaged of 10 minutes prior to 3pm        | Kilometers/Hour | float  |\n| Humidity9am   | Humidity at 9am                                       | Percent         | float  |\n| Humidity3pm   | Humidity at 3pm                                       | Percent         | float  |\n| Pressure9am   | Atmospheric pressure reduced to mean sea level at 9am | Hectopascal     | float  |\n| Pressure3pm   | Atmospheric pressure reduced to mean sea level at 3pm | Hectopascal     | float  |\n| Cloud9am      | Fraction of the sky obscured by cloud at 9am          | Eights          | float  |\n| Cloud3pm      | Fraction of the sky obscured by cloud at 3pm          | Eights          | float  |\n| Temp9am       | Temperature at 9am                                    | Celsius         | float  |\n| Temp3pm       | Temperature at 3pm                                    | Celsius         | float  |\n| RainToday     | If there was rain today                               | Yes/No          | object |\n| RainTomorrow  | If there is rain tomorrow                             | Yes/No          | float  |\n\nColumn definitions were gathered from [http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml](http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01)\n\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## **Import the required libraries**\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# All Libraries required for this lab are listed below. The libraries pre-installed on Skills Network Labs are commented.\n# !mamba install -qy pandas==1.3.4 numpy==1.21.4 seaborn==0.9.0 matplotlib==3.5.0 scikit-learn==0.20.1\n# Note: If your environment doesn't support \"!mamba install\", use \"!pip install\"",
      "metadata": {
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "# Surpress warnings:\ndef warn(*args, **kwargs):\n    pass\nimport warnings\nwarnings.warn = warn",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "#you are running the lab in your  browser, so we will install the libraries using ``piplite``\nimport piplite\nawait piplite.install(['pandas'])\nawait piplite.install(['numpy'])\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "import pandas as pd\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn import preprocessing\nimport numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn import svm\nfrom sklearn.metrics import jaccard_score\nfrom sklearn.metrics import f1_score\nfrom sklearn.metrics import log_loss\nfrom sklearn.metrics import confusion_matrix, accuracy_score\nimport sklearn.metrics as metrics",
      "metadata": {
        "trusted": true
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "### Importing the Dataset\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "from pyodide.http import pyfetch\n\nasync def download(url, filename):\n    response = await pyfetch(url)\n    if response.status == 200:\n        with open(filename, \"wb\") as f:\n            f.write(await response.bytes())",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillUp/labs/ML-FinalAssignment/Weather_Data.csv'",
      "metadata": {
        "trusted": true
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "await download(path, \"Weather_Data.csv\")\nfilename =\"Weather_Data.csv\"",
      "metadata": {
        "trusted": true
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "df = pd.read_csv(\"Weather_Data.csv\")\ndf.head()\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 8,
      "outputs": [
        {
          "execution_count": 8,
          "output_type": "execute_result",
          "data": {
            "text/plain": "       Date  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine WindGustDir  \\\n0  2/1/2008     19.5     22.4      15.6          6.2       0.0           W   \n1  2/2/2008     19.5     25.6       6.0          3.4       2.7           W   \n2  2/3/2008     21.6     24.5       6.6          2.4       0.1           W   \n3  2/4/2008     20.2     22.8      18.8          2.2       0.0           W   \n4  2/5/2008     19.7     25.7      77.4          4.8       0.0           W   \n\n   WindGustSpeed WindDir9am WindDir3pm  ...  Humidity9am  Humidity3pm  \\\n0             41          S        SSW  ...           92           84   \n1             41          W          E  ...           83           73   \n2             41        ESE        ESE  ...           88           86   \n3             41        NNE          E  ...           83           90   \n4             41        NNE          W  ...           88           74   \n\n   Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  RainToday  \\\n0       1017.6       1017.4         8         8     20.7     20.9        Yes   \n1       1017.9       1016.4         7         7     22.4     24.8        Yes   \n2       1016.7       1015.6         7         8     23.5     23.0        Yes   \n3       1014.2       1011.8         8         8     21.4     20.9        Yes   \n4       1008.3       1004.8         8         8     22.5     25.5        Yes   \n\n   RainTomorrow  \n0           Yes  \n1           Yes  \n2           Yes  \n3           Yes  \n4           Yes  \n\n[5 rows x 22 columns]",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Date</th>\n      <th>MinTemp</th>\n      <th>MaxTemp</th>\n      <th>Rainfall</th>\n      <th>Evaporation</th>\n      <th>Sunshine</th>\n      <th>WindGustDir</th>\n      <th>WindGustSpeed</th>\n      <th>WindDir9am</th>\n      <th>WindDir3pm</th>\n      <th>...</th>\n      <th>Humidity9am</th>\n      <th>Humidity3pm</th>\n      <th>Pressure9am</th>\n      <th>Pressure3pm</th>\n      <th>Cloud9am</th>\n      <th>Cloud3pm</th>\n      <th>Temp9am</th>\n      <th>Temp3pm</th>\n      <th>RainToday</th>\n      <th>RainTomorrow</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>2/1/2008</td>\n      <td>19.5</td>\n      <td>22.4</td>\n      <td>15.6</td>\n      <td>6.2</td>\n      <td>0.0</td>\n      <td>W</td>\n      <td>41</td>\n      <td>S</td>\n      <td>SSW</td>\n      <td>...</td>\n      <td>92</td>\n      <td>84</td>\n      <td>1017.6</td>\n      <td>1017.4</td>\n      <td>8</td>\n      <td>8</td>\n      <td>20.7</td>\n      <td>20.9</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2/2/2008</td>\n      <td>19.5</td>\n      <td>25.6</td>\n      <td>6.0</td>\n      <td>3.4</td>\n      <td>2.7</td>\n      <td>W</td>\n      <td>41</td>\n      <td>W</td>\n      <td>E</td>\n      <td>...</td>\n      <td>83</td>\n      <td>73</td>\n      <td>1017.9</td>\n      <td>1016.4</td>\n      <td>7</td>\n      <td>7</td>\n      <td>22.4</td>\n      <td>24.8</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2/3/2008</td>\n      <td>21.6</td>\n      <td>24.5</td>\n      <td>6.6</td>\n      <td>2.4</td>\n      <td>0.1</td>\n      <td>W</td>\n      <td>41</td>\n      <td>ESE</td>\n      <td>ESE</td>\n      <td>...</td>\n      <td>88</td>\n      <td>86</td>\n      <td>1016.7</td>\n      <td>1015.6</td>\n      <td>7</td>\n      <td>8</td>\n      <td>23.5</td>\n      <td>23.0</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>2/4/2008</td>\n      <td>20.2</td>\n      <td>22.8</td>\n      <td>18.8</td>\n      <td>2.2</td>\n      <td>0.0</td>\n      <td>W</td>\n      <td>41</td>\n      <td>NNE</td>\n      <td>E</td>\n      <td>...</td>\n      <td>83</td>\n      <td>90</td>\n      <td>1014.2</td>\n      <td>1011.8</td>\n      <td>8</td>\n      <td>8</td>\n      <td>21.4</td>\n      <td>20.9</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>2/5/2008</td>\n      <td>19.7</td>\n      <td>25.7</td>\n      <td>77.4</td>\n      <td>4.8</td>\n      <td>0.0</td>\n      <td>W</td>\n      <td>41</td>\n      <td>NNE</td>\n      <td>W</td>\n      <td>...</td>\n      <td>88</td>\n      <td>74</td>\n      <td>1008.3</td>\n      <td>1004.8</td>\n      <td>8</td>\n      <td>8</td>\n      <td>22.5</td>\n      <td>25.5</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n  </tbody>\n</table>\n<p>5 rows × 22 columns</p>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### Data Preprocessing\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### One Hot Encoding\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "First, we need to perform one hot encoding to convert categorical variables to binary variables.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed = pd.get_dummies(data=df, columns=['RainToday', 'WindGustDir', 'WindDir9am', 'WindDir3pm'])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "Next, we replace the values of the 'RainTomorrow' column changing them from a categorical column to a binary column. We do not use the `get_dummies` method because we would end up with two columns for 'RainTomorrow' and we do not want, since 'RainTomorrow' is our target.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed.replace(['No', 'Yes'], [0,1], inplace=True)\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "### Training Data and Test Data\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Now, we set our 'features' or x values and our Y or target variable.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed.drop('Date',axis=1,inplace=True)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed = df_sydney_processed.astype(float)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "features = df_sydney_processed.drop(columns='RainTomorrow', axis=1)\nY = df_sydney_processed['RainTomorrow']\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "### Linear Regression\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q1) Use the `train_test_split` function to split the `features` and `Y` dataframes with a `test_size` of `0.2` and the `random_state` set to `10`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {
        "trusted": true
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "x_train, x_test, y_train, y_test = train_test_split(features, Y, test_size = 0.2, random_state = 10)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q2) Create and train a Linear Regression model called LinearReg using the training data (`x_train`, `y_train`).\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot\nfrom sklearn import linear_model",
      "metadata": {
        "trusted": true
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "LinearReg = linear_model.LinearRegression()\nx_train = np.asarray(x_train)\ny_train = np.asarray(y_train)\nLinearReg.fit(x_train, y_train)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 17,
      "outputs": [
        {
          "execution_count": 17,
          "output_type": "execute_result",
          "data": {
            "text/plain": "LinearRegression()",
            "text/html": "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q3) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {
        "trusted": true
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = LinearReg.predict(x_test)\npredictions",
      "metadata": {
        "trusted": true
      },
      "execution_count": 94,
      "outputs": [
        {
          "name": "stderr",
          "text": "/lib/python3.11/site-packages/sklearn/base.py:432: UserWarning: X has feature names, but LinearRegression was fitted without feature names\n  warnings.warn(\n",
          "output_type": "stream"
        },
        {
          "execution_count": 94,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([ 3.31874847e-01, -1.65748596e-02,  4.81964111e-01,  3.05580139e-01,\n       -1.37138367e-02,  8.85749817e-01,  2.69340515e-01,  7.16285706e-02,\n        2.17414856e-01,  1.68125153e-01,  5.41454315e-01,  4.07947540e-01,\n        4.38701630e-01, -6.62460327e-02, -6.46018982e-02, -7.95631409e-02,\n        4.06063080e-01,  2.37541199e-02,  1.00151062e-01,  7.35740662e-02,\n        5.46237946e-01,  9.17686462e-01,  5.36270142e-02,  9.10720825e-02,\n        2.40356445e-01,  1.45378113e-02, -2.03933716e-02,  2.23979950e-01,\n        4.17510986e-01,  3.37432861e-01,  4.55280304e-01, -2.18322754e-01,\n        3.28350067e-01,  7.65735626e-01,  6.96762085e-01,  4.14558411e-01,\n        5.61283112e-01,  1.28719330e-01,  8.17050934e-01,  1.86832428e-01,\n        3.70349884e-01,  7.96127319e-03,  3.94702911e-01,  2.20108032e-01,\n       -1.79901123e-02,  9.60693359e-02,  2.99144745e-01,  3.81809235e-01,\n        3.11748505e-01,  5.02902985e-01,  7.24567413e-01,  2.57148743e-02,\n        5.48004150e-01,  1.63360596e-01,  4.60483551e-01,  8.70727539e-01,\n       -1.54830933e-01,  4.33845520e-02,  1.00921631e-01,  3.87039185e-02,\n       -1.23275757e-01,  4.35626984e-01, -6.65817261e-02,  1.00044250e-01,\n        1.79241180e-01,  1.53690338e-01,  3.45993042e-02,  3.32870483e-02,\n        1.24740601e-01,  2.27401733e-01,  8.43200684e-02,  7.71240234e-01,\n        1.71012878e-01,  1.52397156e-01, -8.66737366e-02,  2.39128113e-01,\n        1.37485504e-01,  1.30378723e-01, -1.93405151e-03,  1.86920166e-01,\n        1.65870667e-01,  4.92835999e-01,  4.86095428e-01,  8.87298584e-03,\n        7.23979950e-01,  2.13989258e-01, -3.35311890e-03, -2.46238708e-02,\n        9.21848297e-01, -2.05459595e-02,  3.40927124e-01,  4.45289612e-01,\n        4.68284607e-01,  2.41199493e-01,  5.91472626e-01,  3.83258820e-01,\n        5.09506226e-01,  3.70712280e-01,  1.28818512e-01,  4.45533752e-01,\n        2.15141296e-01,  9.02648926e-01, -8.40454102e-02,  8.76766205e-01,\n        5.20572662e-01,  3.25454712e-01,  1.65508270e-01,  9.98306274e-03,\n        3.15933228e-01,  2.90668488e-01,  1.61605835e-01,  6.87789917e-03,\n        6.90532684e-01,  6.65538788e-01,  7.73162842e-02,  3.52779388e-01,\n        6.83307648e-01,  3.34346771e-01, -9.14878845e-02,  3.68312836e-01,\n        6.70982361e-01, -5.90209961e-02,  2.81578064e-01,  4.03900146e-01,\n        3.02505493e-03,  2.96440125e-01,  2.39471436e-01,  2.73506165e-01,\n        5.50281525e-01, -2.34718323e-02,  5.53398132e-02,  4.15397644e-01,\n       -7.22579956e-02,  1.50962830e-01,  6.77223206e-01,  4.96139526e-01,\n        1.73034668e-01, -6.77490234e-02, -1.77726746e-01,  5.85384369e-01,\n        1.80496216e-01,  7.41683960e-01,  3.11843872e-01, -9.56344604e-03,\n       -3.34930420e-02,  8.39321136e-01,  2.42362976e-01,  7.66895294e-01,\n        8.51505280e-01,  3.21235657e-02,  1.06266022e-01,  3.38500977e-01,\n        1.13773346e+00, -5.68084717e-02,  4.02069092e-03,  7.59876251e-01,\n        2.62153625e-01,  2.23705292e-01,  5.85269928e-01,  4.26376343e-01,\n        6.75693512e-01,  1.99539185e-01,  7.15232849e-01,  5.33943176e-01,\n       -2.94265747e-02, -5.29518127e-02,  1.23802185e-01, -4.87136841e-02,\n        4.26013947e-01,  1.44889832e-01,  3.26438904e-01,  3.51398468e-01,\n        1.26194000e-01,  8.10962677e-01,  3.39073181e-01, -1.78783417e-01,\n        1.39041901e-01,  2.03025818e-01,  2.21843719e-01,  1.04520416e+00,\n        6.25930786e-01,  1.68651581e-01,  1.09191895e-01,  5.38841248e-01,\n        7.79525757e-01,  7.48912811e-01,  1.14196777e-01,  2.35942841e-01,\n        3.30646515e-01,  5.78041077e-02,  3.40423584e-02,  9.58404541e-02,\n        9.41864014e-01, -5.25665283e-03,  2.31018066e-02,  6.70032501e-01,\n        8.06121826e-02,  6.13510132e-01,  1.69094086e-01,  3.95572662e-01,\n       -9.56077576e-02,  1.21826172e-01,  2.36690521e-01,  3.37944031e-02,\n       -8.29086304e-02,  6.66057587e-01,  6.51058197e-01,  1.47521973e-01,\n        7.13157654e-02,  7.93289185e-01, -6.16149902e-02,  2.40211487e-02,\n        2.02644348e-01,  5.41637421e-01,  4.25323486e-01, -4.75616455e-02,\n       -8.38279724e-02,  8.15559387e-01,  2.63416290e-01,  4.34570312e-02,\n        6.49185181e-02,  5.64476013e-01, -7.24487305e-02,  1.00632095e+00,\n        9.40689087e-01,  2.78472900e-04,  2.40982056e-01, -2.29492188e-02,\n        1.37561798e-01,  2.18498230e-01,  5.06839752e-01,  8.50963593e-01,\n        3.64032745e-01,  2.59197235e-01,  2.56774902e-01,  3.42517853e-01,\n        1.53507233e-01,  1.57035828e-01, -5.28526306e-02,  6.62158966e-01,\n        3.11874390e-01,  2.17666626e-02,  5.57575226e-01, -8.20350647e-02,\n        9.34295654e-02,  5.00720978e-01,  8.17276001e-01,  4.03079987e-01,\n        4.88002777e-01,  1.04125977e-01,  1.16916656e-01,  4.09141541e-01,\n        1.30252838e-01,  3.10173035e-02,  5.60600281e-01, -6.96258545e-02,\n        2.90374756e-02, -7.18612671e-02,  1.11064911e-01,  6.77017212e-01,\n        5.97145081e-01,  8.51539612e-01,  1.63917542e-02,  3.15479279e-01,\n       -6.52313232e-02, -1.08432770e-01,  3.19229126e-01,  3.18653107e-01,\n       -4.42237854e-02,  2.73635864e-01,  2.03960419e-01,  1.73835754e-01,\n        1.57241821e-02,  7.01103210e-02,  2.45761871e-01,  1.43074036e-01,\n        9.71832275e-02, -4.41894531e-02,  6.98940277e-01,  2.21214294e-02,\n        4.47319031e-01,  4.18506622e-01,  5.91789246e-01,  9.39121246e-01,\n        7.43225098e-01,  8.15620422e-02, -2.26379395e-01,  3.83750916e-01,\n        2.43213654e-01,  6.44317627e-01,  6.87740326e-01,  6.74171448e-02,\n       -7.07664490e-02,  5.35232544e-01,  2.92663574e-02,  6.63166046e-01,\n        3.88233185e-01,  2.47032166e-01, -2.42248535e-01, -1.26914978e-02,\n        7.59025574e-01, -3.38058472e-02, -3.08292389e-01,  2.37091064e-01,\n       -2.65384674e-01,  5.48973083e-01,  8.03718567e-01,  3.31905365e-01,\n        1.77875519e-01,  2.92194366e-01,  7.45582581e-01,  2.43057251e-01,\n        4.07188416e-01,  1.10023499e-01,  4.82997894e-01,  8.30055237e-01,\n        2.15690613e-01, -1.65161133e-01,  3.34697723e-01,  4.65587616e-01,\n        2.39364624e-01,  4.36485291e-01,  5.51757812e-02,  1.92428589e-01,\n       -1.18320465e-01,  6.98249817e-01,  1.08489990e-01,  4.93240356e-02,\n        7.14950562e-01,  5.08960724e-01,  4.28432465e-01,  1.87854767e-01,\n        6.70345306e-01,  2.35439301e-01,  6.37207031e-02,  3.14064026e-02,\n        1.39698029e-01,  3.33152771e-01,  8.77761841e-03,  2.67295837e-02,\n        7.19623566e-01,  8.96434784e-01,  2.33425140e-01, -5.83648682e-02,\n        5.87287903e-01,  5.80158234e-01,  7.69489288e-01,  3.26080322e-02,\n        6.27941132e-01,  8.64639282e-02,  5.60379028e-03,  8.26862335e-01,\n        1.03530884e-01,  1.09016418e-01,  2.02575684e-01,  1.55223846e-01,\n        4.82971191e-01,  9.00611877e-02, -3.82690430e-02, -1.39541626e-02,\n        8.18061829e-02,  1.91101074e-01,  3.29059601e-01,  1.29665375e-01,\n        1.18221283e-01,  8.81614685e-01,  9.34600830e-02, -1.79378510e-01,\n       -1.99714661e-01,  7.54928589e-03,  1.30596161e-01,  3.35426331e-01,\n        4.64088440e-01,  1.65435791e-01,  6.82106018e-02,  1.11349487e+00,\n        9.30824280e-02,  3.71364594e-01,  3.49807739e-01,  2.18635559e-01,\n        2.43976593e-01,  3.89938354e-02,  9.09309387e-02,  7.91473389e-02,\n        5.27954102e-03,  4.80766296e-01,  9.40246582e-02, -9.38415527e-04,\n        1.00121689e+00,  6.83860779e-01,  2.98854828e-01,  1.10679626e-01,\n        1.98989868e-01, -5.61904907e-02,  2.62596130e-01,  3.20343018e-01,\n        7.56248474e-01,  9.10491943e-02,  1.23672485e-01,  1.47155762e-01,\n        3.14826965e-02,  1.49784088e-01,  1.23764038e-01,  2.06439972e-01,\n       -3.18336487e-02, -6.25343323e-02,  3.29246521e-01,  2.02064514e-02,\n        3.46527100e-02,  1.06384277e-01,  2.33669281e-01,  1.41868591e-02,\n        2.80380249e-03,  8.94355774e-02,  4.31312561e-01, -5.29212952e-02,\n       -2.22381592e-01,  9.99679565e-02,  1.84486389e-01,  1.34963989e-02,\n        8.19091797e-02, -6.25991821e-03,  1.41887665e-01,  2.21832275e-01,\n       -7.18040466e-02,  2.45304108e-01, -1.42566681e-01, -4.47616577e-02,\n        4.35577393e-01,  2.84301758e-01,  1.88552856e-01,  1.83151245e-01,\n        6.02787018e-01,  5.28419495e-01, -1.02027893e-01,  9.21173096e-02,\n        4.25910950e-02, -8.46939087e-02,  3.95355225e-01,  2.07489014e-01,\n        6.83197021e-01,  8.53542328e-01,  7.15850830e-01,  1.59851074e-01,\n        2.35839844e-01,  8.33129883e-03,  1.09766769e+00,  3.95812988e-02,\n        6.13147736e-01,  2.30224609e-01,  2.98076630e-01, -6.26220703e-02,\n       -9.31205750e-02,  8.86325836e-01,  2.85942078e-01,  2.17838287e-01,\n       -9.20143127e-02,  4.44168091e-01,  3.70525360e-01, -5.80406189e-02,\n        6.20811462e-01, -1.28833771e-01,  2.75592804e-01,  7.01103210e-01,\n        6.61128998e-01,  2.61356354e-01, -1.58443451e-01,  5.99647522e-01,\n        3.73630524e-01, -3.26118469e-02,  5.89752197e-03, -6.15921021e-02,\n        4.45198059e-01,  8.55632782e-01,  4.27776337e-01,  1.11160278e-01,\n        6.29077911e-01,  2.25982666e-01, -1.88629150e-01,  5.14385223e-01,\n        3.96198273e-01, -2.82707214e-02, -2.98156738e-02,  4.18895721e-01,\n        1.28562927e-01,  1.27391815e-01,  6.56814575e-01,  3.23547363e-01,\n       -2.81524658e-03,  6.86096191e-01,  9.69402313e-01,  1.05628967e-01,\n        9.79419708e-01,  2.60005951e-01,  1.92443848e-01,  2.59552002e-02,\n        1.94084167e-01, -6.72531128e-02,  6.63131714e-01,  2.78663635e-01,\n        2.99026489e-01,  7.39032745e-01, -5.83457947e-02,  9.76791382e-02,\n        4.61059570e-01,  1.78714752e-01, -1.83982849e-02, -3.50570679e-03,\n        6.57466888e-01, -1.91612244e-02,  2.34527588e-02,  2.34458923e-01,\n        8.88023376e-02, -1.16977692e-01,  4.90711212e-01,  8.25950623e-01,\n       -1.15692139e-01,  1.71718597e-01,  5.67558289e-01,  2.99098969e-01,\n        1.13910675e-01,  2.23678589e-01,  3.41842651e-01, -1.61933899e-02,\n        3.66546631e-01,  4.43733215e-01,  1.45996094e-01, -2.19612122e-02,\n        1.06861115e-01,  4.11094666e-01,  5.71441650e-03,  1.36947632e-02,\n        1.53198242e-01,  4.87518311e-01,  6.79801941e-01,  1.86325073e-01,\n        1.07509613e+00, -1.93138123e-02,  4.24983978e-01,  5.37525177e-01,\n        6.46629333e-02, -2.32852936e-01, -8.63838196e-02, -4.74967957e-02,\n        1.13361359e-01,  5.50750732e-01,  1.78924561e-01,  4.76791382e-01,\n        3.21872711e-01,  1.02485657e-01,  2.69531250e-01,  4.33910370e-01,\n        7.31353760e-02,  3.28315735e-01,  4.53033447e-01,  1.92047119e-01,\n        8.50486755e-02, -7.01141357e-03,  2.85614014e-01,  2.39509583e-01,\n        2.73612976e-01,  4.30648804e-01,  6.87469482e-01,  6.35429382e-01,\n        1.41807556e-01,  2.56004333e-02,  1.92417145e-01,  1.14295959e-01,\n        3.18824768e-01,  2.49935150e-01,  5.47981262e-02,  7.94452667e-01,\n        6.34056091e-01,  9.54437256e-02,  9.25407410e-02,  7.42530823e-02,\n        1.60842896e-01,  7.60688782e-02,  5.08354187e-01,  3.80859375e-02,\n        1.79065704e-01, -1.40792847e-01,  8.96301270e-02,  1.36306381e+00,\n        1.61472321e-01,  5.33535004e-01, -6.72683716e-02,  2.87883759e-01,\n        6.07643127e-02,  4.25605774e-02,  7.08122253e-01, -1.01329803e-01,\n        9.54399109e-02,  3.68469238e-01, -1.00635529e-01,  2.21233368e-01,\n       -5.22918701e-02,  5.27572632e-03,  6.57314301e-01,  5.41526794e-01,\n       -1.21002197e-02,  2.72521973e-02,  6.23588562e-01, -3.62586975e-02,\n        4.02297974e-02, -1.16016388e-01,  1.64710999e-01,  4.61933136e-01,\n        3.05500031e-01,  2.60639191e-01, -7.64236450e-02, -2.27661133e-02,\n        1.31111145e-02,  1.35425568e-01,  2.42755890e-01,  9.79728699e-02,\n        7.54985809e-01,  2.93407440e-01,  9.41429138e-02, -3.41758728e-02,\n        3.51715088e-02,  5.94116211e-01,  1.59408569e-01,  4.48520660e-01,\n        1.11808777e-02,  3.71196747e-01,  6.05323792e-01,  2.72724152e-01,\n        1.38294220e-01,  2.45464325e-01,  1.05751038e-01,  6.10084534e-01,\n        1.74034119e-01,  3.71398926e-01,  6.05144501e-01,  5.74707031e-01,\n       -1.28990173e-01, -4.43458557e-02, -1.77879333e-02,  6.21543884e-01,\n        3.89865875e-01,  1.09924316e+00, -6.16149902e-02, -3.05557251e-02,\n        6.42860413e-01, -3.50952148e-04,  1.24053955e-02,  2.56114960e-01,\n        8.45161438e-01, -3.28750610e-02,  5.94554901e-01,  3.83941650e-01,\n       -1.07837677e-01,  4.30606842e-01,  6.42089844e-01])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q4) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {
        "trusted": true
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "from sklearn.metrics import r2_score\nLinearRegression_MAE = np.mean(np.absolute(predictions - y_test))\nLinearRegression_MSE = np.mean((predictions - y_test)) ** 2\nLinearRegression_R2 = r2_score(predictions , y_test)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q5) Show the MAE, MSE, and R2 in a tabular format using data frame for the linear model.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {
        "trusted": true
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "data = {\"matrics\" : [\"Mean Absolute Error\", \"Mean Squared Error\", \"R2_Score\"],\n       \"score\" : [LinearRegression_MAE, LinearRegression_MSE, LinearRegression_R2]}\nReport = pd.DataFrame(data)\nReport\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 95,
      "outputs": [
        {
          "execution_count": 95,
          "output_type": "execute_result",
          "data": {
            "text/plain": "               matrics     score\n0  Mean Absolute Error  0.256319\n1   Mean Squared Error  0.000039\n2             R2_Score -0.384717",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>matrics</th>\n      <th>score</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Mean Absolute Error</td>\n      <td>0.256319</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Mean Squared Error</td>\n      <td>0.000039</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>R2_Score</td>\n      <td>-0.384717</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### KNN\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q6) Create and train a KNN model called KNN using the training data (`x_train`, `y_train`) with the `n_neighbors` parameter set to `4`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {
        "trusted": true
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "KNN = KNeighborsClassifier(n_neighbors = 4).fit(x_train ,y_train)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q7) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {
        "trusted": true
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = KNN.predict(x_test)\npredictions",
      "metadata": {
        "trusted": true
      },
      "execution_count": 96,
      "outputs": [
        {
          "name": "stderr",
          "text": "/lib/python3.11/site-packages/sklearn/base.py:432: UserWarning: X has feature names, but KNeighborsClassifier was fitted without feature names\n  warnings.warn(\n",
          "output_type": "stream"
        },
        {
          "execution_count": 96,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,\n       0., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1.,\n       0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1.,\n       0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 1., 1., 0., 0., 0., 1.,\n       0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0.,\n       0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 1.,\n       0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       1., 0., 0., 0., 1., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0.,\n       0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       1., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,\n       1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 1., 0., 1.,\n       0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0.,\n       0., 0., 1., 0., 1., 0., 0., 0., 0.])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q8) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {
        "trusted": true
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "KNN_Accuracy_Score = accuracy_score(y_test, predictions)\nKNN_JaccardIndex = jaccard_score(y_test, predictions)\nKNN_F1_Score =  f1_score(y_test, predictions)\n\ndata = {\n    'Metric': ['Accuracy Score', 'Jaccard Index', 'F1-Score'],\n    'Score': [KNN_Accuracy_Score, KNN_JaccardIndex, KNN_F1_Score]\n}\nReport = pd.DataFrame(data)\nReport",
      "metadata": {
        "trusted": true
      },
      "execution_count": 97,
      "outputs": [
        {
          "execution_count": 97,
          "output_type": "execute_result",
          "data": {
            "text/plain": "           Metric     Score\n0  Accuracy Score  0.839695\n1   Jaccard Index  0.461538\n2        F1-Score  0.631579",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Metric</th>\n      <th>Score</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Accuracy Score</td>\n      <td>0.839695</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Jaccard Index</td>\n      <td>0.461538</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>F1-Score</td>\n      <td>0.631579</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### Decision Tree\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q9) Create and train a Decision Tree model called Tree using the training data (`x_train`, `y_train`).\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "Tree = DecisionTreeClassifier(criterion=\"entropy\", max_depth = 4)\nDT = Tree.fit(x_train, y_train)\nDT",
      "metadata": {
        "trusted": true
      },
      "execution_count": 40,
      "outputs": [
        {
          "execution_count": 40,
          "output_type": "execute_result",
          "data": {
            "text/plain": "DecisionTreeClassifier(criterion='entropy', max_depth=4)",
            "text/html": "<style>#sk-container-id-4 {color: black;background-color: white;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>DecisionTreeClassifier(criterion=&#x27;entropy&#x27;, max_depth=4)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" checked><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">DecisionTreeClassifier</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeClassifier(criterion=&#x27;entropy&#x27;, max_depth=4)</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q10) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = Tree.predict(x_test)\npredictions",
      "metadata": {
        "trusted": true
      },
      "execution_count": 98,
      "outputs": [
        {
          "name": "stderr",
          "text": "/lib/python3.11/site-packages/sklearn/base.py:432: UserWarning: X has feature names, but DecisionTreeClassifier was fitted without feature names\n  warnings.warn(\n",
          "output_type": "stream"
        },
        {
          "execution_count": 98,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([1., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,\n       0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,\n       0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1.,\n       0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0., 1., 1., 0., 1.,\n       0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 1., 1., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 1.,\n       0., 0., 1., 0., 0., 1., 0., 1., 0., 1., 1., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 1., 1., 0., 0., 0., 0., 1., 1., 0., 0., 1., 1., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0.,\n       0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,\n       0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 1., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,\n       0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0., 0., 1., 0.,\n       1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,\n       1., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0.,\n       0., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.,\n       1., 1., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 1., 1.,\n       1., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,\n       1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 1., 0., 1.,\n       0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 1., 0.,\n       0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0.,\n       0., 0., 1., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0.,\n       0., 1., 1., 0., 1., 1., 0., 0., 0.])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q11) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "Tree_Accuracy_Score = accuracy_score(y_test, predictions)\nTree_JaccardIndex = jaccard_score(y_test, predictions)\nTree_F1_Score = f1_score(y_test, predictions)\n\ndata = {\n    'Metric': ['Accuracy Score', 'Jaccard Index', 'F1-Score'],\n    'Score': [Tree_Accuracy_Score, Tree_JaccardIndex, Tree_F1_Score]\n}\nReport = pd.DataFrame(data)\nReport",
      "metadata": {
        "trusted": true
      },
      "execution_count": 99,
      "outputs": [
        {
          "execution_count": 99,
          "output_type": "execute_result",
          "data": {
            "text/plain": "           Metric     Score\n0  Accuracy Score  0.827481\n1   Jaccard Index  0.481651\n2        F1-Score  0.650155",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Metric</th>\n      <th>Score</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Accuracy Score</td>\n      <td>0.827481</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Jaccard Index</td>\n      <td>0.481651</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>F1-Score</td>\n      <td>0.650155</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "\n\n\n\n\n### Logistic Regression\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q12) Use the `train_test_split` function to split the `features` and `Y` dataframes with a `test_size` of `0.2` and the `random_state` set to `1`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "x_train, x_test, y_train, y_test = train_test_split(features, Y, test_size = 0.2, random_state = 1)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q13) Create and train a LogisticRegression model called LR using the training data (`x_train`, `y_train`) with the `solver` parameter set to `liblinear`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "LR = LogisticRegression(C=0.01, solver='liblinear').fit(x_train,y_train)\nLR",
      "metadata": {
        "trusted": true
      },
      "execution_count": 100,
      "outputs": [
        {
          "execution_count": 100,
          "output_type": "execute_result",
          "data": {
            "text/plain": "LogisticRegression(C=0.01, solver='liblinear')",
            "text/html": "<style>#sk-container-id-8 {color: black;background-color: white;}#sk-container-id-8 pre{padding: 0;}#sk-container-id-8 div.sk-toggleable {background-color: white;}#sk-container-id-8 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-8 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-8 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-8 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-8 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-8 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-8 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-8 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-8 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-8 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-8 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-8 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-8 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-8 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-8 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-8 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-8 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-8 div.sk-item {position: relative;z-index: 1;}#sk-container-id-8 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-8 div.sk-item::before, #sk-container-id-8 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-8 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-8 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-8 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-8 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-8 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-8 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-8 div.sk-label-container {text-align: center;}#sk-container-id-8 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-8 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-8\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression(C=0.01, solver=&#x27;liblinear&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-8\" type=\"checkbox\" checked><label for=\"sk-estimator-id-8\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression(C=0.01, solver=&#x27;liblinear&#x27;)</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q14) Now, use the `predict` and `predict_proba` methods on the testing data (`x_test`) and save it as 2 arrays `predictions` and `predict_proba`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {
        "trusted": true
      },
      "execution_count": 76,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = LR.predict(x_test)\npredictions",
      "metadata": {
        "trusted": true
      },
      "execution_count": 101,
      "outputs": [
        {
          "execution_count": 101,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1.,\n       1., 1., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,\n       0., 1., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1.,\n       0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 1., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,\n       0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 1., 1., 0., 0., 0., 1.,\n       0., 0., 1., 0., 0., 1., 0., 1., 0., 1., 1., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 1., 0., 0., 1., 1., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0.,\n       0., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0.,\n       1., 0., 1., 1., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 1., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,\n       0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 1., 1., 0., 0., 0., 0.,\n       1., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1.,\n       1., 0., 0., 0., 1., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.,\n       1., 1., 0., 0., 1., 1., 1., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1.,\n       1., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.,\n       0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0., 0.,\n       1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 1., 0., 1.,\n       0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1., 0.,\n       0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 1., 0., 0., 0., 0.,\n       0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,\n       0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0.,\n       0., 0., 1., 0., 1., 0., 0., 0., 1.])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "predict_proba = LR.predict_proba(x_test)\npredict_proba",
      "metadata": {
        "trusted": true
      },
      "execution_count": 102,
      "outputs": [
        {
          "execution_count": 102,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([[0.71865751, 0.28134249],\n       [0.9758825 , 0.0241175 ],\n       [0.49701165, 0.50298835],\n       ...,\n       [0.97264147, 0.02735853],\n       [0.73340911, 0.26659089],\n       [0.38535984, 0.61464016]])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q15) Using the `predictions`, `predict_proba` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {
        "trusted": true
      },
      "execution_count": 79,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "LR_Accuracy_Score = accuracy_score(y_test, predictions)\nLR_JaccardIndex = jaccard_score(y_test, predictions,pos_label=0)\nLR_F1_Score = f1_score(y_test, predictions, average='micro')\nLR_Log_Loss = log_loss(y_test, predict_proba)\n\n\ndata = {\n    'Metric': ['Accuracy Score', 'F1-Score', 'Log Loss', 'Jaccard Index (Class 0)'],\n    'Score': [LR_Accuracy_Score, LR_F1_Score, LR_Log_Loss, LR_JaccardIndex]\n}\nReport = pd.DataFrame(data)\nReport",
      "metadata": {
        "trusted": true
      },
      "execution_count": 103,
      "outputs": [
        {
          "execution_count": 103,
          "output_type": "execute_result",
          "data": {
            "text/plain": "                    Metric     Score\n0           Accuracy Score  0.827481\n1                 F1-Score  0.827481\n2                 Log Loss  0.380085\n3  Jaccard Index (Class 0)  0.794171",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Metric</th>\n      <th>Score</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Accuracy Score</td>\n      <td>0.827481</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>F1-Score</td>\n      <td>0.827481</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Log Loss</td>\n      <td>0.380085</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Jaccard Index (Class 0)</td>\n      <td>0.794171</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### SVM\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q16) Create and train a SVM model called SVM using the training data (`x_train`, `y_train`).\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {
        "trusted": true
      },
      "execution_count": 57,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "SVM = svm.SVC(kernel='rbf')\nSVM.fit(x_train, y_train)\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 104,
      "outputs": [
        {
          "execution_count": 104,
          "output_type": "execute_result",
          "data": {
            "text/plain": "SVC()",
            "text/html": "<style>#sk-container-id-9 {color: black;background-color: white;}#sk-container-id-9 pre{padding: 0;}#sk-container-id-9 div.sk-toggleable {background-color: white;}#sk-container-id-9 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-9 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-9 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-9 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-9 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-9 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-9 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-9 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-9 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-9 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-9 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-9 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-9 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-9 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-9 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-9 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-9 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-9 div.sk-item {position: relative;z-index: 1;}#sk-container-id-9 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-9 div.sk-item::before, #sk-container-id-9 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-9 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-9 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-9 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-9 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-9 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-9 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-9 div.sk-label-container {text-align: center;}#sk-container-id-9 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-9 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-9\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SVC()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-9\" type=\"checkbox\" checked><label for=\"sk-estimator-id-9\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SVC</label><div class=\"sk-toggleable__content\"><pre>SVC()</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q17) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {
        "trusted": true
      },
      "execution_count": 59,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = SVM.predict(x_test)\npredictions",
      "metadata": {
        "trusted": true
      },
      "execution_count": 105,
      "outputs": [
        {
          "execution_count": 105,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0.])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q18) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "SVM_Accuracy_Score =  accuracy_score(y_test, predictions)\nSVM_JaccardIndex = jaccard_score(y_test, predictions,pos_label=0)\nSVM_F1_Score = f1_score(y_test, predictions, average='weighted') ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 106,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "### Report\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q19) Show the Accuracy,Jaccard Index,F1-Score and LogLoss in a tabular format using data frame for all of the above models.\n\n\\*LogLoss is only for Logistic Regression Model\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "\nmodels = {\n    'Linear Regression': {\"matrics\" : [\"Mean Absolute Error\", \"Mean Squared Error\", \"R2_Score\"],\n       \"score\" : [LinearRegression_MAE, LinearRegression_MSE, LinearRegression_R2]                         },\n    \n    'KNN': {'Metric': ['Accuracy Score', 'Jaccard Index', 'F1-Score'],\n    'Score': [KNN_Accuracy_Score, KNN_JaccardIndex, KNN_F1_Score]\n           },   \n    'Decision Tree': {\n    'Metric': ['Accuracy Score', 'Jaccard Index', 'F1-Score'],\n    'Score': [Tree_Accuracy_Score, Tree_JaccardIndex, Tree_F1_Score]\n            },  \n    'Logistic Regression': {'Metric': ['Accuracy Score', 'F1-Score', 'Log Loss', 'Jaccard Index (Class 0)'],\n    'Score': [LR_Accuracy_Score, LR_F1_Score, LR_Log_Loss, LR_JaccardIndex]\n             },  \n    'SVM': {'Metric': ['Accuracy Score', 'Jaccard Index', 'F1-Score'],\n    'Score': [SVM_Accuracy_Score, SVM_JaccardIndex, SVM_F1_Score]\n           }\n}\n\nall_data = []\nfor model_name, model_data in models.items():\n    data = {'Model': model_name}\n    data.update(model_data)\n    all_data.append(data)\n    \nReport = pd.DataFrame(all_data)\n\nReport",
      "metadata": {
        "trusted": true
      },
      "execution_count": 107,
      "outputs": [
        {
          "execution_count": 107,
          "output_type": "execute_result",
          "data": {
            "text/plain": "                 Model                                            matrics  \\\n0    Linear Regression  [Mean Absolute Error, Mean Squared Error, R2_S...   \n1                  KNN                                                NaN   \n2        Decision Tree                                                NaN   \n3  Logistic Regression                                                NaN   \n4                  SVM                                                NaN   \n\n                                               score  \\\n0  [0.2563193284828244, 3.937411875993206e-05, -0...   \n1                                                NaN   \n2                                                NaN   \n3                                                NaN   \n4                                                NaN   \n\n                                              Metric  \\\n0                                                NaN   \n1          [Accuracy Score, Jaccard Index, F1-Score]   \n2          [Accuracy Score, Jaccard Index, F1-Score]   \n3  [Accuracy Score, F1-Score, Log Loss, Jaccard I...   \n4          [Accuracy Score, Jaccard Index, F1-Score]   \n\n                                               Score  \n0                                                NaN  \n1  [0.8396946564885496, 0.46153846153846156, 0.63...  \n2  [0.8274809160305343, 0.481651376146789, 0.6501...  \n3  [0.8274809160305343, 0.8274809160305343, 0.380...  \n4  [0.7221374045801526, 0.7221374045801526, 0.605...  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Model</th>\n      <th>matrics</th>\n      <th>score</th>\n      <th>Metric</th>\n      <th>Score</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Linear Regression</td>\n      <td>[Mean Absolute Error, Mean Squared Error, R2_S...</td>\n      <td>[0.2563193284828244, 3.937411875993206e-05, -0...</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>KNN</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>[Accuracy Score, Jaccard Index, F1-Score]</td>\n      <td>[0.8396946564885496, 0.46153846153846156, 0.63...</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Decision Tree</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>[Accuracy Score, Jaccard Index, F1-Score]</td>\n      <td>[0.8274809160305343, 0.481651376146789, 0.6501...</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Logistic Regression</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>[Accuracy Score, F1-Score, Log Loss, Jaccard I...</td>\n      <td>[0.8274809160305343, 0.8274809160305343, 0.380...</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>SVM</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>[Accuracy Score, Jaccard Index, F1-Score]</td>\n      <td>[0.7221374045801526, 0.7221374045801526, 0.605...</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<h2 id=\"Section_5\">  How to submit </h2>\n\n<p>Once you complete your notebook you will have to share it. You can download the notebook by navigating to \"File\" and clicking on \"Download\" button.\n\n<p>This will save the (.ipynb) file on your computer. Once saved, you can upload this file in the \"My Submission\" tab, of the \"Peer-graded Assignment\" section.  \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>About the Authors:</h2> \n\n<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n\n### Other Contributors\n\n[Svitlana Kramar](https://www.linkedin.com/in/svitlana-kramar/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0232ENSkillsNetwork30654641-2022-01-01)\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## Change Log\n\n| Date (YYYY-MM-DD) | Version | Changed By    | Change Description          |\n| ----------------- | ------- | ------------- | --------------------------- |\n| 2023-04-10        | 2.1     | Anita Verma  | Removed \"RISK_MM\" and updated Q14 and Q15 |\n| 2022-06-22        | 2.0     | Svitlana K.   | Deleted GridSearch and Mock |\n\n\n## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n",
      "metadata": {}
    }
  ]
}
