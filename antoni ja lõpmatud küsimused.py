import random

class student:
    def __init__(self, name, mind):
        self.name = name
        self.mind = mind

    def answer_question(self):
        #
        return random.randint(0, 100) <= self.mind

stu = [
    student("марго", 43),
    student("ваня", 58),
    student("элина", 80),
    student("даша", 100),
    student("милана(logitpv24)", 1),
    student("настя(tarpv24)", 100),
    student("ждун", 100),
    student("катя", 50),
    student("нильс", 100),
    student("соломыков", 100)
]

diary = []

questions = [
    "mis on kapseldamine? (что такое инкапсуляция?)",
    "mis on pärandumine? (что такое наследование?)",
    "mis on polümorfism? (что такое полиморфизм?)",
    "mis on abstraktsioon? (что такое абстракция?)",
    "mis on klass oop-s? (что такое класс в ооп?)",
    "mis on objekt oop-s? (что такое объект в ооп?)",
    "mis on erinevus meetodi ja funktsiooni vahel? (чем отличается метод от функции?)",
    "kus elab spongebob? (где живет губка боб?)",
    "kes on fixikud? (кто такие фиксики?)",
    "kas balto on hunt või koer? (балто волк или пес?)"
]

def menu():
    while True:
        print("\n1. päevik")  
        print("2. piinama õpilasi")  # piinama - пытать
        print("3. valja") 

        choice = input("vali: ")