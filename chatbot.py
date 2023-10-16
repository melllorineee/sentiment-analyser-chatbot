import re
import random
from textblob import TextBlob

pairs = [
    {
        'pattern': r'hello|hi|hey',
        'responses': ['Hello!', 'Hi there!', 'Hey!']
    },
    {
        'pattern': r'how are you',
        'responses': ['I am doing well, thanks!', 'I am just a computer program, but I\'m here to help!', 'I\'m functioning as expected. How can I assist you?']
    },
    {
        'pattern': r'what is your name',
        'responses': ['I am an AI chatbot.', 'You can call me ChatBot.', 'I\'m just a program, so I don\'t have a name.']
    },
    {
        'pattern': r'my name is (.*)',
        'responses': ['Hello , How are you today?','Hi %1']
    },
    {
        'pattern': r"how are you ?",
        'responses': ["I\'m doing good. How about you?","I\'m fine, what about you?"]
    },
    {
        'pattern': r"i am fine|i'm good|i'm healthy",
        'responses': ["Great to hear that, How can I help you?","nice to hear it"]
     }
    # Add more pairs here
]
def chatbot_response(user_input):
    for pair in pairs:
        pattern = re.compile(pair['pattern'], re.IGNORECASE)
        if re.search(pattern, user_input):
            return random.choice(pair['responses'])
    return ""

def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment
def generate_response(sentiment):
    if sentiment > 0:
        return "I'm glad you're feeling positive!"
    elif sentiment < 0:
        return "I'm sorry you're feeling negative. Try eating an ice cream and light up your mood;)"
    else:
        return "I see you're feeling neutral. How can I assist you today?"

print("Hello! I am a chatbot. How can I assist you today?")
while True:
    # Get user input
    user_input = input("User: ")
    user_input.lower()
    # Exit if the user says "bye"
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        res=chatbot_response(user_input)
        if res!="":
            print("Chatbot: ",res)
        elif res=="":
            sentiment = get_sentiment(user_input)
            response = generate_response(sentiment)
            print("Chatbot: ",response)
