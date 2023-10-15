# Define a function to get the chatbot's response
def chatbot_response(user_input):
    # Convert the user input to lowercase for easier pattern matching
    user_input = user_input.lower()
    
    # Define some predefined rules and responses
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a computer program, but I'm here to help you!"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I can help you with general information. Just ask me a question."
    else:
        return "I'm sorry, I don't understand that. Please ask me something else."

# Main loop for user interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
