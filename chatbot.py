import re

# Function to generate a chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for easier matching
    
    # Rule-based responses
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'\bhow are you\b|\bhow are you doing\b', user_input):
        return "I'm just a bot, but I'm functioning as expected! How about you?"
    elif re.search(r'\bwhat is your name\b|\bwho are you\b', user_input):
        return "I'm ChatBot, your virtual assistant!"
    elif re.search(r'\bwhat can you do\b|\bwhat are your skills\b', user_input):
        return "I can respond to simple queries based on predefined rules!"
    elif re.search(r'\bwho is the president of india\b', user_input):
        return "The President of India is Droupadi Murmu."
    elif re.search(r'\bwho is the father of ai\b|\bwho is the father of artificial intelligence\b', user_input):
        return "John McCarthy is considered the father of Artificial Intelligence."
    elif re.search(r'\bhow to learn python syllabus wise\b|\bhow to learn python provide syllabus\b', user_input):
        return (
            "To learn Python, start with basics like syntax, variables, and data types. "
            "Next, cover control flow (if-else, loops), functions, and modules. Learn about "
            "object-oriented programming (OOP), then move on to file handling, exception handling, "
            "and libraries like NumPy and Pandas. Finally, explore APIs, web scraping, and advanced "
            "topics such as decorators and generators."
        )
    elif re.search(r'\bbye\b|\bexit\b|\bleave\b', user_input):
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Can you try asking something else?"

# Main chat loop
def chat():
    print("ChatBot: Hello! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
