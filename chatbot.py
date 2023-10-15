import random

class ChatBot:
    def __init__(self):
        self.greetings = ['Hello', 'Hi', 'Hey', 'Greetings',]
        self.farewells = ['Goodbye', 'Bye', 'Take care', 'See you']
        self.questions = ['How are you?', 'What is your name?', 'Where do you live?', 'What do you do for a living?', 'How can I track my order?',
            'What payment methods do you accept?',
            'Do you offer discounts?''How do I create an account?',
    'Can I change my shipping address after placing an order?',
    'What is your return policy?',
    'Do you offer international shipping?',
    'How do I contact customer support?',
    'Are there any ongoing promotions or sales?',
    'What is the estimated delivery time for my order?']
        self.answers = {
            'How are you?': ['I am good, thank you!', 'I am fine, how about you?'],
            'What is your name?': ['I am a chatbot, so I do not have a name.'],
            'Where do you live?': ['I live on your computer screen.'],
            'What do you do for a living?': ['I help people with their questions and provide assistance on this website.'],
            'How can I track my order?': ['You can track your order by logging into your account and going to the "Order History" section.'],
            'What payment methods do you accept?': ['You talk to the seller directly and decide on the mode of payment.'],
            'Do you offer discounts?': ['It depends on the seller'],
            'How do I create an account?': ['You can create an account by clicking on the "Sign Up" or "Register" link at the top of the page and following the instructions.'],
            'Can I change my shipping address after placing an order?': ['Yes, you can usually change your shipping address if your order has not been shipped yet. Please contact our customer support for assistance.'],
    'What is your return policy?': ['Our return policy allows you to return items within 30 days of purchase for a full refund. Please review our "Returns and Refunds" page for details.'],
    'Do you offer international shipping?': ['Yes, we offer international shipping to many countries. You can check the list of supported countries during the checkout process.'],
    'How do I contact customer support?': ['You can reach our customer support team through the "Contact Us" page on our website or by emailing VITXchange@gmail.com.'],
    'Are there any ongoing promotions or sales?': ['Yes, we frequently run promotions and sales. Visit our "Promotions" page to see our current offers.'],
    'What is the estimated delivery time for my order?': ['Delivery times vary depending on your location and the shipping method chosen. You can find estimated delivery times during checkout.']
            
        }

    def greet(self):
        return random.choice(self.greetings)

    def farewell(self):
        return random.choice(self.farewells)

    def ask_question(self):
        return random.choice(self.questions)

    def answer_question(self, question):
        if question in self.answers:
            return random.choice(self.answers[question])
        else:
            return "I do not know the answer to that question."

def chat(chatbot):
    print(chatbot.greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot.farewell())
            break
        else:
            print(chatbot.answer_question(user_input))

if __name__ == "__main__":
    chatbot = ChatBot()
    chat(chatbot)