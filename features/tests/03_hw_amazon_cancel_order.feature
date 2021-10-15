# Created by keisharoberts at 10/7/21
Feature: Test Cancel Order in Help Search

  Scenario: User can search for Cancel Order in Help Search
    Given Open Amazon Help page
    When Input cancel order into Amazon search
    Then Verify cancel order search text is shown

