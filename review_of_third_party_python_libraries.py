import requests

"""Requests
requests - это библиотека для отправки HTTP - запросов и взаимодействия с веб - серверами.Основные возможности включают:
Отправку GET -, POST -, PUT -, DELETE - и других типов запросов. Работу с заголовками, параметрами и данными запросов.
Обработку ответов от сервера, включая статус,коды и содержимое ответа"""


response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Данные успешно получены:')
    print(response.json())   # Выводим данные в формате JSON
else:
    print('Ошибка при получении данных:', response.status_code)



import pandas as pd

"""pandas - это библиотека для анализа и обработки данных.Основные возможности включают:
Создание и манипуляцию структурами данных(DataFrame, Series).Чтение и запись данных из различных форматов
(CSV, Excel, JSON).Фильтрация, сортировка и группировка данных.Объединение и слияние данных."""

# Series - одномерный массив с метками (индексами)

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

# DataFrame - двумерная структура данных

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)

# Запись данных в CSV
df.to_csv('output.csv', index=False)

# Чтение данных из CSV
df = pd.read_csv('output.csv')
print(df.head())

# Фильтрация

filtered_df = df[df['Age'] > 30]
print(filtered_df)


import matplotlib.pyplot as plt
import numpy as np

"""Matplotlib - это библиотека для создания статических, анимированных и интерактивных визуализаций в Python.Основные
возможности включают:
Создание различных типов графиков(линейных, столбчатых, круговых и т.д.). Настройка графиков(заголовки, метки, легенды)
Сохранение графиков в различных форматах(PNG, PDF, SVG)"""


# Линейный график

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("График синуса")
plt.xlabel("X")
plt.ylabel("sin(X)")
plt.grid(True)
plt.show()

# Столбчатая диаграмма

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)
plt.title('Столбчатая диаграмма')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()

# Гистограмма

data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.7)
plt.title('Гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()

# График рассеяния

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title('График рассеяния')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



