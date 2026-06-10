"""
библиотека простая🤪
"""

__lib__ = "enda"
__version__ = round((4+5) / 10, 2) # 4-количество локализованых функций, 4-количество не локализованых функций
__author__ = "devenda"
__license__ = "Apache 2.0"

if __name__ == "__main__":
    print("\aЭто библиотека, не недо выполнять её👍")
    input()


def kolokol(y=True): # kolokolnia
    import random
    import time
    import threading
    def zvon():
        while y:
            print("\a", end="")
            print("🔔")
            time.sleep(random.uniform(0.5, 2))
    zvon = threading.Thread(target=zvon)
    zvon.start()

def httpcat(cat=500):
    import webbrowser
    url = "https://http.cat/"+str(cat)
    webbrowser.open(url)
    
def clr():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
def url(base="https://example.com"):
    import webbrowser
    webbrowser.open("http://" + base)
    
def git():
    import webbrowser
    webbrowser.open("https://github.com/binar113/enda")


class ru:
    @staticmethod
    def info():
        print(f"Версия enda: {__version__}\nАвтор: {__author__}")
    
    @staticmethod
    def pause():
        input("Для продолжения нажмите любую клавишу . . .")

    @staticmethod
    def exe():
        while True:
            inpt = input(">>> ")
            if inpt == "exit":
                break
            else:
                try:
                    eval(inpt)
                except:
                    print("Ошибка .  .  . ")
         
    @staticmethod
    def wow():
        import webbrowser
        print("Держи рикролл🤪")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
class tr: # трасянка, смесь русского и беларусского(а тут ещё и латинкой)
    @staticmethod
    def info():
        print(f"Versija enda: {__version__}\nAutar: {__author__}")

    @staticmethod
    def pause():
        input("Dlia praciahy nacisnite lubuju klavishu . . .")

    @staticmethod
    def exe():
        while True:
            inpt = input(">>> ")
            if inpt == "exit":
                break
            else:
                try:
                    eval(inpt)
                except:
                    print("Pamylka .  .  . ")
       
    @staticmethod
    def wow():
        import webbrowser
        print("Trymaj rykrol🤪")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

class en:
    @staticmethod
    def info():
        print(f"Version of enda: {__version__}\nAuthor: {__author__}")

    @staticmethod
    def pause():
        input("Press any key to continue . . .")

    @staticmethod
    def exe():
        while True:
            inpt = input(">>> ")
            if inpt == "exit":
                break
            else:
                try:
                    eval(inpt)
                except:
                    print("error .  .  . ")

    @staticmethod
    def wow():
        import webbrowser
        print("Pick the rickroll🤪")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")