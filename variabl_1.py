number_of_completed_homework_assignments = 12 # количество выполненых ДЗ
Number_of_hours_spent = 1.5 # Количество затраченных часов
Course_name = "Python" # Название курса
Time_for_one_task = float(Number_of_hours_spent / number_of_completed_homework_assignments) # Время на одно задание
print("Курс:", Course_name, "всего задач:", number_of_completed_homework_assignments,
      "затрачено часов:", Number_of_hours_spent, "среднее время выполнения", Time_for_one_task)