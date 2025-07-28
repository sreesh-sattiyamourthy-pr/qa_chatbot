from chatbot_app.chatbot import get_response

def main():
    print("Simple Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        print("Bot:", get_response(user_input))

if __name__ == "__main__":
    main()
