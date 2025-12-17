import os
import pandas as pd

def load_users(df: pd.DataFrame, output_path: str):
    """
    Loads transformed data into processed layer.
    """
    print("Loading data...")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Data successfully written to {output_path}")

