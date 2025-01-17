def summarize_data(df):
    """Returns a summary of the dataset including data types, null values, and basic statistics."""
    summary = {
        'Data Types': df.dtypes,
        'Missing Values': df.isnull().sum(),
        'Basic Statistics': df.describe()
    }
    return summary

# Get summary
summary = summarize_data(df)
print(summary)
