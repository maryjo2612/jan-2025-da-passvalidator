**Password Validator Project**

## **Team:**
- 👩‍💻 Maria Jose Calles — Validation Logic
- 👨‍💻 Franklin Sotolongo — User Interface & Testing

---

## 🧠 **Project Description**
This is a beginner-friendly password validation tool written in Python. It asks the user to input a password and checks if it meets security rules.

---

## 📋 **Validation Rules**
Your password must:
- ✨ Be between 8–16 characters
- 🔒 Include at least one special character: %$#^&*!@()
- 🔢 Include at least one number
- 🔠 Include at least one capital letter
- 🔤 Start with a lowercase letter
- 🚫 Not contain the phrase "pass"
- 🚫 Not contain the phrase "qwerty"
- 🚫 Not contain the sequence "123"

---

## 📚 **Learnings:**
 - ✅ Python Conditionals & Loops: Using if, else, and loops to implement logic.
 - ✅ Regular Expressions (Regex): Using regex to validate passwords against patterns.
 - ✅ Git & Version Control: Using branches, making commits, and handling merge conflicts.
 - ✅ Collaboration: Efficiently split tasks, handle pull requests, and merge code.

---

## **Challenges & Solutions**

### 🛠️ **Challenges:**
- **Branching Issues**: One team member working directly on the main branch and the other on a separate branch created some merge conflicts, leading to repeatedly pulling the latest code.
- **Test File Creation & Integration**: After creating a test file to test password functionality, integrating it with the main code posed challenges, as it wasn’t directly linked to the main logic. Ensuring the tests ran adequately without interfering with the main code was a learning curve.
- **Using .gitignore**: Learning the need for a .gitignore file to avoid committing unnecessary files like __pycache__, which are excessive in the repository.

### 💡 **Solutions**:
- **Branching & Git Workflow**: We created separate branches for different features, allowing both members to work simultaneously without affecting the main code. After finalizing the changes, we merged them back into the main branch.
- **Test File Integration**: We wrote unit tests for the password validation logic, ensuring that the test cases did not disrupt the main program’s functionality.
- **Utilizing .gitignore**: We created a .gitignore file to ensure that unnecessary files (such as Python bytecode) are not committed to the repository, keeping the project clean.

---

## 💻 **How to Run**
- Option 1 – Interactive Mode --- python3 main.py
- Option 2 – Run the Test File -- python3 test_passwords.py

---

🎉 **Conclusion:**
We successfully developed a password validation tool that checks for various security requirements. Throughout the project, we gained valuable skills in Python programming, Git workflow, and collaborative development. This experience allowed us to practice applying logic to real-world problems and learn about version control systems like Git and GitHub.

