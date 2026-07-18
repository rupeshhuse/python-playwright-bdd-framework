Feature: Validate Amazon India upper navigation links
  As a user
  I want to verify the visible upper navigation links on Amazon.in
  So that I can ensure the navigation grid remains clickable and navigable

  Scenario: Validate the visible upper navigation links on Amazon.in
    Given the user opens the Amazon India homepage
    When the user collects the visible upper navigation links
    Then each visible link with a valid destination should be clickable
    And each clicked link should navigate to a valid Amazon destination
    And a screenshot should be captured for the navigation validation
