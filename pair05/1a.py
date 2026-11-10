def minimum_length(password):
    if len(password) >= 8:
        return True
    else:
        return False

def digital(password):
    if any(char.isdigit() for char in password):
        return True
    else:
        return False

def upper_letter(password):
    if any(char.isupper() for char in password):
        return True
    else:
        return False

def lower_letter(password):
    if any(char.islower() for char in password):
        return True
    else:
        return False

def special_character(password):
    if any(not char.isalnum() for char in password):
        return True
    else:
        return False

def validate_password(password):
    errors = []
    
    if not minimum_length(password):
        errors.append("довжина менше 8 символів")
    if not digital(password):
        errors.append("немає хоча б однієї цифри")
    if not upper_letter(password):
        errors.append("немає великої літери")
    if not lower_letter(password):
        errors.append("немає малої літери")
    if not special_character(password):
        errors.append("немає спеціального символу")

    if len(errors) == 0:
        return "Пароль надійний"
    else:
        return "Пароль не відповідає вимогам. \nНе виконано: " + ", ".join(errors)

def main():
    password = input("Введіть пароль: ")
    print(validate_password(password))

main()