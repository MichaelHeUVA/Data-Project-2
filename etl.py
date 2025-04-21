import pandas as pd
import requests
import os


def extract_fear_greed():
    """
    Retrieves Fear & Greed Index from the alternative.me API.
    Converts timestamps to datetime and returns a DataFrame with:
    - 'date': Datetime version of UNIX timestamp
    - 'fear_greed_index': Integer sentiment score
    """
    url = "https://api.alternative.me/fng/?limit=0"
    response = requests.get(url)
    data = response.json().get("data", [])

    # Error Handling
    if not data:
        print("No sentiment data retrieved.")
        return pd.DataFrame()

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"].astype(int), unit="s")
    df["value"] = df["value"].astype(int)

    df = df.rename(columns={"value": "fear_greed_index", "timestamp": "date"})

    return df[["date", "fear_greed_index"]]


def load_price_data(filepath):
    """
    Loads a CSV file of cryptocurrency price data.
    Converts 'timestamp' column to datetime and renames it to 'date'
    """
    df = pd.read_csv(filepath)

    if "timestamp" in df.columns:
        df = df.rename(columns={"timestamp": "date"})

    df["date"] = pd.to_datetime(df["date"])
    return df


def transform_data(price_df, sentiment_df):
    """
    Transforms raw minute-level crypto data to daily:
    - Aggregates OHLCV values by day
    - Calculates daily percent change and volatility
    - Merges with daily sentiment scores
    - Adds lagged sentiment column for predictive testing
    """
    # Convert to daily datetime
    price_df["date"] = pd.to_datetime(price_df["date"]).dt.floor("d")

    # Aggregate OHLCV by day
    daily_crypto = (
        price_df.groupby("date")
        .agg(
            {
                "open": "first",
                "high": "max",
                "low": "min",
                "close": "last",
                "volume": "sum",
            }
        )
        .reset_index()
    )

    # Add % change and volatility
    daily_crypto["pct_change"] = daily_crypto["close"].pct_change() * 100
    daily_crypto["volatility"] = (
        daily_crypto["high"] - daily_crypto["low"]
    ) / daily_crypto["open"]

    # Merge with sentiment
    df = pd.merge(daily_crypto, sentiment_df, on="date", how="inner")

    # Error Handling
    if df.empty:
        print("No matching data on dates.")
        return df

    # Add lagged sentiment (yesterday’s sentiment) for predictive correlation
    df["lagged_sentiment"] = df["fear_greed_index"].shift(1)

    return df


def get_dataframe():
    try:
        if os.path.exists("data/processed_data.csv"):
            df = pd.read_csv("data/processed_data.csv")
            return df
        else:
            sentiment_df = extract_fear_greed()
            price_df = load_price_data("data/BTCUSDT.csv")
            transformed_df = transform_data(price_df, sentiment_df)
            transformed_df.to_csv("data/processed_data.csv")
            return transformed_df
    except Exception as e:
        print(f"Error in data processing: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    df = get_dataframe()
    print(df.head())
