# mitigram_test_project
A small pytest-bdd demo project which perform login and careers tests on mitigram.com 

## 1. Pre-requisites:
- Python and pytest installed. and environment variables are configured on your computer.
- This test project is developed and tested on a windows machine. So it is better to use a windows computer to perform a test run.

## 2. Installation: 
- Download or clone the code from repository.
- Required libraries as mentioned in requirements.txt file. Install them with the commmad `pip install -r requirements.txt`  

## 3. Execution:
- Run the following pytest command on the working directory
	`pytest tests/step_definitions/test_mitigram.py --alluredir ./allure-reports --junitxml=./reports/junitreport.xml`
	
## 4. Reports:
- Allure report is used to generate html reports based on pytest bdd test execution format. That means, the allure will capture the features, scenarios and steps that are been executed. As well as a screenshot is captured at the end of test execution and attached in the report. 
- To see the allure report in html format, install allure (https://allurereport.org/docs/gettingstarted-installation/), configure environment variable, then use the following command on the working directory:
	`allure serve ./allure-reports`
- This will generate report to an temporary directory, and give user a link to open web view of the report.
