__lib__ = "enda"
__version__ = round((4+6) / 10, 2) # 4-количество локализованых функций, 6-количество не локализованых функций
__author__ = "devenda"
__license__ = "Apache 2.0"

if __name__ == "__main__":
    print("\aIt is library, dont execute this👍")
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
    webbrowser.open("https://github.com/binar113/endalib")
    
def json(base={"Значение не присвоено": True}):
    import json
    print(json.dumps(base, ensure_ascii=False, indent=2))

class ru:
    @staticmethod
    def info():
        print(f"Версия {__lib__}: {__version__}\nАвтор: {__author__}")
    
    @staticmethod
    def pause():
        input("Для продолжения нажмите любую клавишу . . .")

    @staticmethod
    def exe():
        print("Вводите команды на свой страх и риск! разработчик ответственности за введённые вами команды НЕ НЕСЁТ")
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
        
class by:
    @staticmethod
    def info():
        print(f"Versija {__lib__}: {__version__}\nAutar: {__author__}")

    @staticmethod
    def pause():
        input("Dlia praciahy nacisnite lubuju klavishu . . .")

    @staticmethod
    def exe():
        print("uvadzite komandy na svoj strah i risk! razrabotchyk za uviedzienyje vami komandy NE NESIOT")
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
        print(f"Version of {__lib__}: {__version__}\nAuthor: {__author__}")

    @staticmethod
    def pause():
        input("Press any key to continue . . .")

    @staticmethod
    def exe():
        print("Execute comands at your own risk! developer takes NO responsibility for entered commands.")
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
