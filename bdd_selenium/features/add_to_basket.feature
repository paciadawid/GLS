# Created by BRL062.krk at 5/22/2020
Feature: Add to basket

  Scenario: Add Printed Summer cloth
    When I search Printed Summer
    And I add Printed Summer to the basket
    Then total price should be smaller than 30
    And shipping price should be 2
