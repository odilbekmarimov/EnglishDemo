from extract import extract_users
from transform import transform_users
from load import load_users

RAW_PATH = "data/raw/users_raw.csv"
OUTPUT_PATH = "data/processed/users_clean.csv"

def run_etl():
    df_raw = extract_users(RAW_PATH)
    df_transformed = transform_users(df_raw)
    load_users(df_transformed, OUTPUT_PATH)

if __name__ == "__main__":
    run_etl()
