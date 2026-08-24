# 🐟 Aquaculture & Livestock Disease Risk Classification

A Streamlit web app that predicts disease risk level (Low / Medium / High) for aquaculture and livestock farms based on farm details, water quality, feed, environmental factors, and disease indicators.

## Project Files

| File | Description |
|---|---|
| `app.py` | Streamlit application — collects farm input and displays predictions |
| `aquaculture_livestock_best_model.pkl` | Trained `sklearn.Pipeline` (preprocessing + `DecisionTreeClassifier`) |
| `scaler (4).pkl` | Standalone scaler (not required — scaling is already built into the model pipeline) |
| `aquaculture_livestock_disease_feed_optimization_dataset.csv` | Training dataset |
| `requirements.txt` | Python package dependencies |

## Requirements

- **Python 3.11** (the model was trained with `scikit-learn==1.6.1`, which does not have prebuilt wheels for newer Python versions such as 3.14 — use Python 3.11 to avoid build errors)

## Setup — Run Locally

```bash
# 1. Create a virtual environment with Python 3.11
py -3.11 -m venv venv

# 2. Activate it
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app will open automatically in your browser, or print a local URL (e.g. `http://localhost:8501`) to open manually.

## How It Works

1. Enter farm details in the sidebar and main form (sector, species, water quality, feed, environmental factors, disease indicators).
2. Click **🔍 Predict Disease Risk**.
3. The app feeds your inputs into the trained pipeline, which:
   - Imputes missing values
   - Scales numeric features (`StandardScaler`)
   - One-hot encodes categorical features
   - Predicts the disease risk level using a `DecisionTreeClassifier`
4. The predicted risk level and class probabilities are displayed.

## Model Details

- **Type:** `sklearn.pipeline.Pipeline`
- **Preprocessing:** `ColumnTransformer` with median imputation + standard scaling (numeric columns) and most-frequent imputation + one-hot encoding (categorical columns)
- **Classifier:** `DecisionTreeClassifier(class_weight='balanced', random_state=42)`
- **scikit-learn version:** 1.6.1 (must match to load the pickle correctly)

## Deploying for a Permanent Link

To get a permanent public URL (instead of a local-only link):

1. Push this project to a public GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, select the repo/branch, and set the main file to `app.py`.
4. Deploy — you'll get a link like `https://your-app-name.streamlit.app`.

Streamlit Cloud uses Python 3.11/3.12 by default, so `scikit-learn==1.6.1` in `requirements.txt` will install without issues.

## Troubleshooting

- **Model fails to load / `AttributeError`:** scikit-learn version mismatch — make sure `requirements.txt` pins `scikit-learn==1.6.1` and you're using Python 3.11.
- **`pip install` tries to compile scikit-learn from source:** you're likely on a Python version without a prebuilt wheel (e.g. 3.14) — switch to Python 3.11.
