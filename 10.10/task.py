class Student:
    students = []

    def __init__(self, name):
        self.name = name
        self.grades = []
        Student.students.append(self)

    def add_grade(self, grade):
        if Student.is_valid_grade(grade):
            self.grades.append(grade)
        else:
            print(f"Оценка {grade} недопустима (должна быть от 1 до 5).")

    def get_average(self):
        if len(self.grades) == 0:
            print(f"У студента {self.name} нет оценок.")
        else:
            avg = sum(self.grades) / len(self.grades)
            print(f"Средняя оценка студента {self.name}: {avg:.2f}")

    @classmethod
    def get_class_average(cls):
        all_grades = []
        for s in cls.students:
            all_grades.extend(s.grades)
        if len(all_grades) == 0:
            print("Нет ни одной оценки у студентов.")
        else:
            avg = sum(all_grades) / len(all_grades)
            print(f"Средняя оценка всех студентов: {avg:.2f}")

    @staticmethod
    def is_valid_grade(grade):
        return grade >= 1 and grade <= 5


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить нового студента")
        print("2. Добавить оценку студенту")
        print("3. Вывести среднюю оценку студента")
        print("4. Вывести среднюю оценку всех студентов")
        print("5. Проверить допустимость оценки")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            name = input("Введите имя студента: ")
            Student(name)
            print("Студент добавлен.")
        elif choice == "2":
            name = input("Введите имя студента: ")
            student = None
            for s in Student.students:
                if s.name == name:
                    student = s
                    break
            if student is None:
                print("Студент не найден.")
            else:
                grade_str = input("Введите оценку (1–5): ")
                if grade_str.isdigit():
                    grade = int(grade_str)
                    student.add_grade(grade)
                else:
                    print("Нужно ввести число!")
        elif choice == "3":
            name = input("Введите имя студента: ")
            found = False
            for s in Student.students:
                if s.name == name:
                    s.get_average()
                    found = True
                    break
            if not found:
                print("Студент не найден.")
        elif choice == "4":
            Student.get_class_average()
        elif choice == "5":
            grade_str = input("Введите оценку для проверки: ")
            if grade_str.isdigit():
                grade = int(grade_str)
                if Student.is_valid_grade(grade):
                    print("Оценка допустима.")
                else:
                    print("Оценка недопустима (должна быть от 1 до 5).")
            else:
                print("Нужно ввести число!")
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Повторите попытку.")


main()
