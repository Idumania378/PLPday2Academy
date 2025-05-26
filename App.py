print ("This is day 2 of Essentials of Software Engineering") 

class RuleBasedChatBot:
    def __init__(self):
        self.rules = {
            "hi": "Hello! How can I assist you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a program, but thanks for asking! How can I help you?",
            "bye": "Goodbye! Have a great day!",
            "help": "Sure! What do you need help with?",
            "how are you": "I am good bruh",
            }
    def respond(self, message):
        message = message.lower().strip()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        return "I'm sorry, I don't understand that. Can you please rephrase?"

class RuleBasedChatBot:
    def __init__(self):
        self.rules = {
            "hi": "Hello! How can I assist you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a program, but thanks for asking! How can I help you?",
            "bye": "Goodbye! Have a great day!",
            "help": "Sure! What do you need help with?",
            "how are you": "I am good bruh",
            }
    def respond(self, message):
        message = message.lower().strip()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        return "I'm sorry, I don't understand that. Can you please rephrase?"

    #example
chatbot = RuleBasedChatBot()
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot.respond(user_input))
   
