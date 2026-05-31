import pandas as pd
import os

def load_data(file_path:str) -> pd.DataFrame:
    """
    Loads CSV into a pandas DataFrame.

    Args: file_path (str): Path to the CSV file.

    Returns:
        Pd.DataFrame: Loaded Dataset.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found {file_path}")
    return pd.read_csv(file_path)