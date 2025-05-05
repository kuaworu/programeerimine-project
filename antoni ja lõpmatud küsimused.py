import random

class Student:
    def __init__(self, name, mind):
        self.name = name
        self.mind = mind
        self.correct = 0
        self.incorrect = 0
        self.asked_questions = []  # Список заданных этому ученику вопросов

    def answer(self, question):
        print(f"{self.name} küsib küsimust: {question}")
        if self.mind >= random.randint(40, 90):
            print("Õige vastus! (Правильный ответ!)")
            self.correct += 1
        else:
            print("Vale vastus! (Неправильный ответ!)")
            self.incorrect += 1

    def get_result(self):
        return f"{self.name}: {self.correct} õige vastus (правильных ответов), {self.incorrect} vale vastus (неправильных ответов)"

class Teacher:
    def __init__(self, name):
        self.name = name

    def ask(self, student, question):
        print(f"{self.name} küsib {student.name}lt: {question}")
        student.answer(question)

students = [
    Student("марго", 43),
    Student("ваня", 58),
    Student("элина", 80),
    Student("даша", 100),
    Student("милана(logitpv24)", 1),
    Student("настя(tarpv24)", 100),
    Student("ждун", 100),
    Student("катя", 50),
    Student("нильс", 100),
    Student("соломыков", 100)
]

questions = [
    "mis on kapseldamine? (что такое инкапсуляция?)",
    "mis on pärandumine? (что такое наследование?)",
    "mis on polümorfism? (что такое полиморфизм?)",
    "mis on abstraktsioon? (что такое абстракция?)",
    "mis on klass oop-s? (что такое класс в ооп?)",
    "mis on objekt oop-s? (что такое объект в ооп?)",
    "mis on erinevus meetodi ja funktsiooni vahel? (чем отличается метод от функции?)",
    "kus elab spongebob? (где живёт губка боб?)",
    "kes on fixikud? (кто такие фиксики?)",
    "kas balto on hunt või koer? (балто волк или пес?)"
]

teacher = Teacher("anton")
print("i am anton and i am meh, because i make suffer students :( (я антон и я ве, потому что я заставляю учеников страдать)")

# Этот список будет отслеживать все уже заданные вопросы
asked_questions = []

while True:
    print("\n1. Küsi küsimus (задать вопрос)")
    print("2. Vaata tulemusi (посмотреть результаты)")
    print("3. Välju (выход)")

    choice = input("Vali (выбери): ")

    if choice == "1":
        print("\nVali õpilane (выбери ученика):")
        for i, student in enumerate(students):
            print(f"{i+1}. {student.name}")
        student_choice = int(input("Õpilase number (номер ученика): ")) - 1
        selected_student = students[student_choice]

        # Получаем список вопросов, которые ещё не задавались этому ученику
        available_questions = []
for q in questions:
    if q not in selected_student.asked_questions and q not in asked_questions:
        available_questions.append(q)


        if not available_questions:
            print("Küsimused on kõik läbi! (Вопросы закончились!)")
            break

        print("\nVali küsimus (выбери вопрос):")
        for i, question in enumerate(available_questions):
            print(f"{i+1}. {question}")
        question_choice = int(input("Küsimuse number (номер вопроса): ")) - 1
        selected_question = available_questions[question_choice]

        # Добавляем этот вопрос в список заданных вопросам ученику и всему классу
        selected_student.asked_questions.append(selected_question)
        asked_questions.append(selected_question)

        teacher.ask(selected_student, selected_question)

    elif choice == "2":
        print("\n--- Tulemused (результаты) ---")
        for student in students:
            print(student.get_result())

    elif choice == "3":
        print("Head aega! (До свидания!)")
        break

    else:
        print("Vale valik! (Неверный выбор!)")
