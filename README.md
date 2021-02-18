# EDA-Project

## Content
- EDA.ipynb : Exploratory Data Analysis
- housePredict.py
- data-params.pkl

The EDA.ipynb file contains an Exploratory Data Analysis about a data set describing features about houses in King County, USA. In this document, we will step by step discover several variables which can possibly determine the price of a certain house. The file includes a lot of graphics, which can illustrate the extent to which a certain factor influences our target value. At the end, we'll finally do a linear regression modell which will help us to make predictions about prices of a house with given features.

The housePredict.py Python file is designed to do this prediction. We'll use the coefficients our model in the previously described file has determined. Given these coefficient, the file will ask the user to insert concrete values for some features we found relevant. Be aware that the data has to be inserted quite specifically, e.g. some features only take float values. Also be aware of the fact that this current version is not yet able to make predictions for all values you might insert, so try not to focus on rather unlikely values.

Finally data_params.pkl is a pickle-file in which all the coefficients for the prediction model are saved.


