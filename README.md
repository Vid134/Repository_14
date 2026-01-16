 Zen Portal Automation Testing (Python + Playwright + Pytest)

This project automates the Login and Logout workflow of the Zen Portal using **Python**, **Microsoft Playwright**, and **Pytest**.  
It follows the **Page Object Model (POM)** structure and generates **HTML test reports** using `pytest-html`.

---

## 📌 Features & Requirements Implemented

The automation framework fulfills the following requirements:

1. **Usage of POM (Page Object Model)**
2. **Usage of Explicit Waits**
3. **Login with valid credentials**
4. **Login with invalid credentials (negative test case)**
5. **Logout functionality validation**
6. **Username & Password input box validation**
7. **Submit button validation**
8. **Usage of Python OOPS principles**
9. **Usage of Python exception handling**
10. **HTML Test Report generation using Pytest**

---

---

## ⚙️ Technologies & Tools Used

| Component | Tool |
|---|---|
| Language | Python 3.x |
| Automation | Microsoft Playwright |
| Test Framework | Pytest |
| Design Pattern | Page Object Model (POM) |
| Reporting | pytest-html |
| Synchronization | Playwright explicit waits |
| IDE (optional) | PyCharm / VS Code |

---

## 🛠️ Installation & Setup Instructions

### 1. Clone the Repository
```sh
git clone <repo-url>
cd <project-root>
🧱 POM (Page Object Model) Implementation
login_page.py contains all login page elements & methods.
dashboard_page.py contains dashboard & logout methods.
Tests import & use these page classes → ensuring maintainability.

Test Case and Description:

1.Successful Login-Valid creds â†’ Login should pass

2.Unsuccessful Login-Invalid creds â†’ Error message / failure

3.Validate Username/Password Fields-Input fields should be visible & enabled

4.Validate Submit Button-Submit button visible, enabled, clickable

5.Logout Functionality-Logout should redirect to login page



🧱 Python OOPS Usage
Classes for page objects
Methods for actions
Instances created inside tests


🛡️ Exception Handling
Try/Except blocks implemented inside POM for stability:

🏁 Conclusion:
This project successfully demonstrates the end-to-end automation of the Zen Portal using Python, 
Playwright, and Pytest, following clean coding and testing standards. By implementing the Page Object Model (POM)
, explicit waits, structured test cases, and exception handling, the framework achieves
 maintainability, scalability, and reliability.
All required test scenarios—including successful login, unsuccessful login, input field validation, 
submit button validation, and logout functionality—were automated and executed. 
Test results were captured using Pytest HTML reporting, ensuring clear visibility of execution outcomes.
Overall, this automation framework showcases practical skills in UI testing, modern tooling usage, 
and software test development best practices.

