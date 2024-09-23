from selenium import webdriver
from behave.model_core import Status

RETRY_COUNT = 2

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    context.driver.maximize_window()
    context.allure_report_dir = "features/reports"
    print("Initialized WebDriver and other global settings before all tests.")
    pass

def after_all(context):
    # Teardown code after all scenarios
    context.driver.quit()
    print("Closed WebDriver and cleaned up after all tests.")

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    pass
   #  if scenario.status == Status.failed and getattr(context, scenario.scenario_retries, 0) < RETRY_COUNT:
   #      print(f"Retrying scenario '{scenario.name}' ({context.scenario_retries + 1}/{RETRY_COUNT}) due to failure.")
   #      context.scenario_retries += 1
   #     scenario.clear_steps()
   #     context.driver.quit()
   #      context.failed = True  # Mark to retry
   #  elif scenario.status == Status.failed:
   #      print(f"Scenario '{scenario.name}' failed after {RETRY_COUNT} retries.")
   # else:
   #      context.failed = False  # Reset retry status