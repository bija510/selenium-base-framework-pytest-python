# SeleniumBase Project Setup

## 1. Setup a New Project
1. Create a new project:
    - File -> New Project
    - Give your desired project name.

2. Open Command Prompt as Administrator and navigate to your project path:
    ```bash
    cd <project-path>
    ```

3. Install `seleniumbase` via pip:
    ```bash
    pip3 install seleniumbase
    ```

4. Verify installation by typing:
    ```bash
    sbase
    ```

## 2. Download Web Drivers
To install the necessary drivers, run the following commands:

- Install the latest Chrome driver:
    ```bash
    sbase install chromedriver latest
    ```

## 3. Project Structure and Sample Test Cases
- By default, CSS Selectors are used for finding page elements.

- Create project structure and sample test cases:
    ```bash
    sbase mkdir ui_tests
    ```

This will create the project structure and add some sample test cases.

## 4. Running Tests
To run tests, follow these steps:

1. Navigate to the `ui_tests` directory (use `Tab` for autocompletion):
    ```bash
    cd ui_tests
    ```

2. Run the test using `pytest`:
    ```bash
    pytest TestCases/my_first_test.py
    ```

3. If using `Tab` for autocompletion:
    ```bash
    pytest TestCases/Test_01_Login.py
    ```

4. To run the tests on a specific browser (e.g., Chrome):
    ```bash
    pytest my_first_test.py --browser=chrome
    ```

5. Run on Firefox:
    ```bash
    nosetests test_suite.py --browser=firefox
    ```

By default, Chrome is the selected browser unless specified otherwise.

## 5. Running Specific Methods
To run specific methods in the test, use:
```bash
pytest LoginTest.py::LoginTest::test_login
```
## 6. Running Tests in Headless Mode
To run tests in headless mode, simply add the `--headless` option to the `pytest` command:
```bash
pytest Test_01_Login.py --headless
```

## 7. Handling Test Failures
When a test fails, SeleniumBase automatically performs the following actions:

- **Screenshot**: A screenshot is captured of the failed test.
- **Logs**: Logs of the test run are generated.
- **HTML Page Source**: The HTML page source at the time of failure is saved.

These files will be stored in the `latest_logs` folder for easy access and debugging.
## 8. Avoiding Flaky Tests
SeleniumBase methods automatically wait for page elements to finish loading before interacting with them (up to a timeout limit of 6 seconds). This means you no longer need to use random `time.sleep()` statements in your scripts, reducing flaky tests and improving test reliability.

## 9. Generating Reports
To generate a test report, use the following command:

```bash
pytest Test_01_Login.py --dashboard -rs --headless
```
