# Define the rules for the password Validation
Rules = [
 "✨ Contains 8-16 characters",
 "🔒 Contains one of the special characters: %$#^&*!@()",
 "🔢 Contains at least one number 0-9",
 "🔠 Contains at least one capital letter",
 "🔤 Starts with a lowercase letter",
 "🚫 Does not contain the phrase “pass” in any format",
 "🚫 Does not contain the phrase “qwerty” in any format",
 "🚫 Does not contain the phrase “123”",
]
def show_rules():
    print("\nPassword Validation Rules:")
    for rule in Rules:
        print(rule)

show_rules()