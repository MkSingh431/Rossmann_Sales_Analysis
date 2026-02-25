# Store Sales Analysis (Rossmann / Store Data)

Project for exploring store sales data, training forecasting models, and running exploratory notebooks and a small app.

## Project structure
- `app.py` - main application entry (small demo / analysis runner).
- `train.csv`, `store.csv` - core datasets used for modeling and analysis.
- `rossman.csv`, `rossman.ipynb`, `rossmann.ipynb` - alternative dataset and notebooks.
- `requirements.txt` - Python dependencies for this project.

See the repository root for all files.

## Overview
This repository contains preprocessing, exploratory analysis, and modeling artifacts for a store-sales forecasting task (Rossmann-style dataset). It includes Jupyter notebooks for interactive exploration and an `app.py` script for quick demos.

## Requirements
- Python 3.8+ recommended
- A Conda environment `data_scientist` is used in this workspace (optional but recommended)

Install dependencies:

```bash
conda activate data_scientist
pip install -r requirements.txt
```

If you prefer venv:

```bash
python -m venv .venv
source .venv/Scripts/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Datasets
- `train.csv` — primary training data (historical sales per store/day).
- `store.csv` — store meta-data (store type, assortment, competition info).
- `rossman.csv` — alternate or combined dataset (if present).

Place any additional CSVs in the project root or point your notebook to the appropriate path.

## Quick Start

1. Activate environment and install dependencies (see Requirements).
2. Run the notebooks for exploration:

```bash
jupyter notebook
# or
jupyter lab
```

3. Run the demo app (if `app.py` is present and runnable):

```bash
# Example: run the script directly
python app.py

# If it's a Streamlit app (check header); to run Streamlit:
streamlit run app.py
```

Adjust the command depending on the app type; inspect `app.py` for details.

## Notebooks
- `rossman.ipynb` / `rossmann.ipynb` — exploratory analysis and experiments.

Open them with Jupyter to explore preprocessing, feature engineering and model training steps.

## Reproducing experiments / training
1. Ensure dependencies are installed.
2. Open the main notebook used for training (look for `train.csv` usage).
3. Follow notebook cells sequentially and re-run training/evaluation cells.

For script-based training (if present), run:

```bash
python train.py
```

(If `train.py` is not present, use the provided notebooks to run training.)

## Notes and tips
- Keep datasets in the repository root or update notebook script paths.
- If you encounter `ModuleNotFoundError`, ensure the active Python interpreter matches the environment where `requirements.txt` was installed.
- If datasets are large, consider using a sample subset for quick iteration.

## Contact / Next steps
If you want, I can:
- Run the notebooks and produce summary outputs
- Add a small `requirements-dev.txt` or environment YAML
- Convert a main notebook into a reproducible script

## Author
[Linkedln](https://www.linkedin.com/in/motilal-das-42b4a9254)\
[GitHub](https://github.com/MkSingh431)

