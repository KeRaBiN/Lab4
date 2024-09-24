import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


csv_file = 'employees.csv'


def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


def analyze_employee_data(filename):
    try:
        data = pd.read_csv(filename, parse_dates=['Дата народження'], dayfirst=True)
        print("Ok, файл CSV відкрито успішно.")
    except FileNotFoundError:
        print(f"Помилка: CSV файл '{filename}' не знайдений.")
        return
    except Exception as e:
        print(f"Помилка при відкритті CSV файлу: {e}")
        return


    gender_counts = data['Стать'].value_counts()
    print("\nКількість співробітників за статтю:")
    print(gender_counts)

    gender_counts.plot(kind='bar', title='Кількість співробітників за статтю', color=['blue', 'orange'])
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.show()


    data['Дата народження'] = pd.to_datetime(data['Дата народження'])
    data['Вік'] = data['Дата народження'].apply(calculate_age)

    bins = [-1, 18, 45, 70, float('inf')]
    labels = ['younger_18', '18-45', '45-70', 'older_70']
    data['Вікова категорія'] = pd.cut(data['Вік'], bins=bins, labels=labels)

    age_counts = data['Вікова категорія'].value_counts()
    print("\nКількість співробітників за віковими категоріями:")
    print(age_counts)

    age_counts.sort_index().plot(kind='bar', title='Кількість співробітників за віковими категоріями')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.show()


    gender_age_counts = data.groupby(['Вікова категорія', 'Стать']).size().unstack(fill_value=0)
    print("\nКількість співробітників за статтю в кожній віковій категорії:")
    print(gender_age_counts)

    gender_age_counts.plot(kind='bar', stacked=True, title='Кількість співробітників за статтю в кожній віковій категорії')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.show()


analyze_employee_data(csv_file)
