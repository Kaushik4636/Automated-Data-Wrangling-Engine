# Automated Data Wrangling Engine

## Overview
This project is a **modular Python library** for automating common data cleaning tasks in real-world datasets. It handles:

- Missing values (numeric and categorical)
- Outlier detection and capping
- Skewed numeric feature transformation

The project is built in a **pipeline style**, allowing end-to-end preprocessing in one call, and is designed to be reusable for any dataset.

---

## Folder Structure


data_wrangling_engine/
│
├── src/ # Python modules
│ ├── init.py
│ ├── missing_handler.py
│ ├── outlier_handler.py
│ ├── skew_handler.py
│ └── pipeline.py
├── data/ # Sample dataset for testing
│ └── sample.csv
├── notebooks/ # Jupyter notebooks for experimentation
│ └── testing.ipynb
├── requirements.txt
└── README.md


---

## Features

1. **Missing Value Handling**
   - Numeric columns: replace with mean or median
   - Categorical columns: replace with mode

2. **Outlier Handling**
   - Automatically detect outliers using IQR
   - Cap extreme values instead of removing

3. **Skew Handling**
   - Detect skewed numeric columns
   - Apply log or square root transformations

4. **Full Pipeline**
   - Combine all three steps in one reusable pipeline
   - Example usage:
   ```python
   from pipeline import DataWranglingPipeline

   pipeline = DataWranglingPipeline()
   df_clean = pipeline.fit_transform(df)
How to Run
Create virtual environment:
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
Install dependencies:
pip install -r requirements.txt
Run notebook for testing:
jupyter notebook notebooks/testing.ipynb
Sample Output

Before Cleaning:

age	income	score
25	50000	200
30	NaN	210
120	70000	3000

After Cleaning (Final Pipeline):

age	income	score
3.25	10.81	5.30
3.43	10.92	5.35
3.84	11.15	7.14

Numeric columns are scaled and skewed appropriately.

Notes
Designed for real-world messy datasets
Modular design allows easy extension (add new handlers, transformations)
Ready for use in ML pipelines or data preprocessing for modeling
