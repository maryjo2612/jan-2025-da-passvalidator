
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