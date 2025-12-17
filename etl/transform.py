import pandas as pd

def transform_users(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms user data:
    - Removes inactive users
    - Fixes missing emails
    - Converts signup_date to datetime
    """
    print("Transforming data...")

    df = df[df["is_active"] == "yes"]

    df["email"] = df["email"].fillna("unknown@email.com")

    df["signup_date"] = pd.to_datetime(
        df["signup_date"],
        errors="coerce"
    )

    df = df.dropna(subset=["signup_date"])

    return df
