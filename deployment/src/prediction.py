# Import libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np



# Load all files
with open('./src/best_model.pkl', 'rb') as file_best_model:
  best_model = pickle.load(file_best_model)

# frequency encoding 
with open('./src/country_name_freq.pkl', 'rb') as file_country_name_freq:
  freq_country_name = pickle.load(file_country_name_freq)

# preprocessing objects
with open('./src/median_imputer.pkl', 'rb') as file_median_imputer:
  median_imputer = pickle.load(file_median_imputer)



def run():
    st.title("Country-Based Health Risk Assessment")
    st.subheader("Predict health status using country-level indicators")
  # Pembuatan Form
  # key itu hanya penamaan form aja jadi bebas
  # inputan angka bisa dibatasi dengan min max values, dan bisa set defaultnya juga
    with st.form(key='form_health_population'):
        st.write('## **Country Profile**')
        country_name = st.text_input('Country Name', value='--input country name--')
        year = st.number_input('Year', min_value=1960, max_value=2026, value=2026, step=1, help='You can only input from 1960-2026.')
        region = st.selectbox('Region', ('Europe & Central Asia', 'Sub-Saharan Africa', 'Latin America & Caribbean', 'East Asia & Pacific', 'Middle East & North Africa', 'South Asia', 'North America'), index=0)
        income_group = st.selectbox('Income Group', ('Low income', 'Lower middle income', 'Upper middle income', 'High income'), index=0)        
        
        st.markdown('---')

        st.write('## **Demographic**')
        age_dependency_of_working_age = st.number_input('Age Dependency Ratio (% of working-age population)', max_value=200, value=50, step=1, help='You can only input until 200.')
        population_ages_0_14 = st.slider('Population ages 0-14 (% of total population)', 1,100,50, help='in percentage(%).')
        population_ages_65_above = st.slider('Population ages 65 and above (% of total population)', 1,100,50, help='in percentage(%).')
        population_growth = st.number_input('Population growth (annual %)', max_value=100, value=50, step=1, help='You can only input 100.')
        urban_population = st.slider('Urban population (% of total population)', 1,100,50, help='in percentage(%).')
        
        st.markdown('---')

        st.write('## **Mortality**')
        mortality_rate_infant = st.number_input('Mortality Rate (Infant)', min_value=1, max_value=1000, value=50, step=1, help='You can only input from 1 until 1000.')
        mortality_rate_under5 = st.number_input('Mortality Rate (Under-5)', min_value=1, max_value=1000, value=50, step=1, help='You can only input from 1 until 1000.')
        death_rate_crude = st.number_input('Death Rate, crude (per 1,000 people)', min_value=1, max_value=1000, value=10, step=1, help='You can only input from 1 until 1000.')
        
        st.markdown('---')

        st.write('## **Healthcare System**')
        current_health_expenditure = st.number_input('Current health expenditure per capita (current US$)', min_value=1, value=250, step=1)
        hospital_beds = st.number_input('Hospital beds (per 1,000 people)', max_value=1000, value=10, step=1, help='You can only input until 1000.')
        nurses_and_midwives = st.number_input('Nurses and midwives (per 1,000 people)', max_value=1000, value=10, step=1, help='You can only input until 1000.')
        physicians = st.number_input('Physicians (per 1,000 people)', max_value=1000, value=10, step=1, help='You can only input until 1000.')
        
        st.markdown('---')

        st.write('## **Sanitation**')
        people_using_safely_drinking_water = st.slider('People using safely managed drinking water services (% of population)', 1,100,50, help='in percentage(%).')
        people_using_safely_sanitation = st.slider('People using safely managed sanitation services (% of population)', 1,100,50, help='in percentage(%).')
        people_with_basic_handwashing_facilities = st.slider('People with basic handwashing facilities including soap and water (% of population)', 1,100,50, help='in percentage(%).')
        
        st.markdown('---')

        st.write('## **Nutrition**')
        prevalence_of_stunting = st.slider('Prevalence of stunting, height for age (% of children under 5)', 1,100,50, help='in percentage(%).')
        prevalence_of_undernourishment = st.slider('Prevalence of undernourishment (% of population)', 1,100,50, help='in percentage(%).')

        st.markdown('---')

        st.write('## **Fertility**')
        adolescent_fertility_rate = st.number_input('Adolescent Fertility Rate', max_value=1000, value=50, step=1, help='You can only input until 1000.')
        fertility_rate = st.number_input('Fertility rate', min_value=1, max_value=10, value=3, step=1, help='You can only input from 1 until 10.')
        
        st.markdown('---')

        submitted = st.form_submit_button('Predict')


    # Create a new data
    # Use all columns not just the results of feature selection
    data_inf = {
        'country_name': country_name,
        'year': year,
        'region': region, 
        'income_group': income_group,
        'adolescent_fertility_rate_births_per_1000_women_ages_15-19': adolescent_fertility_rate,
        'age_dependency_ratio_pct_of_working-age_population':age_dependency_of_working_age,
        
        'current_health_expenditure_per_capita_current_us$':current_health_expenditure,
        'death_rate_crude_per_1000_people':death_rate_crude,
        'fertility_rate_total_births_per_woman':fertility_rate,
        'hospital_beds_per_1000_people':hospital_beds,
        'mortality_rate_infant_per_1000_live_births':mortality_rate_infant,
        'mortality_rate_under-5_per_1000':mortality_rate_under5,
        'nurses_and_midwives_per_1000_people':nurses_and_midwives,
        'people_using_safely_managed_drinking_water_services_pct_of_population':people_using_safely_drinking_water,
        'people_using_safely_managed_sanitation_services_pct_of_population':people_using_safely_sanitation,
        'people_with_basic_handwashing_facilities_including_soap_and_water_pct_of_population':people_with_basic_handwashing_facilities,
        'physicians_per_1000_people':physicians,
        'population_ages_0-14_pct_of_total_population':population_ages_0_14,
        'population_ages_65_and_above_pct_of_total_population':population_ages_65_above,
        'population_growth_annual_pct':population_growth,
        'prevalence_of_stunting_height_for_age_pct_of_children_under_5':prevalence_of_stunting,
        'prevalence_of_undernourishment_pct_of_population':prevalence_of_undernourishment,
        'urban_population_pct_of_total_population':urban_population
    }
    data_inf = pd.DataFrame([data_inf])
    #st.dataframe(data_inf)

    if submitted: 
        def preprocess_input(df):
            df = df.copy()

            # 🔹 1. Frequency Encoding
            df['country_name_freq'] = df['country_name'].map(freq_country_name).fillna(0)
            df.drop(columns=['country_name'], inplace=True)

            # 🔹 2. Missing Value (median dari training)
            num_cols_impute = [
                'adolescent_fertility_rate_births_per_1000_women_ages_15-19',
                'age_dependency_ratio_pct_of_working-age_population',
                'death_rate_crude_per_1000_people',
                'fertility_rate_total_births_per_woman',
                'mortality_rate_infant_per_1000_live_births',
                'mortality_rate_under-5_per_1000',
                'population_ages_0-14_pct_of_total_population',
                'population_ages_65_and_above_pct_of_total_population',
                'population_growth_annual_pct',
                'urban_population_pct_of_total_population'
            ]

            df[num_cols_impute] = median_imputer.transform(df[num_cols_impute])

            # Outlier Handling 
            # 1. Normal
            for col in [    
                'year', 'age_dependency_ratio_pct_of_working-age_population',
                'fertility_rate_total_births_per_woman', 'population_ages_0-14_pct_of_total_population',
                'urban_population_pct_of_total_population'
            ]:
                avg = df[col].mean()
                std = df[col].std()
                
                lower =  avg - 3 * std
                upper = avg + 3 * std
                
                df[col] = df[col].clip(lower, upper)

            # 2. Skew
            for col in [    
                'adolescent_fertility_rate_births_per_1000_women_ages_15-19'
            ]:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR
                
                df[col] = df[col].clip(lower, upper)

            # 3. Extreme Skew
            for col in [    'death_rate_crude_per_1000_people', 'mortality_rate_infant_per_1000_live_births', 
                            'mortality_rate_under-5_per_1000', 'population_ages_65_and_above_pct_of_total_population',
                            'population_growth_annual_pct'
            ]:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                
                lower = Q1 - 3 * IQR
                upper = Q3 + 3 * IQR
                
                df[col] = df[col].clip(lower, upper)

            return df

        # Predict using Linear Regression
        data_inf_final = preprocess_input(data_inf)
        data_inf_final

        y_pred = best_model.predict(data_inf_final)
        y_proba = best_model.predict_proba(data_inf_final)

        prob_selected = y_proba[0][y_pred[0]]

        st.write('## Prediction: ', str(int(y_pred)))

        print(f'Prediction: {y_pred[0]}')
        print(f'Probability: {prob_selected:.0%}')

        if y_pred[0] == 1:
            st.success('✅ Health Status: High.')
            st.success('Based on the model prediction, the health condition is within a healthy range.')
        else:
            st.error('⚠️ Health Status: Low.')
            st.error('Based on the model prediction, the health condition is classified as below optimal and may require further monitoring.')


if __name__ == '__main__':
    run()