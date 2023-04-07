import random
from time import sleep

def chatbot():
    print("Welcome! My name is Chatbot.")
    while True:
        sleep(1)
        user_input = input("Please, ask something, or press 'q' to quit: ")
        if user_input.lower() == "q":
            print("Good bye!")
            sleep(5)
            break
        else:
            responses = ["Please ask something else, I don't understand.",
                         "This is a good question, but unfortunately I don't have the answer.",
                         "Please clarify your question.",
                         "I'm sorry, I don't understand what you asked."]
            bot_response = random.choice(responses)
            print(bot_response)

chatbot()
