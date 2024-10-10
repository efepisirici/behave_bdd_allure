import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import re
from behave.model_core import Status

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Start a Chrome session for each scenario
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    context.driver.set_page_load_timeout(30)  # Add a timeout to avoid connection issues
    context.driver.maximize_window()
    context.allure_report_dir = os.path.join("features", "reports")
    os.makedirs(context.allure_report_dir, exist_ok=True)
    print(f"Initialized WebDriver for scenario: {scenario.name}")

def after_step(context, step):
    # Check if the scenario has an @api tag, and if so, do not take a screenshot
    if 'api' not in context.tags:
        if step.status == Status.failed or step.status == Status.passed:
            screenshot_name = sanitize_filename(f"{step.name}_{step.status.name.lower()}.png")
            screenshot_path = os.path.join(context.allure_report_dir, screenshot_name)
            try:
                context.driver.save_screenshot(screenshot_path)
                attach_screenshot_to_allure(screenshot_path)
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

def after_scenario(context, scenario):
    # Kill Chrome session after each scenario
    if context.driver:
        context.driver.quit()
    print(f"Closed WebDriver for scenario: {scenario.name}")

def attach_screenshot_to_allure(filepath):
    with open(filepath, 'rb') as image_file:
        allure.attach(image_file.read(), name=os.path.basename(filepath), attachment_type=allure.attachment_type.PNG)
