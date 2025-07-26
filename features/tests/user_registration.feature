# Created by rekhagujalwar at 7/16/25

Feature:  User Registration

    @smoke
  Scenario: # Enter the user details to get registered
    Given Open the Registration page
    When Enter test Information in the registration form
    Then Verify that the correct information is present




