grades = {
   "Іван": 80,
   "Марія": 95,
   "Олег": 78,
   "Анна": 85
}


name = input("Введіть ім'я студента: ").strip()


# Перевірка: чи ім'я містить лише літери
if not name.isalpha():
   print("Ім'я повинно містити лише літери. Спробуйте ще раз.")
else:
   name = name.capitalize()
   if name in grades:
       print(f"Оцінка студента {name}: {grades[name]}")
   else:
       print(f"Студента з іменем '{name}' не знайдено.")
