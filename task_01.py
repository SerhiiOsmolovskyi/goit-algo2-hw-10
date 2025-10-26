# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    selected_teachers = []

    while uncovered_subjects:
        best_teacher = None
        subjects_covered_by_best = set()

        for teacher in teachers:
            # Пошук предметів, які цей викладач може викладати, але вони ще не покриті
            can_cover = teacher.can_teach_subjects & uncovered_subjects
            if not can_cover:
                continue

            # Вибір викладача, який покриває найбільше нових предметів
            if (not best_teacher or 
                len(can_cover) > len(subjects_covered_by_best) or
                (len(can_cover) == len(subjects_covered_by_best) and teacher.age < best_teacher.age)):
                best_teacher = teacher
                subjects_covered_by_best = can_cover

        if not best_teacher:
            return None

        # Призначення предметів цьому викладачу
        best_teacher.assigned_subjects = subjects_covered_by_best
        selected_teachers.append(best_teacher)
        # Видалення покритих предметів з множини непокритих
        uncovered_subjects -= subjects_covered_by_best

    return selected_teachers


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
