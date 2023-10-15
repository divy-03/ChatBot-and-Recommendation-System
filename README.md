## ChatBot

The `ChatBot` class in this Python script simulates a chatbot that can greet users, answer predefined questions, and engage in conversations. The chatbot's responses are randomly selected from predefined responses.

### Usage

To use the chatbot, follow these steps:

1. Create an instance of the `ChatBot` class.
2. Call the `greet` method to initiate the conversation with a greeting.
3. Enter user messages, and the chatbot will respond based on predefined answers.
4. To end the conversation, simply type "bye."

The chatbot can be customized by modifying the predefined greetings, farewells, questions, and answers.

## User-Item Recommendation

The Python script in this file demonstrates user-item recommendation using a hypothetical dataset. It calculates recommendations based on user similarity using cosine similarity. Users are asked to input a user, and the script recommends items for that user.

### Usage

To use the recommendation script, follow these steps:

1. Run the script and provide a user input, e.g., "User1," "User2," or "User3."
2. The script will recommend food items for the selected user based on their similarity to other users' preferences.
3. The recommendations consider the user's recently purchased product and, in the case of "Smartphone" or "Tablet," provide accessory recommendations.

## Seller-Based Recommendation

This Python script demonstrates seller-based recommendations using a hypothetical dataset. It calculates recommendations based on seller similarity using cosine similarity. Users are asked to input a seller, and the script recommends food items from that seller.

### Usage

To use the seller-based recommendation script, follow these steps:

1. Run the script and provide a seller input, e.g., "Seller1," "Seller2," or "Seller3."
2. The script will recommend food items sold by the selected seller based on their similarity to other sellers' offerings.

## Product Category Recommendation

The Python script in this file recommends products within the same category or subcategory based on user input. It uses a TF-IDF vectorizer and cosine similarity to find similar products.

### Usage

To use the product category recommendation script, follow these steps:

1. Run the script.
2. Select a category or subcategory from the provided list.
3. Enter a product from the selected category or subcategory.
4. The script will recommend up to three similar products within the same category or subcategory.

Please ensure you have the required Python libraries (e.g., pandas, scikit-learn) installed to run these scripts.