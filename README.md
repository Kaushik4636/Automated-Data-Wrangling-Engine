# Automated Data Wrangling Engine

## Overview

**Automated Data Wrangling Engine** is a **modular Python library** for automating common data cleaning tasks in real-world datasets. It helps with:

* Handling missing values (numeric and categorical)
* Detecting and capping outliers
* Transforming skewed numeric features

The library is built in a **pipeline style**, allowing **end-to-end preprocessing in a single call**, and is reusable across different datasets.

---

## Folder Structure

```
data_wrangling_engine/
│
├── src/                     # Python modules
│   ├── __init__.py
│   ├── missing_handler.py
│   ├── outlier_handler.py
│   ├── skew_handler.py
│   └── pipeline.py
│
├── data/                    # Sample dataset for testing
│   └── sample.csv
│
├── notebooks/               # Jupyter notebooks for experimentation
│   └── testing.ipynb
│
├── requirements.txt         # Dependencies
└── README.md
```

---

## Features

### 1. Missing Value Handling

* **Numeric columns:** Replace missing values with mean or median.
* **Categorical columns:** Replace missing values with mode.

### 2. Outlier Handling

* Automatically detect outliers using **IQR**.
* Cap extreme values instead of removing them.

### 3. Skew Handling

* Detect skewed numeric columns.
* Apply **log** or **square root transformations**.

### 4. Full Pipeline

* Combine all three steps into a single reusable pipeline.

**Example Usage:**

```python
from src.pipeline import DataWranglingPipeline
import pandas as pd

# Load your dataset
df = pd.read_csv('data/sample.csv')

# Initialize and run the pipeline
pipeline = DataWranglingPipeline()
df_clean = pipeline.fit_transform(df)

print(df_clean.head())
```

---

## How to Run

1. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Jupyter notebook for testing:**

```bash
jupyter notebook notebooks/testing.ipynb
```

---

## Sample Output

**Before Cleaning:**

| age | income | score |
| --- | ------ | ----- |
| 25  | 50000  | 200   |
| 30  | NaN    | 210   |
| 120 | 70000  | 3000  |

**After Cleaning (Final Pipeline):**

| age  | income | score |
| ---- | ------ | ----- |
| 3.25 | 10.81  | 5.30  |
| 3.43 | 10.92  | 5.35  |
| 3.84 | 11.15  | 7.14  |

> Numeric columns are scaled and skewed appropriately.

---

## Notes

* Designed for **real-world messy datasets**.
* **Modular design** allows easy extension (add new handlers or transformations).
* Ready for use in **ML pipelines** or general **data preprocessing** for modeling.
