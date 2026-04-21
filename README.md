````md
# World-Health-Population
---

## Repository Outline
```text
1. README.md  
   Overview and general explanation of the project

2. modeling.ipynb  
   Data exploration, preprocessing, and model training process

3. inference.ipynb  
   Notebook for making predictions (inference)

4. url.txt  
   Contains deployment links or related project references

5. deployment/
   ├── Dockerfile            Container configuration file
   ├── requirements.txt     Project dependencies
   └── src/
       ├── streamlit_app.py Main Streamlit application
       ├── eda.py           Exploratory Data Analysis (EDA) module
       └── prediction.py    Prediction module
````

## Problem Background

In recent years, a country's health condition has become an important indicator in measuring the overall well-being of its population. One of the most commonly used indicators is **life expectancy**, which is influenced by various factors such as healthcare quality, access to medical services, sanitation, and demographic conditions.

However, not all countries share the same level of health conditions. These differences are influenced by multiple indicators such as fertility rates, mortality rates, healthcare facilities, and economic conditions. Therefore, a data-driven approach is needed to better understand the factors affecting a country's health status.

## Objectives

* Develop a *machine learning* model to classify a country's **health status**.
* Identify relationships between health indicators and life expectancy.
* Compare the performance of multiple models to determine the best one.
* Build a model that can be used for predicting new data.

## Project Output

* Global health data visualizations
* Machine learning model for health status prediction
* Interactive Streamlit dashboard
* Insights from health indicator data
* Real-time prediction feature

## Data

The dataset contains information about countries, years, regions, income groups, health indicators, and population data from various countries. The original dataset consists of 6 columns and 3,174,996 rows.

Columns included in the dataset:

* `country_name`: country name
* `indicator_name`: type of indicator
* `value`: indicator value
* `year`: year
* `region`: region
* `income_group`: economic category

The dataset is then transformed and extracted based on selected indicators such as:

* Population growth
* Mortality rate
* Fertility rate
* Healthcare resources (physicians, hospital beds, etc.)
* Sanitation & water access
* Nutrition indicators
* Life Expectancy

## Method

### 1. Data Preprocessing

* Handling missing values (*SimpleImputer*)
* Handling outliers
* Feature frequency transformation
* Feature encoding (*OneHotEncoder* & *OrdinalEncoder*)
* Feature scaling (*MinMaxScaler*)

### 2. Modeling

* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Decision Tree
* Random Forest
* Gradient Boosting

### 3. Model Selection

* Cross Validation
* Hyperparameter tuning (*GridSearchCV*)

### 4. Evaluation

* Precision Score
* ROC-AUC Score

## Tech Stack

### Programming Language

* Python

### Libraries

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* phik

### Tools

* VSCode
* Streamlit
* GitHub

## License

This project is open-source and can be used for learning purposes.

## References

* [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Seaborn Documentation](https://seaborn.pydata.org/)
* [Streamlit Documentation](https://docs.streamlit.io/)
* [World Bank – Global Health Insights](https://www.worldbank.org/en/topic/health)
* [Our World in Data – Life Expectancy](https://ourworldindata.org/life-expectancy)
* [WHO – Health Equity](https://www.who.int/health-topics/health-equity)

```
```
