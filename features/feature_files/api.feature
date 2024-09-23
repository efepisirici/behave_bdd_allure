@pet_store_api
Feature: Test the User API

  @positive @api @severity.blocker
  Scenario: Get all users
    Given the API endpoint is "https://jsonplaceholder.typicode.com"
    When I send a GET request to "/users"
    Then the response code should be 200
    And the response should contain a list of users
  
  @negative @api @severity.critical
  Scenario: Check Wrong Endpoint
    Given the API endpoint is "https://jsonplaceholder.typicode.com"
    When I send a GET request to "/user"
    Then the response code should be 404

  @positive @api @severity.normal
  Scenario: Create a new user
    Given the API endpoint is "https://jsonplaceholder.typicode.com"
    When I send a POST request to "/users" with the following data
      | name       | username    | email           |
      | John Doe   | johndoe     | johndoe@email.com |
    Then the response code should be 201
    And the response should contain "John Doe"
