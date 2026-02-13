# Define the message length threshold
MESSAGE_LENGTH_THRESHOLD = 10


def analyze_messages(messages):
    """
    Analyzes messages by displaying their length and flagging long messages.
    
    Args:
        messages (list): List of messages to analyze
    """
    for message in messages:
        length = len(message)
        print(f"Message: '{message}' | Length: {length}")
        
        if length > MESSAGE_LENGTH_THRESHOLD:
            print(f"⚠ This message is longer than {MESSAGE_LENGTH_THRESHOLD} characters")


def main():
    """Main function to process and display message analysis."""
    messages_list = ["Hi", "Welcome to the platform", "OK"]
    analyze_messages(messages_list)


if __name__ == "__main__":
    main()
