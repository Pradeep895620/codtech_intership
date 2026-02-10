# Sequential Question Chatbot

def run_sequential_chatbot():
    print("--- CODTECH AI CHATBOT ---")
    print("Type 'quit' at any time to exit.\n")

    # Dictionary to store answers
    user_data = {}

    # Question 1: Name
    name = input("What's your name? ")
    if name.lower() in ["quit", "bye"]:
        print("Goodbye! Have a great day.")
        return
    user_data['name'] = name
    print(f"Hello {name}! Nice to meet you.")

    # Question 2: Mood
    mood = input(f"How are you feeling today, {name}? ")
    if mood.lower() in ["quit", "bye"]:
        print("Goodbye! Have a great day.")
        return
    user_data['mood'] = mood
    print(f"Thanks for sharing that you're feeling {mood}!")

    # Question 3: Favorite color
    color = input("What's your favorite color? ")
    if color.lower() in ["quit", "bye"]:
        print("Goodbye! Have a great day.")
        return
    user_data['color'] = color
    print(f"{color} is a beautiful color!")

    # Question 4: Hobby
    hobby = input("What's your favorite hobby? ")
    if hobby.lower() in ["quit", "bye"]:
        print("Goodbye! Have a great day.")
        return
    user_data['hobby'] = hobby
    print(f"That sounds fun! {hobby} is a great way to spend time.")

    # Summary
    print("\n--- Summary of your answers ---")
    print(f"Name: {user_data['name']}")
    print(f"Mood: {user_data['mood']}")
    print(f"Favorite Color: {user_data['color']}")
    print(f"Hobby: {user_data['hobby']}")
    print("\nIt was great talking to you! Goodbye!")

if __name__ == "__main__":
    run_sequential_chatbot()
