# SmartPad Customer Feedback - Test Automation Project

This repository contains the test automation framework and manual test cases for the SmartPad Customer Feedback form. The project aims to ensure the functionality, usability, and stability of the feedback submission process.

## Table of Contents

- [Overall Test Strategy](#overall-test-strategy)
- [Key Product Flows Tested](#key-product-flows-tested)
- [Test Cases](#test-cases)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Run Tests](#how-to-run-tests)
- [Reporting](#reporting)

---

## Overall Test Strategy

The primary goal of this testing effort is to validate the core functionality, usability, and stability of the SmartPad Customer Feedback form. We employ a hybrid testing approach:

* **Automated Testing (Selenium with Pytest):** Used for efficient regression testing, covering critical functional flows and input validations. This ensures that new changes do not introduce regressions in existing functionality.
* **Manual Exploratory Testing:** Performed to uncover edge cases, usability issues, and visual inconsistencies that might be missed by automated scripts, especially across different devices and browsers.

The test effort focuses on the following aspects:

* **Functional Testing:** Verifying that all features of the feedback form work as expected.
* **Boundary Value Analysis:** Testing input fields with boundary values (e.g., minimum/maximum lengths).
* **Input Validation:** Ensuring proper error handling for invalid or missing data.
* **UI/UX Checks:** Confirming the visual correctness and user-friendliness of the interface.

## Key Product Flows Tested

The automation framework primarily focuses on the following critical user flows:

* **Filling out and submitting the feedback form:** Verifying the end-to-end submission process.
* **Form validation and error handling for required fields:** Ensuring users are prompted for mandatory information.
* **Input sanitization:** Testing with various types of invalid inputs (e.g., invalid email formats, excessively long comments) to ensure the system handles them gracefully.
* **Verifying the presence and content of the success message:** Confirming positive feedback is acknowledged correctly.

Manual testing covers aspects like:

* Usability across different devices (mobile, tablet, desktop) and browsers (Chrome, Firefox, Edge, Safari).
* Edge cases and exploratory scenarios.

## Test Cases

Below is a summary of the key test cases covered in this project. Automated tests are identified where applicable, while others might be covered by manual testing.

| ID    | Test Case Description              | Expected Result                             | Automation Status |
| :---- | :--------------------------------- | :------------------------------------------ | :---------------- |
| TC01  | Submit valid feedback form         | Form submitted successfully with thank you message | Automated         |
| TC02  | Submit empty form                  | Error messages for required fields          | Automated         |
| TC03  | Invalid email input                | Error message for email field               | Automated         |
| TC04  | Skip rating selection              | Form should not submit without rating       | Automated         |
| TC05  | Very long comment                  | Form accepts and processes long text        | Manual / Automated (boundary) |
| TC06  | Special characters in comment      | No crash or misbehavior                     | Manual / Automated (input sanitization) |
| TC07  | Responsive layout on mobile        | Proper layout and alignment                 | Manual            |


## Tech Stack

* **Programming Language**: Python
* **Test Framework**: pytest 
* **Automation Tool**: Selenium WebDriver
* **Reporting**: pytest-html
* **Browser Compatibility**: Microsoft Edge, Google Chrome, Mozilla Firefox, Safari
* **CI/CD Integration**: GitHub Actions

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/imranc07/Smartpad-Customer-Feedback.git](https://github.com/imranc07/Smartpad-Customer-Feedback.git) 
    cd "Smartpad Customer feedback"
    ```

2.  **Create a Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate   # For Windows, use `env\Scripts\activate`
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure your `requirements.txt` file is present in the root directory. A basic `requirements.txt` should contain:
    ```
    selenium
    pytest
    webdriver-manager
    pytest-html
    ```
    )

4.  **Set Up Environment Variables**:
    * Create a `.env` file in the root directory to store sensitive information such as login credentials and URLs. Example:
        ```
        BASE_URL=[https://example.com](https://example.com) # Replace with your application's base URL
        USER_EMAIL=test@example.com
        USER_PASSWORD=yourpassword
        ```

## Running Tests

To execute tests, use the following commands:

1.  **Run All Tests**:
    ```bash
    pytest TestScripts/
    ```

2.  **Generate HTML Report**:
    ```bash
    pytest --html=Reports/test_reports.html 
    ```

3.  **Run Tests by Marker** (e.g., only specific tests):
    
    ```bash
    pytest TestScripts/test_FeedbackPage.py::test_TC01_valid_submission
    ```
    * **If you introduce markers (e.g., `@pytest.mark.smoke`)**:
        ```bash
        pytest -m smoke TestScripts/
        ```
4.  **Headless Browser Execution**:
    * You can set up tests to run in Headless mode directly in your test script (e.g., by adding ChromeOptions or FirefoxOptions to your WebDriver initialization in your fixture).

## Reporting

Pytest provides a summary of test execution in the console. For more detailed and visually appealing reports, you can generate an HTML report using the `pytest-html` plugin.

To generate an HTML report:

    ```bash
    pytest --html=Reports/test_reports.html
    ```

## Project Structure

```
The project follows a standard Page Object Model (POM) structure for better maintainability and readability.

Smartpad Customer feedback/
│
├── PageObjects/             # Contains Page Object Models for Smartpad Customer Feedback application
│   └── FeedbackPage.py      # Handles methods and elements for FeedbackPage
│
├── Reports/                 # Contains HTML reports
│   ├── test_report.html     # HTML reports generated by pytest
│   
├── TestData/                # Stores test data for the test cases
│   └── data.py              # Contains reusable test data
│
├── TestLocators/            # Stores locators for web elements
│   └── locators.py          # Contains locators for all web elements used in the tests
│
├── TestScripts/             # Contains all test cases
│   └── test_HomePage.py     # Test cases for FeedbackPage
│
├── requirements.txt         # Lists project dependencies
│
└── README.md                # Project documentation
```
