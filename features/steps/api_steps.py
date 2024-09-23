import requests
from behave import *

@given('the API endpoint is "{base_url}"')
def step_impl_base_url_api(context, base_url):
    context.base_url = base_url

@when('I send a GET request to "{endpoint}"')
def step_impl_enpoint(context, endpoint):
    response = requests.get(context.base_url + endpoint)
    context.response = response

@when('I send a POST request to "{endpoint}" with the following data')
def step_impl_post_req(context, endpoint):
    data = {}
    for row in context.table:
        data[row['name']] = row['username']
        data[row['email']] = row['email']
    response = requests.post(context.base_url + endpoint, json=data)
    context.response = response

@then('the response code should be {expected_status:d}')
def step_impl_check_responce_body(context, expected_status):
    assert context.response.status_code == expected_status, f"Expected {expected_status}, but got {context.response.status_code}"

@then('the response should contain a list of users')
def step_impl_check_rb(context):
    users = context.response.json()
    assert isinstance(users, list), "Response is not a list"
    assert len(users) > 0, "User list is empty"

@then('the response should not contain a list of users')
def step_impl_fail_check(context):
    try:
        users = context.response.json()
        assert not isinstance(users, list), "Response incorrectly returned a list"
    except ValueError:
        # If the response is not a JSON response, this will catch it and pass
        pass

@then('the response should contain "{expected_value}"')
def step_impl_check_directly_rb(context, expected_value):
    response_text = context.response.text
    assert expected_value in response_text, f"'{expected_value}' not found in response"
