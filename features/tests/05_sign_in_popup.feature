# Created by keisharoberts at 10/9/21
Feature: Amazon Sign In tests

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens