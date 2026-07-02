Feature: User login
  As a user
  I want to log in to the application
  So that I can access the home page

  Scenario: Valid login
    Given the user opens the login page
    When the user enters valid credentials
    And the user clicks the login button
    Then the user should be redirected to the inventory page
