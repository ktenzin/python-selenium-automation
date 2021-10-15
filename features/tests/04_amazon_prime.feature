# Created by keisharoberts at 10/8/21
Feature: Amazon Prime tests

  Scenario: Verify user sees correct amount of benefit boxes
    Given Open Amazon Prime
    Then Verify 7 benefit boxes are present