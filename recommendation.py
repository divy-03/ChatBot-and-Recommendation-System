import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Extended product data with more diverse categories
data = {
    'Product': ['Smartphone', 'Tablet', 'Laptop', 'eBook Reader', 'Notebook', 'Pen', 'Bicycle', 'Camera', 'Headphones', 'Mountain Bike', 'Road Bike', 'City Bike', 'Sci-Fi Book', 'Mystery Book', 'Romance Book'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Books', 'Stationery', 'Stationery', 'Cycles', 'Electronics', 'Electronics', 'Cycles', 'Cycles', 'Cycles', 'Books', 'Books', 'Books']
}

df = pd.DataFrame(data)

# Create a TF-IDF vectorizer to convert text data into numerical vectors
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the 'Category' column into TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Category'])

# Compute the cosine similarity between categories
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create separate lists of products for each category
category_lists = {}
unique_categories = df['Category'].unique()
for category in unique_categories:
    category_lists[category] = df[df['Category'] == category]['Product'].tolist()

# Function to get recommendations based on category
def get_recommendations(category, product, cosine_sim=cosine_sim, lists=category_lists):
    category_products = lists.get(category, [])
    
    if not category_products:
        return []
    
    idx = df[df['Product'] == product].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    product_indices = [i[0] for i in sim_scores]
    
    # Filter out products not in the selected category
    recommended_products = [df['Product'].iloc[i] for i in product_indices if df['Product'].iloc[i] in category_products]
    
    return recommended_products[:3]  # Get the top 3 similar products in the same category

# Display the list of valid product inputs to the user
valid_categories = list(unique_categories)
print("Valid categories are:")
print(valid_categories)

# Get user input for a category
selected_category = input("Select a category from the list above: ").capitalize()

if selected_category in valid_categories:
    # Get user input for a product within the selected category
    category_products = category_lists[selected_category]
    print(f"Products in the {selected_category} category are:")
    print(category_products)
    selected_product = input(f"Select a product from the {selected_category} category: ").capitalize()
    
    if selected_product in category_products:
        recommendations = get_recommendations(selected_category, selected_product)
        if recommendations:
            print(f"Recommendations for {selected_product} in the {selected_category} category:")
            print(recommendations)
        else:
            print("No recommendations available for the selected product.")
    else:
        print("Invalid product input. Please select a product from the specified category.")
else:
    print("Invalid category input. Please select a valid category from the list above.")
