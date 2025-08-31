# 🧪 Python Selenium Framework

This repository contains **three end-to-end Selenium-based automation frameworks** built with **Python, Pytest, and Page Object Model (POM)**.  
Each project demonstrates automation of different sample applications, complete with test data, reporting, and reusable utilities.

---
## 👤 Author

Abdul-ur-Rehman

---

## 📂 Repository Structure
```
Python-Selenium-Framework/
├── Project1_ProtoCommerce_PSF/ # Automation for ProtoCommerce app
│ ├── pageObjects/ # Page Object Model classes
│ ├── reports/ # Test reports
│ ├── testData/ # Test data (Python & Excel)
│ ├── tests/ # Automated test cases (pytest)
│ └── utilities/ # Base classes, logs, configs
│
├── Project2_GreenKart_PSF/ # Automation for GreenKart app
│ ├── pageObjects/
│ ├── reports/
│ ├── testData/
│ ├── tests/
│ └── utilities/
│
└── Project3_LightninesStudio_PSF/ # Automation for Lightnines Studio app
├── pageObjects/
├── reports/
├── testData/
├── tests/
└── utilities/

```


---

## 🚀 Features

- **Page Object Model (POM):** Separation of test logic from UI locators.  
- **Data-Driven Testing:** Using Python classes and Excel files for input data.  
- **Reusable Base Classes:** For logging, driver setup, and utilities.  
- **Pytest Integration:** Simplified test execution and reporting.  
- **HTML Reports:** Auto-generated under the `reports/` directory.  
- **Scalable Structure:** Separate frameworks for each application.

---

## 🛠️ Prerequisites

- Python **3.8+**
- Google Chrome / Firefox
- ChromeDriver / GeckoDriver (matching browser version)

---

## 📦 Installation

Clone the repository:

```
git clone https://github.com/Abdul-ur-Rehman/Python-Selenium-Framework.git
cd Python-Selenium-Framework
```

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

Install dependencies:
```
pip install -r requirements.txt
```

## ▶️ Running Tests

Navigate to any project folder and run tests using pytest:
```
cd Project1_ProtoCommerce_PSF
pytest -v -s tests/
```
Run a specific test file:
```
pytest -v -s tests/test_e2eTestCase-ProtoCommerce.py
```
Generate an HTML report:
```
pytest --html=reports/report.html --self-contained-html
```

## 📊 Reporting & Logs

- Test execution reports are saved in the reports/ folder.

- Log files are generated inside the utilities/logfile/ directory.

- Reports include test results, screenshots (if configured), and execution details.

## ✅ Automated Test Cases
### Project1: ProtoCommerce

- Filling and submitting the homepage form with data-driven values.

- Adding products to cart and verifying total price.

- End-to-end checkout flow.

### Project2: GreenKart

- Searching and selecting vegetables/fruits.

- Adding items to cart and applying discount codes.

- Validating checkout and price calculation.

### Project3: Lightnines Studio

- Filling out homepage form fields.

- Uploading a company logo.

- Verifying successful submission.

## 🔧 Utilities

- BaseClass.py → Handles WebDriver setup, teardown, and reusable fixtures.

- logfile/ → Stores framework execution logs.

- conftest.py → Central pytest configuration for fixtures and hooks.

##📌 Best Practices Followed

- Page Object Model (POM) for maintainability.

- Data-driven testing approach.

- Structured logging and reporting.

- Reusable utility classes.

- Configurable test setup (drivers, environment).
