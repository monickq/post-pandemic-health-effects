# Post-Pandemic Effects – Data Analysis

This repository contains Jupyter notebook and a Python script for analyzing the **post-pandemic effects** on various aspects such as mental health, physical well-being, and work arrangements.

## Files

- `predict_depression.py` - Python script containing RandomForest model for predicting depression.
- `data_analysis.ipynb` – Core data analysis notebook (data cleaning, visualization, descriptive statistics).
- `post_pandemic_effects2025.ipynb` – Focused analysis on the effects observed in 2025 (source: https://www.kaggle.com/datasets/kshitijsaini121/remote-work-of-health-impact-survey-june-2025/data)

## Requirements

Make sure you have installed:

- Python 3.8+
- Jupyter Notebook / Jupyter Lab
- Required libraries (install via pip):

```bash
pip install -r requirements.txt
```

## Running the Notebooks

### Option 1 – Open in Jupyter Lab/Notebook
Start Jupyter and open the notebooks interactively:
```bash
jupyter lab
```
or
```bash
jupyter notebook
```

### Option 2 – Run from Command Line
To execute a notebook and save the output:

```bash
jupyter nbconvert --to notebook --execute data_analysis.ipynb --output executed_data_analysis.ipynb
jupyter nbconvert --to notebook --execute post_pandemic_effects2025.ipynb --output executed_post_pandemic_effects.ipynb
```

### Option 3 – Run Both Notebooks Automatically
You can also create a simple Python script (`run_all.py`) to execute both:

```python
import os

notebooks = ["data_analysis.ipynb", "post_pandemic_effects2025.ipynb"]

for nb in notebooks:
    os.system(f'jupyter nbconvert --to notebook --execute {nb} --output executed_{nb}')
```

Run it with:
```bash
python run_all.py
```

---

## Notes
- Make sure your working directory contains both notebooks before running the commands.
- Output notebooks will be saved as `executed_*.ipynb`, preserving the original files.

# predict_depression.py
What the script does:
1. Loads the dataset from post_pandemic_remote_work_health_impact_2025.csv.
2. Transforms columns:
  Burnout_Level → maps Low = 1, Medium = 2, High = 3
  Mental_Health_Status → fills missing values with "none"
  Creates a binary variable Depression (1 = has depression, 0 = no depression)
  Inverts Work_Life_Balance_Score so that 1 = best, 5 = worst.

3. Trains a Random Forest model to predict depression based on:
- Social_Isolation_Score
- Burnout_Level
- Work_Life_Balance_Score_inv

4. Evaluates the model – prints overall accuracy and a classification report.

5. Predicts new data – for example, a person with:

Social_Isolation_Score = 1

Burnout_Level = 3

Work_Life_Balance_Score_inv = 4

## Output:

Accuracy (0.67)

classification_report (precision, recall, F1-score per class)

Text interpretation of the prediction result, e.g.:

Score: 1 -> Is at risk of depression

Score: 0 -> Probably won't experience depression
