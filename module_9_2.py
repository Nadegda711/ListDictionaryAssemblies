first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Сборка длин строк из first_strings с длиной не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Сборка пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Сборка словаря, где ключ-значение: строка-длина строки, только при чётной длине
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Результаты
print("First Result:", first_result)
print("Second Result:", second_result)
print("Third Result:", third_result)



