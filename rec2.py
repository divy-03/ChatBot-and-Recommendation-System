import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Extended product data with categories and subcategories
data = {
    'Product': ['Smartphone', 'Tablet', 'Laptop', 'eBook Reader', 'Notebook', 'Pen', 'Bicycle', 'Camera', 'Headphones', 'Mountain Bike', 'Road Bike', 'City Bike', 'Sci-Fi Book', 'Mystery Book', 'Romance Book', 'Earphones', 'Chargers'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Books', 'Stationery', 'Stationery', 'Cycles', 'Electronics', 'Electronics', 'Cycles', 'Cycles', 'Cycles', 'Books', 'Books', 'Books', 'Electronics', 'Electronics'],
    'Subcategory': [None, None, None, None, None, None, None, None, 'Headphones', None, None, None, None, None, None, 'Earphones', 'Chargers']
}

df = pd.DataFrame(data)

# Create a TF-IDF vectorizer to convert text data into numerical vectors
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the 'Category' column into TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Category'])

# Compute the cosine similarity between categories
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create separate lists of products for each category and subcategory
category_lists = {}
subcategory_lists = {}

unique_categories = df['Category'].unique()
unique_subcategories = df['Subcategory'].dropna().unique()

for category in unique_categories:
    category_products = df[df['Category'] == category]['Product'].tolist()
    category_lists[category] = category_products

for subcategory in unique_subcategories:
    subcategory_products = df[df['Subcategory'] == subcategory]['Product'].tolist()
    subcategory_lists[subcategory] = subcategory_products

# Function to get recommendations based on category or subcategory
def get_recommendations(category, product, cosine_sim=cosine_sim, category_lists=category_lists, subcategory_lists=subcategory_lists):
    category_products = category_lists.get(category, [])
    if category not in unique_categories:
        category_products = subcategory_lists.get(category, [])
    
    if not category_products:
        return []

    idx = df[df['Product'] == product].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    product_indices = [i[0] for i in sim_scores]

    # Filter out products not in the selected category or subcategory
    recommended_products = [df['Product'].iloc[i] for i in product_indices if df['Product'].iloc[i] in category_products]

    return recommended_products[:3]  # Get the top 3 similar products in the same category or subcategory

# Display the list of valid product categories to the user
valid_categories = list(unique_categories) + list(unique_subcategories)
print("Valid categories are:")
print(valid_categories)

# Get user input for a category or subcategory
selected_category = input("Select a category from the list above: ").capitalize()

if selected_category in valid_categories:
    # Get user input for a product within the selected category or subcategory
    category_products = category_lists.get(selected_category, []) + subcategory_lists.get(selected_category, [])
    print(f"Products in the {selected_category} category or subcategory are:")
    print(category_products)
    selected_product = input(f"Select a product from the {selected_category} category or subcategory: ").capitalize()

    if selected_product in category_products:
        recommendations = get_recommendations(selected_category, selected_product)
        if recommendations:
            print(f"Recommendations for {selected_product} in the {selected_category} category or subcategory:")
            print(recommendations)
        else:
            print("No recommendations available for the selected product.")
    else:
        print("Invalid product input. Please select a product from the specified category or subcategory.")
else:
    print("Invalid category or subcategory input. Please select a valid category or subcategory from the list above.")

# Ask the user for their recently purchased product
recently_purchased_product = input("Enter the product you recently purchased: ").capitalize()

if recently_purchased_product in df['Product'].tolist():
    if recently_purchased_product in ['Smartphone', 'Tablet']:
        accessories_recommendations = get_recommendations('Electronics', recently_purchased_product)
        if accessories_recommendations:
            print(f"Recommendations for {recently_purchased_product} accessories:")
            print(accessories_recommendations)
        else:
            print(f"No accessory recommendations available for {recently_purchased_product}.")
    else:
        subcategory = df[df['Product'] == recently_purchased_product]['Subcategory'].values[0]
        if subcategory:
            recommended_products = get_recommendations(subcategory, recently_purchased_product)
            if recommended_products:
                print(f"Recommendations for {recently_purchased_product} from the {subcategory} subcategory:")
                print(recommended_products)
            else:
                print("No recommendations available for the selected product.")
        else:
            print(f"{recently_purchased_product} doesn't belong to a subcategory.")
else:
    print("The recently purchased product is not in the dataset.")
