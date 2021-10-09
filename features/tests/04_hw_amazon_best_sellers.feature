# Created by keisharoberts at 10/8/21
Feature: Amazon Best Sellers tests
  # Create a test case that will open Amazon
  # BestSellers page and verify there are 5 links

  Scenario: Verify 5 links are present on Amazon Best Sellers page
    Given Open Amazon Best Sellers1
    Then Verify 5 menu Best Sellers menu links are present