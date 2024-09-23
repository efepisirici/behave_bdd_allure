import allure
from behave import given, when, then, use_step_matcher
from features.pages.login_page import LoginPage

@given('I am on the login page "{url}"')
@allure.step("User navigates to login page {url}")
def step_given_on_login_page(context, url):
    # context.driver = webdriver.Chrome()
    context.driver.get(url)
    context.login_page = LoginPage(context.driver)

@when('I enter a valid username "{username}" and password "{password}"')
@allure.step('User can enter username - "{username}" and password - "{password}"')
def step_when_enter_credentials(context,username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('I click the login button')
@allure.step('User can can click on login button')
def step_when_click_login(context):
    context.login_page.click_submit()

@then('I should be redirected to the dashboard page')
@allure.step('User login successfully and can see home page')
def step_then_redirected_to_dashboard(context):
    # Here you would include an assertion to check that the redirection was successful
    assert "katalon" in context.driver.current_url
    context.driver.quit()


@then("Verify validation message displayed")
@allure.step("Verifying validation message is displayed")
def step_impl(context):
    assert context.login_page.validation_msg_displayed() is True, "Validation message is displayed as expected"