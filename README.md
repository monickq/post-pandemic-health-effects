# Post-Pandemic Effects – Data Analysis

This repository contains Jupyter notebooks for analyzing the **post-pandemic effects** on various aspects such as mental health, physical well-being, and work arrangements.

## Files

- `data_analysis.ipynb` – Core data analysis notebook (data cleaning, visualization, descriptive statistics).
- `post_pandemic_effects2025.ipynb` – Focused analysis on the effects observed in 2025.

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
