unsent_messages = ["Hello, world!", "How are you?", "I'm doing great!"]
sent_messages = []

def send_messages(messages):
    while messages:
        message = messages.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)

send_messages(unsent_messages[:])

print("\nUnsent messages:")
print(unsent_messages)
print("\nSent messages:")
print(sent_messages)