
# The Mini project was Devided into two Parts: Maria is working on the passwrord validation logic and I am working on the user interface.
# The code below is the user interface for the password validation project.
# The code is designed to prompt the user for a password and check if it meets certain criteria.



# Importing the regular expression module to use for pattern matching in password validation.
import re


# Define a list called 'rules' that holds each password requirement, this was provided on the assigment documentation.
# Each rule is represented as a string and we used emojis to make it fun and easy to understand.
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

#This function prints the list of rules to the screen for the user to see.
#we are using the for loop to go through each rules one at a time and print it.
#We are using \n to create a new line after each rule and \t\t to create a tab space before each rule.

def show_rules():
    print("\nThe password must follow these rules: \n\t\t")
    for rule in rules:
        print(rule)

#This is what the user will see first before entering the password.
show_rules()

#Ask the user to enter a password and store it in the cariable called "password"
password = input("\nPlease enter a password that conforms to the above restrictions:\n\t\t")

#Print the password back to the user so they can see what they entered.
#This is for testing purposes while the logic is being developed. we will replace it with a validation funtion. 
#validate_passord(password)
print(f"Your password is: {password}")


# This is a placegolder for the password validation function.
# This function will be replace once the logic function is deloveloped and the validation function is defined.
# For testing purposes, the function will pretend the password is always valid

def validate_password(password):
    return []




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
        return 'Psssword should start with a lowercase letter'
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


#Use this validation fuction to check if the password meets the requirements.
violations = validate_password(password)

#Password Validation Logic will be  added here
    
#This is to show feedback to the user if the password is valid or not

if violations:
    print("\nThis password does not meet the following requirements:")
    for rule in violations:
        print(f'-{rule}')
else:
    print("\n🎉Success! Your Password meets all the requirements.")

