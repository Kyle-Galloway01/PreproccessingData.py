import pandas as pd

def load_data(csv_file):
    """Load CSV data into a Pandas DataFrame."""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None

def preprocess_data(df):
    """Preprocess the data: clean and handle missing values."""
    # Drop rows with missing values
    df = df.dropna()

    # Remove leading and trailing whitespaces from string columns
    str_cols = df.select_dtypes(include=['object']).columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    return df

def main():
    """Main function to orchestrate the data preprocessing."""
    csv_file = 'data.csv'
    print(f"Loading data from '{csv_file}'...")
    df = load_data(csv_file)
    if df is None:
        print("Failed to load data. Exiting.")
        return

    print("Preprocessing data...")
    df = preprocess_data(df)

    # Additional preprocessing steps can be added here

    print("Preprocessing completed.")
    print("Processed DataFrame:")
    print(df.head())

if __name__ == "__main__":
    main()
