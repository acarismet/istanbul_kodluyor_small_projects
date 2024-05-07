# Automated Tests for Sauce Labs Login Page with Python-Selenium

This repository contains Python code for automated tests of the login functionality on Sauce Labs sample login page [saucedemo](https://www.saucedemo.com/).

## Dependencies

This script requires the following Python libraries:

- selenium
- time

You can install them using pip:

```bash
pip install selenium
```

<br>

> <br> **Note:** This script also requires the ChromeDriver to be installed and configured in your system PATH environment variable for Chrome browser automation. You can download it from the official ChromeDriver download.
> <br>

## Functionality

This script defines a class HWSelenium with four test methods:

1. `invalid_login_without_input()`: Attempts to login without username and password, verifies if the expected error message for missing username is displayed.
2. `invalid_login_without_pw()`: Enters a username but leaves the password field blank, verifies if the expected error message for missing password is displayed.
3. `invalid_login_by_blocking_user()`: Enters a locked username `("locked_out_user")` with password, verifies if the expected error message for locked user is displayed.
4. `valid_login_checking_prod_amount()`: Logs in with a valid username `("standard_user")` and password `("secret_sauce")`, retrieves the number of product cards displayed on the inventory page, and verifies if it matches the expected count (6).

## Running the Tests

Clone this repository or download the code.
Install the required libraries (pip install selenium).

### Additional Notes

- The script uses explicit waits (WebDriverWait) with expected conditions to ensure elements are loaded before interacting with them.
- The script uses basic assertions (printing test results) for simplicity. You can integrate a testing framework like unittest for more robust assertions and reporting.
- This is a basic example showcasing some functionalities of Selenium for web automation testing.
- You can extend this script to include additional test cases for different login scenarios and functionalities of the Sauce Labs login application.
