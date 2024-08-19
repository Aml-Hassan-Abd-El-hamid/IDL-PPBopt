# config.py
import os

# Path to the package code location
PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))

# Path to the default model
DEFAULT_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'saved_models', 'model_ppb_3922_Tue_Dec_22_22-23-22_2020_54.pt')
