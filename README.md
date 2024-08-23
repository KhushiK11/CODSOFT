# CODSOFT
# Rule-Based ChatBot

A simple rule-based chatbot built with Python. This chatbot responds to user inputs based on predefined rules, using basic pattern matching techniques such as regular expressions. It helps in understanding the basics of Natural Language Processing (NLP) by identifying user queries and providing appropriate responses.

## Features
- Responds to basic greetings and general questions.
- Answers specific predefined questions, such as:
  - Who is the President of India?
  - Who is the father of Artificial Intelligence?
  - How to learn Python syllabus-wise in a paragraph?
- Handles simple queries using if-else conditions and regular expressions.
- Supports easily extensible rules for new responses.

## Getting Started

### Prerequisites
Make sure you have the following installed on your machine:
- [Python 3.x](https://www.python.org/downloads/)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/KhushiK11/CODSOFT.git
   cd rule-based-chatbotNo external dependencies are required for this project, as it is built using only the Python Standard Library.Running the ChatbotOpen a terminal (or command prompt) and navigate to the project folder where chatbot.py is located:cd path/to/projectRun the Python script:python chatbot.pyThe chatbot will start a conversation, and you can type in your queries. Type exit to end the conversation.Example ConversationChatBot: Hello! Type 'exit' to end the conversation.
You: Hi
ChatBot: Hello! How can I assist you today?
You: Who is the President of India?
ChatBot: The President of India is Droupadi Murmu.
You: Who is the father of Artificial Intelligence?
ChatBot: John McCarthy is considered the father of Artificial Intelligence.
You: How to learn Python syllabus-wise in paragraph?
ChatBot: To learn Python, start with basics like syntax, variables, and data types...
You: Bye
ChatBot: Goodbye! Have a great day!How It WorksThe chatbot uses Python's re module for pattern matching with regular expressions. The user input is compared against predefined patterns using if-else statements. Depending on the match, the bot responds with an appropriate message.The chatbot runs in a loop and waits for user input. It will continue responding to the user until the input matches the exit condition (exit).Key Sections of Code:Input Handling: The user input is converted to lowercase for easier matching and compared against various patterns.Pattern Matching: Regular expressions are used to match user inputs such as greetings, specific queries (e.g., "Who is the President of India?"), and exit conditions.Response Generation: Based on the matched patterns, the chatbot generates a response from a set of predefined rules.Extending the ChatbotYou can easily extend the chatbot by adding more patterns and responses. Here's how:Open the chatbot.py file.Add a new elif block to match the desired pattern. For example:elif re.search(r'\bwhat is python\b|\bexplain python\b', user_input):
    return "Python is a high-level, interpreted programming language known for its simplicity and versatility."Save the file and run the chatbot again. The new pattern will now trigger a response when matched.ContributingIf you'd like to contribute to the project:Fork the repository.Create a new branch (git checkout -b feature-branch).Make your changes.Commit your changes (git commit -m 'Add some feature').Push to the branch (git push origin feature-branch).Open a pull request.
