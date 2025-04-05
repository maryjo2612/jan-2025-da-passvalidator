from main import validate_password

test_passwords = [
    "pass123",
    "Qweerty2024!",
    "123abcABC",
    "aGood1Password!",
    "validPass12!"

]

for test in test_passwords:
    print (f'\n🔍Testing password: {test}')
    violations = validate_password(test)
    if violations:
        print("❌Violations found:")
        for rule in violations:
            print(f"- {rule}")
    else:
        print("✅No violations found. Password is valid.")
        # The test cases above are designed to check the password validation function.")
