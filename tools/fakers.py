import time
import random

def get_random_email() -> str:
    return f'test.{time.time()}@example.com'

# Списки имен и фамилий
names = ["Алексей", "Мария", "Иван", "Елена", "Дмитрий", "Ольга"]
surnames = ["Смирнов", "Иванова", "Петров", "Кузнецова", "Соколов", "Попова"]
middlenames = ["Александрович", "Алексеевич", "Анатольевич", "Борисович",
    "Валерьевич", "Васильевич"]

def get_random_username() -> str:
    random_name = random.choice(names)
    return random_name

def get_random_surname() -> str:
    random_surname = random.choice(surnames)
    return random_surname

def get_random_middle_name() -> str:
    random_middle_name = random.choice(middlenames)
    return random_middle_name