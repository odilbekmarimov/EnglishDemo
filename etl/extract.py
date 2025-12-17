import pandas as pd

def extract_users(file_path: str) -> pd.DataFrame:
    """
    Extracts raw user data from CSV file.
    """
    print("Extracting data...")
    df = pd.read_csv(file_path)
    return df
