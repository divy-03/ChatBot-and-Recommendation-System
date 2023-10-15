import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Create a hypothetical dataset for seller-based recommendations
data = {
    'Seller': ['Seller1', 'Seller1', 'Seller2', 'Seller2', 'Seller3', 'Seller3'],
    'Food_Item': ['Pizza', 'Burger', 'Burger', 'Sushi', 'Pizza', 'Sushi'],
    'Rating': [5, 4, 3, 2, 4, 5]
}

df = pd.DataFrame(data)

# Create a seller-item interaction matrix
seller_item_matrix = df.pivot_table(index='Seller', columns='Food_Item', values='Rating', fill_value=0)

# Calculate seller similarity using cosine similarity
seller_similarity = cosine_similarity(seller_item_matrix)

# Function to make recommendations for a seller
def recommend_food_from_seller(seller):
    # Find the index of the seller
    seller_index = seller_item_matrix.index.get_loc(seller)
    
    # Calculate the weighted average of ratings for food items by similar sellers
    seller_sim_scores = seller_similarity[seller_index]
    weighted_ratings = seller_sim_scores.dot(seller_item_matrix.values)

    # Get the indices of recommended food items (argsort sorts in ascending order)
    recommended_item_indices = weighted_ratings.argsort()[::-1]
    
    # Get the names of recommended food items
    recommended_items = seller_item_matrix.columns[recommended_item_indices]
    
    return recommended_items

# Seller input
seller_to_recommend = input("Enter a seller (e.g., Seller1, Seller2, Seller3): ")
if seller_to_recommend in seller_item_matrix.index:
    recommended_items = recommend_food_from_seller(seller_to_recommend)
    print(f"Recommended food items from {seller_to_recommend}: {', '.join(recommended_items)}")
else:
    print(f"Seller '{seller_to_recommend}' not found in the dataset.")
