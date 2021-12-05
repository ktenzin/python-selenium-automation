# Created by keisharoberts at 10/7/21
Feature: Test Amazon Cart is empty

  Scenario: Amazon Cart is empty
    Given Open Amazon page
    When Click Amazon cart
    Then Verify Amazon Cart is empty

