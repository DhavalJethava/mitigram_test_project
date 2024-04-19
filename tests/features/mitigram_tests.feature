Feature: Test login to mitigram portal

  Background:
    Given User is on the application home page

  Scenario Outline: Invalid login attempt to the portal
    When  User performs login with "<user_name>" and "<password>"
    Then  Login attempt should fail with the message "<notification>"

    Examples:
    | user_name                 | password    |   notification    |
    | test_user@mitigram.com    | testing@123 |   Invalid login attempt. |
    | test_user                 | testing@123 |   The Email field is not a valid e-mail address. |
    | test_user.com             | testing@123 |   The Email field is not a valid e-mail address. |
    | <BLANK>                   | testing@123 |   Email is required The Email field is not a valid e-mail address. |
    | test_user@mitigram.com    | <BLANK>     |   Password is required |
    | <BLANK>                   | <BLANK>     |   Email is required The Email field is not a valid e-mail address. |

  Scenario: Verify careers page displayed
    When  User navigates to the "careers" page
    Then  User should see the page title as "Careers"
    And   User should see "Open positions" section displayed

  Scenario: Verify different open positions
    When  User navigates to the "careers" page
    Then  User should see the following open positions:
        | open positions                    |
        | BI Analyst                        |
        | QA Automation Engineer            |
        | Back-end Software Engineer        |
        | Front-end Software Engineer       |
        | Legal Counsel                     |
        | Product Implementation Consultant |
    When  User click on "Data" section under open positions
    Then  User should see the following open positions:
        | open positions                    |
        | BI Analyst                        |
    When  User click on "Engineering" section under open positions
    Then  User should see the following open positions:
        | open positions                    |
        | QA Automation Engineer            |
        | Back-end Software Engineer        |
        | Front-end Software Engineer       |
    When  User click on "Legal" section under open positions
    Then  User should see the following open positions:
        | open positions                    |
        | Legal Counsel                     |
    When  User click on "Product" section under open positions
    Then  User should see the following open positions:
        | open positions                    |
        | Product Implementation Consultant |










