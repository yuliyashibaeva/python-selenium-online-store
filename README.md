# Selenium WebDriver Automation Project

This is a pet project to polish up my test automation skills 
using Python and Selenium WebDriver. As an object for automation 
I chose a demo online store: https://magento.softwaretestingboard.com/.

**NOTE:** Since I'm new in test automation and Python, comments and advice are very welcome.
Please be polite.

## 🛠️ Tech Stack
1. Programming language - `Python`
2. Testing framework - `Pytest`
3. Automation framework - `Selenium WebDriver`

## 🚀 How to run the tests
1. Clone the repository.
2. Install the dependencies from [the "requirements.txt" file](https://github.com/yuliyashibaeva/python-selenium-online-store/blob/main/requirements.txt).
3. Run the test in the console, for example, with the command:<br>
```shell
pytest -v .\tests\
```

## ✍️ Command line options
1. The tests can be run in Chrome or Firefox. Write a command with option 
`--browser=chrome` or `--browser=firefox` to choose a browser. 
The default browser is Chrome.
2. The tests can be run in a headless mode. Write a command with option 
`--headless`. The default value is `False`.

## 📝 Test Cases
Automated test cases in the text format are stored in [the "TestCases.md" file](https://github.com/yuliyashibaeva/python-selenium-online-store/blob/main/TestCases.md).