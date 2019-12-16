@create_post
Feature: CreatePost

  Scenario: Success
    Given go to login page
    When login with admin admin
    And go to create post page
    And create a post
    Then verify post title
