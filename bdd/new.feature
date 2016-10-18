Scenario Outline: Registration
  Given Open home-page and open registration form
  When I input all required fields "<username>", "<phone>","<email>","<password>"
  Then I press submit button and see homepage authorized user

  Examples:
  | username | phone | email | password |
  | TEST | 4444444444 | wqer21@gmail.com | qwer1234eqer |


  Scenario Outline: Login
  Given Open home-page
  When Open a login form and login "<username>", "<password>" I logout
  Then I see home page an unauthorized user

  Examples:
  | username | password |
  | w@w.com | 111111 |

