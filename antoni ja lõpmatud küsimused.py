import random

class student:
    def __init__(self, name, mind):
        self.name = name
        self.mind = mind
        self.asked = False
        self.asked_questions = []
        self.correct_answers = 0

    def answer_question(self):
        return random.randint(0, 100) <= self.mind

class teacher:
    def __init__(self, name):
        self.name = name
        self.diary = []

    def ask_specific_question(self, student, question_index, questions):
        question = questions[question_index]
        print("\nKüsimus: " + question)
        if student.answer_question():
            print("Õige!")
            student.correct_answers += 1
        else:
            print("Vale.")
        student.asked_questions.append(question_index)

    def finish_exam(self, student):
        if student.correct_answers >= 2:
            result = "zachet"
        else:
            result = "nezachet"
        self.diary.append(student.name + ": " + result)
        student.asked = True
        print("\nTulemus: " + result)

    def show_diary(self):
        print("\n--- päevik ---")
        if len(self.diary) == 0:
            print("päevik on tühi.")
        else:
            for entry in self.diary:
                print(entry)

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

anton = teacher("anton")

def menu():
    while True:
        print("\n1. päevik")  
        print("2. piinama õpilasi")  
        print("3. valja") 

        choice = input("vali: ")

        if choice == "1":
            anton.show_diary()

        elif choice == "2":
            available_students = []
            for s in stu:
                if not s.asked:
                    available_students.append(s)

            if len(available_students) == 0:
                print("Kõiki õpilasi on juba küsitletud.")
                continue

            print("\nVali õpilane:")
            number = 1
            for student_obj in available_students:
                print(str(number) + ". " + student_obj.name)
                number += 1

            try:
                choice_index = int(input("sisesta number: ")) - 1
                chosen_student = available_students[choice_index]
            except:
                print("Vale valik.")
                continue

            print(f"\nAlustame küsitlemist: {chosen_student.name}")

            while len(chosen_student.asked_questions) < 3:
                print("\nVali küsimus:")
                for i in range(len(questions)):
                    if i not in chosen_student.asked_questions:
                        print(str(i + 1) + ". " + questions[i])

                try:
                    q_index = int(input("sisesta küsimuse number: ")) - 1

                    if q_index < 0:
                        print("Liiga väike number.")
                        continue
                    if q_index >= len(questions):
                        print("Liiga suur number.")
                        continue
                    if q_index in chosen_student.asked_questions:
                        print("See küsimus on juba küsitud.")
                        continue

                    anton.ask_specific_question(chosen_student, q_index, questions)

                except:
                    print("Viga sisestamisel.")
                    continue

            anton.finish_exam(chosen_student)

        elif choice == "3":
            print("Head aega!")
            break

        else:
            print("Tundmatu valik.")

menu()
