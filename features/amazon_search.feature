Feature: Search Amazon India from Google
  As a user
  I want to search for Amazon India on Google
  So that I can validate the official Amazon homepage

  Scenario: Open the official Amazon India homepage from Google search
    Given the user opens Google search
    When the user searches for "Amazon India"
    And the user clicks the official Amazon India result
    Then the Amazon India homepage should load
    And the page title should contain "Amazon.in"
    And the page URL should contain "amazon.in"
    And a screenshot should be captured
