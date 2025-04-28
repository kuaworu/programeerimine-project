import random

class student:
    def __init__(self, name, mind):
        self.name = name
        self.mind = mind
        self.asked_questions = []
        self.correct_answers = 0
        
    def answer_question(self):
        pass
    
class teacher:
    def __init__(self, name):
        self.name = name
        self.diary = []
        
    def ask_specific_question(self, student, question_index, questions):
        pass
    
    def finish_exam(self, student):
        pass
    
    def show_diary(self):
        pass
    
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

teacher = teacher("anton")

print("антон, вы плохой :(")