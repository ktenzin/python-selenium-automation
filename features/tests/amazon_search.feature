# Created by keisharoberts at 10/7/21
Feature: test cases for search functionality

# MULTIPLE TEST CASES RUN INDIVIDUALLY
#  Scenario: User can search for coffee on Amazon
#    Given Open Amazon page
#    When Input coffee into amazon search
#    And Click on amazon search icon
#    Then Verify "coffee" text is shown
#
#  Scenario: User can search for table on Amazon
#    Given Open Amazon page
#    When Input table into amazon search
#    And Click on amazon search icon
#    Then Verify "table" text is shown

#  Scenario: User can search for salt lamp on Amazon
#    Given Open Amazon page
#    When Input salt lamp into amazon search
#    And Click on amazon search icon
#    Then Verify "salt lamp" text is shown
#
#  Scenario: User can search for lipstick on Amazon
#    Given Open Amazon page
#    When Input lipstick into amazon search
#    And Click on amazon search icon
#    Then Verify "lipstick" text is shown


#  MULTIPLE TEST CASES IN A SCENARIO OUTLINE

  Scenario Outline: User can search for a product on Amazon
    Given Open Amazon page
    When Input <search_query> into amazon search
    And Click on amazon search icon
    Then Verify <result> text is shown
    Examples:
    |search_query  |result     |
    |table         |"table"    |
    |mug           |"mug"      |