import pandas as pd

data = {
    'Имя': ['Алексей', 'Мария', 'Иван', 'Ольга', 'Дмитрий', 'Анна', 'Сергей', 'Елена', 'Николай', 'Татьяна'],
    'Математика': [85, 78, 92, 74, 88, 95, 67, 80, 72, 90],
    'Физика': [78, 82, 88, 92, 74, 81, 79, 85, 80, 90],
    'Химия': [80, 85, 89, 76, 90, 92, 75, 84, 78, 93],
    'Биология': [90, 87, 85, 78, 92, 88, 80, 86, 82, 91],
    'История': [88, 84, 90, 85, 87, 89, 82, 83, 81, 86]
}

df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head())

average_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(average_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:", Q3_math)
print("IQR для оценок по математике:", IQR_math)

std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)