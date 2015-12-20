Feature: API Service

    Scenario: As an API client I want to list the stores
        Given I access the url "/services/stores/"
        Then I get status code 401

        Given I authenticates as "any_user" / "any_password"
        And I access the url "/services/stores/"
        Then I get status code 401

        Given I authenticates as "my_user" / "my_password"
        And I access the url "/services/stores/"
        Then I get status code 200


    Scenario: As an api client I want to list all the articles
        Given I authenticates as "any_user" / "any_password"
        And I access the url "/services/articles/"
        Then I get status code 401
        
        Given I authenticates as "my_user" / "my_password"
        And I access the url "/services/articles/stores/parameter/"
        Then I get status code 400

        Given I authenticates as "my_user" / "my_password"
        And I access the url "/services/articles/stores/parameter/"
        Then I get error message "Bad Request"

        Given I authenticates as "my_user" / "my_password"
        And I access the url "/services/articles/stores/1/"
        Then I get status code 200

        Given I authenticates as "my_user" / "my_password"
        And I access the url "/services/articles/stores/999/"
        Then I get status code 404

        Given I authenticates as "my_user" / "my_password"
        And I access the url "/services/articles/stores/999/"
        Then I get error message "Record not Found"
