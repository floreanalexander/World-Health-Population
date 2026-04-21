# World-Health-Population
---
## Repository Outline
```
1. README.md  
   Penjelasan gambaran umum project
2. modeling.ipynb  
   Proses eksplorasi data, preprocessing, dan training model
3. inference.ipynb  
   Proses untuk melakukan prediksi (inference)
4. url.txt  
   Berisi link deployment atau referensi terkait project
5. deployment/
   ├── Dockerfile            berisi konfigurasi container
   ├── requirements.txt      berisi dependency project
   └── src/
       ├── streamlit_app.py  berisi Main app Streamlit
       ├── eda.py            berisi  Modul analisis data (EDA)
       └── prediction.py     berisi  Modul prediksi
```

## Problem Background
Dalam beberapa tahun terakhir, kondisi kesehatan suatu negara menjadi indikator penting dalam menilai tingkat kesejahteraan masyarakat. Salah satu indikator utama yang sering digunakan adalah **life expectancy (harapan hidup)**, yang dipengaruhi oleh berbagai faktor seperti kondisi kesehatan, akses layanan medis, sanitasi, dan faktor demografis.

Namun, tidak semua negara memiliki tingkat kesehatan yang sama. Perbedaan ini dipengaruhi oleh berbagai indikator seperti tingkat fertilitas, angka kematian, fasilitas kesehatan, hingga kondisi ekonomi. Oleh karena itu, diperlukan pendekatan berbasis data untuk memahami faktor-faktor yang memengaruhi kondisi kesehatan suatu negara.

## Objectives
- Mengembangkan model *machine learning* untuk mengklasifikasikan **status kesehatan suatu negara**.
- Mengidentifikasi hubungan antara indikator kesehatan dan life expectancy.
- Membandingkan performa beberapa model untuk mendapatkan model terbaik.
- Menghasilkan model yang dapat digunakan untuk prediksi data baru.

## Project Output
- Visualisasi data kesehatan global
- Model machine learning untuk prediksi status kesehatan
- Dashboard interaktif berbasis Streamlit
- Insight dari data indikator kesehatan
- Fitur prediksi secara real-time

## Data
Dataset yang digunakan berisi berbagai negara, tahun, wilayah, kelompok ekonomi, indikator kesehatan dan populasi dari berbagai negara. Dataset asli memiliki 6 kolom dengan 3174996 data. Berikut kolom yang ada di dalam dataset:
- `country_name`: negara
- `indicator_name`: jenis indikator
- `value`: nilai indikator
- `year`: tahun
- `region`: wilayah
- `income_group`: kategori ekonomi

Kemudian dataset akan diextract lagi berdasarkan indicator_name, seperti:
- `Population growth`
- `Mortality rate`
- `Fertility rate`
- `Healthcare resources (physicians, hospital beds, dll)`
- `Sanitation & water access`
- `Nutrition indicators`
- `Life Expectancy`

## Method
1. Data Preprocessing
- Handling missing values (SimpleImputer)
- Handling Outlier
- Feature Frequency
- Feature Encoding (OneHotEncoder & OrdinalEncoder)
- Feature Scaling (MinMaxScaler)

2. Modeling
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- Gradient Boosting

3. Seleksi Model
- Cross Validation
- Hyperparameter tuning (GridSearchCV)

4. Evaluasi
- Precision Score
- ROC-AUC Score

## Stacks
- Programming Language: Python
- Libraries:
a. pandas
b. numpy
c. matplotlib
d. seaborn
e. scikit-learn
f. phik
- Tools:
a. VSCode
b. Streamlit
c. GitHub

## License
Project ini bersifat open-source dan dapat digunakan untuk pembelajaran.

## Reference
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Global Health Inequality – World Bank Insights](https://www.worldbank.org/en/topic/health)
- [Our World in Data – Life Expectancy](https://ourworldindata.org/life-expectancy)
- [WHO – Health Equity](https://www.who.int/health-topics/health-equity)
