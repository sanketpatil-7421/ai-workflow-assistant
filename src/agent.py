import datetime

def simple_agent(command: str) -> str:
    # Clean up user input
    cmd = command.strip().lower()

    if "hello" in cmd or "hi" in cmd:
        return "Hello! How can I help you today?"
    
    elif "date" in cmd or "time" in cmd:
        now = datetime.datetime.now()
        return f"Today's date is {now.strftime('%A, %B %d, %Y')} and the current time is {now.strftime('%I:%M %p')}."
    
    elif "bye" in cmd or "exit" in cmd:
        return "Goodbye! Have a great day."
    
    else:
        return f"Unknown command: '{command}'. Try saying 'hello', 'date', or 'bye'."

# Simple interaction loop
if __name__ == "__main__":
    print("Agent started. Type 'hello', 'date', or 'bye' (or 'exit' to quit).")
    while True:
        user_input = input("\nYou: ")
        response = simple_agent(user_input)
        print(f"Agent: {response}")
        
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break
