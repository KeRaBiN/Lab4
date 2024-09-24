import pandas as pd
from datetime import datetime


csv_file = 'employees.csv'
xlsx_file = 'employees.xlsx'


def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


def create_xlsx_from_csv(csv_filename, xlsx_filename):
    try:
        data = pd.read_csv(csv_filename)
    except FileNotFoundError:
        print(f"Помилка: CSV файл '{csv_filename}' не знайдений.")
        return
    except Exception as e:
        print(f"Помилка при читанні CSV файлу: {e}")
        return

    try:
        data['Дата народження'] = pd.to_datetime(data['Дата народження'])
        data['Вік'] = data['Дата народження'].apply(calculate_age)

        with pd.ExcelWriter(xlsx_filename, engine='openpyxl') as writer:
            data.to_excel(writer, sheet_name='all', index=False)

            younger_18 = data[data['Вік'] < 18]
            between_18_45 = data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]
            between_45_70 = data[(data['Вік'] > 45) & (data['Вік'] <= 70)]
            older_70 = data[data['Вік'] > 70]

            younger_18[['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']].to_excel(writer, sheet_name='younger_18', index=False)
            between_18_45[['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']].to_excel(writer, sheet_name='18-45', index=False)
            between_45_70[['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']].to_excel(writer, sheet_name='45-70', index=False)
            older_70[['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']].to_excel(writer, sheet_name='older_70', index=False)

        print("Програма успішно завершила свою роботу")
    except Exception as e:
        print(f"Помилка при створенні XLSX файла: {e}")


create_xlsx_from_csv(csv_file, xlsx_file)
