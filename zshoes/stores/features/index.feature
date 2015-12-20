Feature: Admin Site

    Scenario: Home Page
        Given I access the url "/"
        Then I see the header "SuperZapatos Administration system"
        Then I see the button "Go to Stores »"
    Scenario: Stores Page
        Given I access the url "/stores/"
        Then I see the header "Stores"
    Scenario: Articles Page
        Given I access the url "/articles/"
        Then I see the header "Articles"
