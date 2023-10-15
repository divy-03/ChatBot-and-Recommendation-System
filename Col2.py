import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Create a hypothetical dataset
data = {
    'User': ['User1', 'User1', 'User1', 'User2', 'User2', 'User2', 'User3', 'User3', 'User3'],
    'Food_Item': ['Pizza', 'Burger', 'Sushi', 'Burger', 'Sushi', 'Tacos', 'Pizza', 'Tacos', 'Salad'],
    'Rating': [5, 4, 3, 3, 2, 4, 4, 5, 3]
}

df = pd.DataFrame(data)

# Create a user-item interaction matrix
user_item_matrix = df.pivot_table(index='User', columns='Food_Item', values='Rating', fill_value=0)

# Calculate user similarity using cosine similarity
user_similarity = cosine_similarity(user_item_matrix)

# Function to make recommendations for a user
def recommend_food(user):
    # Find the index of the user
    user_index = user_item_matrix.index.get_loc(user)
    
    # Calculate the weighted average of ratings by similar users
    user_sim_scores = user_similarity[user_index]
    weighted_ratings = user_sim_scores.dot(user_item_matrix.values)

    # Filter out items already rated by the user
    user_rated_items = user_item_matrix.loc[user].values
    weighted_ratings[user_rated_items > 0] = 0
    
    # Get the indices of recommended items (argsort sorts in ascending order)
    recommended_item_indices = weighted_ratings.argsort()[::-1]
    
    # Get the names of recommended items
    recommended_items = user_item_matrix.columns[recommended_item_indices]
    
    return recommended_items

# User input
user_to_recommend = input("Enter a user (e.g., User1, User2, User3): ")
if user_to_recommend in user_item_matrix.index:
    recommended_items = recommend_food(user_to_recommend)
    print(f"Recommended items for {user_to_recommend}: {', '.join(recommended_items)}")
else:
    print(f"User '{user_to_recommend}' not found in the dataset.")
