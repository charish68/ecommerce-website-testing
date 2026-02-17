![CI](https://github.com/charish68/ecommerce-website-testing/actions/workflows/automation.yml/badge.svg)

🛒 E-Commerce Website Testing Project
📌 Project Overview

Manual and Automation testing of an E-Commerce website to validate core functionalities including registration, login, cart, checkout, and subscription.

🎯 Objective

To design, document, and execute test cases while identifying defects and improving application quality.

🧪 Testing Types Covered

Functional Testing

UI Testing

Validation Testing

Negative Testing

📂 Project Structure

Test Plan

Test Scenarios

Test Cases

Bug Reports

RTM

🤖 Automation Framework

This project includes Selenium + Pytest based automation testing.

🔧 Tech Stack:

Python

Selenium WebDriver

Pytest

WebDriver Manager

▶ How to Run Tests
pip install -r requirements.txt
pytest
## 📊 Reporting

This project supports:
- Pytest HTML Reports
- Allure Reporting Dashboard

To generate Allure report locally:

```bash
pytest --alluredir=allure-results
allure serve allure-results
## 🐳 Run with Docker

Build image:

```bash
docker build -t automation-framework .
