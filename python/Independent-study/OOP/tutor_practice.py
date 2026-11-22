class MathHelper():
    def __init__(self, bot_name, student_name, level):
        self.bot_name = bot_name
        self.student_name = student_name
        self.level = level

class ChemHelper():
    def __init__(self, bot_name, student_name, level):
        self.bot_name = bot_name
        self.student_name = student_name
        self.level = level

def get_info():
    info = {}
    subject = input("What subject do you need help with? ")
    level = input("What level are you at? (grade number): ")
    bot_name = input("What would you like your helper-bots name to be? ")

    info['Subject'] = subject
    info['Level'] = level
    info['Bot name'] = bot_name
    
    return info

def main():
    students = {}  # Stores { "Student Name": their_bot }

    print("Welcome to Helper-Bot!")

    while True:
        print("\n--- Main Menu ---")
        name = input("What's your name? (or type 'quit' to exit): ")

        if name.lower() == "quit":
            print("Goodbye!")
            break

        # 1. Check if this student already has a bot
        if name in students:
            my_bot = students[name]
            print(f"Welcome back, {name}! Pulling up {my_bot.bot_name}...")

        # 2. If they are new, sign them up and save their bot
        else:
            print(f"Nice to meet you, {name}! Let's set up your bot.")
            info = get_info()

            if info['Subject'].lower() == "math":
                my_bot = MathHelper(info['Bot name'], name, info['Level'])
            elif info['Subject'].lower() == "chemistry":
                my_bot = ChemHelper(info['Bot name'], name, info['Level'])
            else:
                print("Sorry, I only have Math and Chemistry helpers right now.")
                continue  # Jumps back to the top of the loop

            students[name] = my_bot  # Save the bot under their name

        # 3. Now use the bot
        print(f"Hi {my_bot.student_name}! I'm {my_bot.bot_name} (Grade {my_bot.level}).")
        
main()