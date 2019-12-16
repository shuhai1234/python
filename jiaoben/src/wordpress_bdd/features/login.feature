Feature: Login

  @login
  Scenario: Success
    Given go to login page
    When login with admin admin
    Then redirect to dashboard page
    And display hello admin
