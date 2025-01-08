import random 
from list import keyboard_characters
class generate: 
    def __init__(self):
        self.length = None
    def ask_length(self):
        while self.length is None:
            try:
                ask_len = int(input("how long do you want your password to be?> "))
                self.length = ask_len
            except ValueError:
                print("Invalid input")
    def generate_password(self):
        password = ''
        while self.length > 0:
            randomize = random.choice(keyboard_characters)
            password += ''.join(randomize)
            self.length -= 1
        print(f"Generate password>{password}")
        print(len(password))

if __name__ == "__main__":
    function = generate()
    function.ask_length()
    function.generate_password()


#ways to improve 
#add a way where the user can decide the use of special characters, numbers and characters