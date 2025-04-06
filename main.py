
# Password Validator Project
# Maria - Validation Logic | Franklin - User Interface

import re

#Password rules display to the user

rules = [
    "✨ Contains 8–16 characters",
    "🔒 Contains one of the special characters: %$#^&*!@()",
    "🔢 Contains at least one number 0–9",
    "🔠 Contains at least one capital letter",
    "🔤 Starts with a lowercase letter",
    "🚫 Does not contain the phrase 'pass'",
    "🚫 Does not contain the phrase 'qwerty'",
    "🚫 Does not contain the phrase '123'",  
]

#Show rules to the user
def show_rules():
    print("\nThe password must follow these rules: \n\t\t")
    for rule in rules:
        print(rule)

#Main validation logic
def validate_password(password):
    errors = []

    passlength_validated = validate_password_length(password)
    specialcharacters_validated = validate_special_characters(password)
    numbers_validated = validate_numbers(password)
    capitalletters_validated = validate_capital_letters(password)
    startlowercase_validated = validate_start_lowercase(password)
    no_pass_validated = validate_no_pass(password)
    no_qwerty_validated = validate_no_qwerty(password)
    no_numbers_validated = validate_no_numbers(password)

    if passlength_validated != 'Valid':
        errors.append(passlength_validated)
    if specialcharacters_validated != 'Valid':
        errors.append(specialcharacters_validated)
    if numbers_validated != 'Valid':
        errors.append(numbers_validated)
    if capitalletters_validated != 'Valid':
        errors.append(capitalletters_validated)
    if startlowercase_validated != 'Valid':
        errors.append(startlowercase_validated)
    if no_pass_validated != 'Valid':
        errors.append(no_pass_validated)
    if no_qwerty_validated != 'Valid':
        errors.append(no_qwerty_validated)
    if no_numbers_validated != 'Valid':
        errors.append(no_numbers_validated)

    return errors

# Validation rule for password length
def validate_password_length(password):
    if len(password) < 8 or len(password) > 16:
        return 'Password needs 8-16 characters'
    return 'Valid'

#Validation rule for special characters
def validate_special_characters(password):
    if not re.search(r'[%$#^&*!@()]', password):
        return "Password should contain one of the special characters: %$#^&*!@()"
    return 'Valid'

#Validation rule for numbers
def validate_numbers(password):
    if not re.search(r'[0-9]', password):
        return 'Password should contain at least one number 0-9'
    return 'Valid'

#Validation rule for capital letters
def validate_capital_letters(password):
    if not re.search(r'[A-Z]', password):
        return 'Password should contain at least one capital letter'
    return 'Valid'

#Validation rule for lowercase letters
def validate_start_lowercase(password):
    if not password[0].islower():
        return 'Password should start with a lowercase letter'
    return 'Valid'

#Validation rule for the phrase "pass"
def validate_no_pass(password):
    if "pass" in password.lower():
        return 'Password should not contain the phrase "pass" in any format'
    return 'Valid'

#Validation rule for the phrase "qwerty"
def validate_no_qwerty(password):
    if "qwerty" in password.lower():
        return 'Password should not contain the phrase "qwerty" in any format'
    return 'Valid'

#Validation rule for the phrase "123"
def validate_no_numbers(password):
    if "123" in password:
        return 'Password should not contain the phrase "123"'
    return 'Valid'

#This is to show feedback to the user if the password is valid or not

def validatepassword():
    while True:
            password = input("\nPlease enter a password that conforms to the above restrictions:\n\t\t")
            print(f"Your password is: {password}")

            violations = validate_password(password)
            
            if violations:
                print("\nThis password does not meet the following requirements:")
                for rule in violations:
                    print(f'-{rule}')
            else:
                print("\n🎉Success! Your Password meets all the requirements.")
                break


if __name__ == "__main__":
    show_rules()
    validatepassword()