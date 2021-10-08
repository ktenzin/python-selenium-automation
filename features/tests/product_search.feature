# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Watches into search field
#    And Click on search icon
#    Then Product results for Watches are shown

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input coffee into Amazon search
    When Click on Amazon search icon
    Then Verify "coffee" text is shown


