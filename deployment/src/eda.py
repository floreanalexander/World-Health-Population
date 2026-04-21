import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import plotly.express as px


def run():
    # Membuat Header
    st.title('World Health and Population Analysis Application')

    # Membuat Sub Header
    st.subheader('This page presents an Exploratory Data Analysis (EDA) of global health and population data to understand key patterns, trends, and relationships across countries.')

    # Menampilkan teks
    # **teks** = bold
    # *teks* = italic
    st.write('Made by **Florean Alexander**')

    # Menambah Gambar
    data = mpimg.imread('./src/health-population.jpg')
    st.image(data, caption='World Health Population')

    # Menampilkan dataframe
    chunks = pd.read_csv('./src/world_health_population.csv', chunksize=10000)

    processed = []

    for chunk in chunks:
        # preprocessing lu di sini
        chunk = chunk.dropna()  # contoh
        
        processed.append(chunk)

    df_final = pd.concat(processed)
    st.dataframe(df_final.head(5000))
    


    # PAGE EDA
    df_clean = df_final.copy()
    df_clean['value'] = df_clean['value'].replace(1, np.nan)

    # 1. Menampilkan histogram demografi
    st.write('## **Demographic**')
    
    growth = df_clean[df_clean['indicator_name'] == 'Population growth (annual %)']['value']
    df_demo = df_clean[df_clean['indicator_name'].isin([
        'Population ages 0-14 (% of total population)',
        'Urban population (% of total population)',
        'Population ages 65 and above (% of total population)',
        'Age dependency ratio (% of working-age population)'
    ])]

    fig1, axes = plt.subplots(1, 2, figsize=(15,5))

    # kiri (growth)
    axes[0].hist(growth, bins=50)
    axes[0].set_title('Population Growth Trends')

    # kanan (skala besar)
    sns.histplot(data=df_demo, x='value', hue='indicator_name', bins=50, alpha=0.5, ax=axes[1])
    axes[1].set_title('Demographic Distribution')

    st.pyplot(fig1)


    # 2. Menampilkan histogram Angka Kematian
    st.write('## **Mortality**')
    
    df_mort = df_clean[df_clean['indicator_name'].isin([
        'Mortality rate, infant (per 1,000 live births)',
        'Mortality rate, under-5 (per 1,000)',
        'Death rate, crude (per 1,000 people)'
    ])]
    fig2 = plt.figure(figsize=(15,5))
    sns.histplot(data=df_mort, x='value', hue='indicator_name', bins=50, alpha=0.5, kde=True)
    plt.title('Mortality Indicators Distribution')
    st.pyplot(fig2)


    # 3. Menampilkan histogram Sistem Kesehatan
    st.write('## **Healthcare System**')
    cur_health_exp = df_clean[df_clean['indicator_name'] == 'Current health expenditure per capita (current US$)']['value']
    df_system = df_clean[df_clean['indicator_name'].isin([
        'Physicians (per 1,000 people)',
        'Nurses and midwives (per 1,000 people)',
        'Hospital beds (per 1,000 people)'
    ])]

    fig3, axes = plt.subplots(1, 2, figsize=(15,5))

    # kiri (cur_health_exp)
    axes[0].hist(cur_health_exp, bins=50)
    axes[0].set_title('Health Expenditure per Capita (USD)')

    # kanan (skala besar)
    sns.histplot(data=df_system, x='value', hue='indicator_name', bins=50, alpha=0.5, ax=axes[1])
    axes[1].set_title('Healthcare Capacity Distribution')

    st.pyplot(fig3)


    # 4. Menampilkan histogram Sanitasi
    st.write('## **Sanitation**')
    df_san = df_clean[df_clean['indicator_name'].isin([
        'People using safely managed drinking water services (% of population)',
        'People using safely managed sanitation services (% of population)',
        'People with basic handwashing facilities including soap and water (% of population)'
    ])]
    fig4 = plt.figure(figsize=(15,5))
    sns.histplot(data=df_san, x='value', hue='indicator_name', bins=50, alpha=0.5)
    plt.title('Sanitation Access Distribution')
    st.pyplot(fig4)


    # 5. Menampilkan histogram Nutrisi
    st.write('## **Nutrition**')
    df_nut = df_clean[df_clean['indicator_name'].isin([
        'Prevalence of undernourishment (% of population)',
        'Prevalence of stunting, height for age (% of children under 5)'
    ])]
    fig5 = plt.figure(figsize=(15,5))
    sns.histplot(data=df_nut, x='value', hue='indicator_name', bins=50, alpha=0.5)
    plt.title('Nutrition Indicators Distribution')
    st.pyplot(fig5)


    # 6. Menampilkan histogram Reproduksi
    st.write('## **Fertility**')
    fert_rate = df_clean[df_clean['indicator_name'] == 'Fertility rate, total (births per woman)']['value']
    adole_fert_rate = df_clean[df_clean['indicator_name'] == 'Adolescent fertility rate (births per 1,000 women ages 15-19)']['value']

    fig6, axes = plt.subplots(1, 2, figsize=(15,5))
    axes[0].hist(fert_rate, bins=50)
    axes[0].set_title('Fertility Rate')

    axes[1].hist(adole_fert_rate, bins=50)
    axes[1].set_title('Adolescent Fertility Rate (Ages 15–19) per 1000')
    st.pyplot(fig6)


    # Menampilkan Histogram berdasarkan Input User
    df_le = df_clean[df_clean['indicator_name'] == 'Life expectancy at birth, total (years)']

    st.write("## **Life Expectancy Overview**")
    opsi = st.selectbox(
        "Choose the Category:",
        ["Country", "Region", "Income Group"]
    )

    if opsi == "Country":
        top_n = st.slider("Top N Countries", 3, 20, 5)

        data = (
            df_le.groupby('country_name')['value']
            .mean()
            .sort_values(ascending=False)
            .head(top_n)
        )

        title = f"Top {top_n} Life Expectancy by Country"
        xlabel = "Life Expectancy"
        ylabel = "Country"

    elif opsi == "Region":
        data = (
            df_le.groupby('region')['value']
            .mean()
            .sort_values(ascending=False)
        )

        title = "Life Expectancy based on Region"
        xlabel = "Life Expectancy"
        ylabel = "Region"

    elif opsi == "Income Group":
        data = df_le.groupby('income_group')['value'].mean()

        title = "Life Expectancy based on Income Group"
        xlabel = "Life Expectancy"
        ylabel = "Income Group"

    # plot
    fig = plt.figure(figsize=(15,5))
    sns.barplot(x=data.values, y=data.index, hue=data.values)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    st.pyplot(fig)
    

if __name__ == '__main__':
    run()