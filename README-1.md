# ApexPlanet Data Analytics

Data analytics internship projects at **ApexPlanet Software Pvt. Ltd.**

## Task 1: Foundational Setup & Exploratory Data Analysis (EDA)

**Objective:** Set up the environment, clean the data and perform exploratory analysis.
**Dataset:** Superstore Sales

### Project structure
```
apexplanet-data-analytics/
├── data/          # raw + cleaned datasets
├── notebooks/     # Jupyter notebooks (EDA)
├── scripts/       # reusable Python scripts
├── reports/       # figures and reports
├── dashboards/    # dashboards (later tasks)
└── README.md
```

### Setup
```bash
pip install -r requirements.txt
```
Download the *Sample - Superstore* dataset (CSV) and place it at `data/Sample - Superstore.csv`.

### What was done
1. **Environment setup:** Anaconda / Python, Jupyter Notebook, pandas, numpy, matplotlib, seaborn, plotly, sqlalchemy.
2. **Data cleaning:** missing values handled, duplicates removed, dates/categories fixed, outliers handled with IQR, cleaned dataset saved.
3. **EDA:** `describe()`/`info()`, histograms & boxplots, bar charts, correlation heatmap, monthly sales trend line chart, 5 key insights.

### Run
```bash
jupyter notebook notebooks/01_data_cleaning_and_eda.ipynb
# or just the cleaning step:
python scripts/clean_data.py
```

### Key insights
_Add your 5 findings here after running the notebook._

### Tech stack
Python · pandas · numpy · matplotlib · seaborn · plotly · sqlalchemy · Jupyter

#DataAnalytics #Python
