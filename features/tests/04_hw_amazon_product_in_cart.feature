# Created by keisharoberts at 10/8/21
Feature: My Amazon Cart tests
  # Create your own test case to add any product
  # you want into the cart, and make sure it’s
  # there (check for the number of items in the
  # cart OR open the cart and verify it’s there,
  # up to you!)

  Scenario: Verify Product is added to Amazon Cart
    Given Open Amazon product page 1
    When Click add to cart button
    Then Verify 1 item is in cart
