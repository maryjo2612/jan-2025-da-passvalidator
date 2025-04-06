from main import validate_password, show_rules

# Show the password rules to the user
show_rules()

# Mixed list of test passwords
test_passwords = [
    "Qwerty!2024",       # FAIL
    "greatDay7!",        # PASS
    "12345678",          # FAIL 
    "validTest1$",       # PASS 
    "StrongPass",        # FAIL
    "frankL1n@2025",     # PASS 
    "pass1234@",         # FAIL
    "sunRise8&Go",       # PASS 
    "HelloWorld123!",    # FAIL
    "devWork4^"          # PASS 
]

# Run validation on each password
for pwd in test_passwords:
    print(f"\n🔍 Testing: {pwd}")
    result = validate_password(pwd)
    if result:
        print("❌ Violations:")
        for r in result:
            print(f"- {r}")
    else:
        print("✅ Valid password 🎉")

