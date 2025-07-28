def get_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! Need any assistance?",
        "how are you": "I'm doing great, thanks for asking!",
        "bye": "Goodbye! Have a great day."
    }

    user_input = user_input.lower().strip()
    return responses.get(user_input, "I'm not sure I understand. Can you rephrase?")
