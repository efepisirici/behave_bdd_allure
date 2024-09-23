from selenium import webdriver
from behave.model_core import Status

RETRY_COUNT = 2

def before_all(context):
    # Setup code before all scenarios
    options = webdriver.ChromeOptions()
    # start browser maximized
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=options)
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