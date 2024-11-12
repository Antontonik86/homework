import pandas as pd


print()     # Отступ


# Для установки Pandas вы можете использовать pip:
# pip install pandas

# Pandas — это мощная библиотека для анализа данных в Python,
# которая предоставляет структуры данных и функции для манипуляции и анализа данных.
# Она особенно полезна для работы с табличными данными, такими как CSV-файлы,
# базы данных и другие форматы.

# Для работы с Excel-файлами в Pandas, вам понадобится библиотека openpyxl или xlrd.
# Вы можете установить их с помощью pip:
# pip install pandas openpyxl xlrd


# ЧТЕНИЕ ДАННЫХ ИЗ EXCEL ФАЙЛА


# Путь к файлу
file_path = './Test.xlsx'

# Читаем данные из Excel-файла и загружает их в объект DataFrame.
data = pd.read_excel(file_path)

# Вывод первых пяти строк данных
print("Первые пять строк данных:")

# Метод head() возвращает первые пять строк DataFrame.
print(data.head())

# Пример фильтрации данных
# выбираем только тех, кто старше 30 лет

filtered_data = data[data['Возраст'] > 30]

# [data['Возраст'] > 30] - это условие создает серию булевых значений (True или False),
# где True соответствует строкам, в которых значение в столбце 'Возраст' больше 30.

# data[data['Возраст'] > 30] - это условие используется для фильтрации строк в DataFrame.
# Только те строки, для которых условие истинно (True), будут включены в новый DataFrame.

print("\nДанные для людей старше 30 лет:")
print(filtered_data)

# Пример группировки данных
# считаем количество людей каждого пола

grouped_data = data.groupby('Пол').size()

# Метод groupby используется для группировки данных по одному или нескольким столбцам.
# Метод size возвращает количество строк в каждой группе.

print("\nКоличество людей каждого пола:")
print(grouped_data)

# Пример сортировки данных
# сортируем данные по возрасту

sorted_data = data.sort_values(by='Возраст')

# Метод sort_values используется для сортировки строк в DataFrame по значениям в одном или нескольких столбцах.
# Параметр by указывает, по какому столбцу нужно сортировать данные.

print("\nДанные, отсортированные по возрасту:")
print(sorted_data)


# ЗАПИСЬ ДАННЫХ В EXCEL ФАЙЛ


# Создаем новый DataFrame с данными, которые хотим добавить
new_data = {
    'Фамилия': ['Иванов', 'Петров'],
    'Имя': ['Иван', 'Петр'],
    'Отчество': ['Иванович', 'Петрович'],
    'Возраст': [30, 35],
    'Пол': ['Мужской', 'Мужской']
}

# pd.DataFrame(new_data): Этот метод создает новый DataFrame из переданного словаря new_data
new_data = pd.DataFrame(new_data)

# Объединяем существующие данные с новыми данными

# pd.concat([existing_data, new_df], ignore_index=True): Этот метод объединяет два DataFrame по строкам.
# Параметр ignore_index=True указывает, что индексы в объединенном DataFrame
# будут сброшены и заменены новыми индексами, начиная с 0.
combined_data = pd.concat([data, new_data], ignore_index=True)

# Записываем объединенные данные обратно в существующий Excel-файл

# pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace'):
# Этот метод создает объект ExcelWriter, который используется для записи данных в Excel-файл.
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    combined_data.to_excel(writer, sheet_name='Лист1', index=False)

# ENGINE='OPENPYXL': Указывает, какую библиотеку использовать для записи данных
# MODE='A': Указывает режим записи. 'a' означает добавление данных к существующему файлу
# IF_SHEET_EXISTS='REPLACE': Указывает, что делать, если лист уже существует.
# 'REPLACE' означает, что существующий лист будет заменен новыми данными.
# combined_data.to_excel(writer, sheet_name='Sheet1', index=False):
# Этот метод записывает DataFrame combined_data в указанный лист (Sheet1) в Excel-файле.
# Параметр INDEX=FALSE указывает, что индексы строк не должны быть записаны в файл.

# Вместо 'REPLACE' можно использовать:
# IF_SHEET_EXISTS='OVERLAY' - параметр добавляет новые данные поверх существующих данных в листе.
# IF_SHEET_EXISTS='NEW' - параметр создает новый лист с уникальным именем, если лист с указанным именем уже существует.

# Создаем новый DataFrame с другой информацией
new_sheet_data = {
    'Столбец1': ['Значение1', 'Значение2'],
    'Столбец2': ['Значение3', 'Значение4']
}

new_sheet_df = pd.DataFrame(new_sheet_data)

# Записываем новый DataFrame в новый лист в том же Excel-файле
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    new_sheet_df.to_excel(writer, sheet_name='Лист2', index=False)



