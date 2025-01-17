def plot_rating_distribution(df):
    """Plots the distribution of ratings in the Zomato dataset."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rating'], kde=True, color='blue')
    plt.title('Distribution of Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()

# Call the function
plot_rating_distribution(df)
