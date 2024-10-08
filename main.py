import pandas as pd
import numpy as np

# Создаем DataFrame с данными о 10 учениках и оценками по 5 предметам
data = {
    'Ученик': ['Алексей', 'Мария', 'Иван', 'Ольга', 'Сергей', 'Анна', 'Дмитрий', 'Елена', 'Никита', 'Татьяна'],
    'Математика': [85, 92, 78, 65, 90, 88, 70, 76, 82, 91],
    'Физика': [78, 85, 88, 92, 74, 80, 77, 84, 90, 93],
    'Химия': [91, 72, 88, 86, 79, 75, 85, 90, 87, 89],
    'Литература': [83, 85, 88, 80, 79, 82, 90, 84, 76, 81],
    'История': [89, 91, 77, 88, 90, 86, 82, 84, 85, 87]
}

df = pd.DataFrame(data)

# Выводим первые несколько строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Вычисляем среднюю оценку по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Вычисляем медианную оценку по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисляем Q1 и Q3 для оценок по математике
q1_math = df['Математика'].quantile(0.25)
q3_math = df['Математика'].quantile(0.75)
iqr_math = q3_math - q1_math
print(f"\nQ1 по математике: {q1_math}")
print(f"Q3 по математике: {q3_math}")
print(f"IQR по математике: {iqr_math}")

# Вычисляем стандартное отклонение по каждому предмету
std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)
