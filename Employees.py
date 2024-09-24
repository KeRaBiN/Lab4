import csv
from faker import Faker
import random

csv_file = 'employees.csv'

fake = Faker('uk_UA')

male_patronymics = [
    'Олександрович', 'Іванович', 'Васильович', 'Миколайович', 'Петрович',
    'Андрійович', 'Володимирович', 'Сергійович', 'Михайлович', 'Дмитрович',
    'Юрійович', 'Богданович', 'Степанович', 'Вікторович', 'Павлович',
    'Романович', 'Олегович', 'Тарасович', 'Євгенович', 'Георгійович'
]

female_patronymics = [
    'Олександрівна', 'Іванівна', 'Василівна', 'Миколаївна', 'Петрівна',
    'Андріївна', 'Володимирівна', 'Сергіївна', 'Михайлівна', 'Дмитрівна',
    'Юріївна', 'Богданівна', 'Степанівна', 'Вікторівна', 'Павлівна',
    'Романівна', 'Олегівна', 'Тарасівна', 'Євгенівна', 'Георгіївна'
]


def generate_person_data():
    gender = random.choices(['male', 'female'], weights=[0.6, 0.4])[0]

    if gender == 'male':
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        patronymic = random.choice(male_patronymics)
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
        patronymic = random.choice(female_patronymics)

    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, patronymic, 'Чоловіча' if gender == 'male' else 'Жіноча',
            birth_date, position, city, address, phone, email]


def create_csv(filename, num_records):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження',
                         'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

        for _ in range(num_records):
            writer.writerow(generate_person_data())


create_csv(csv_file, 2000)
