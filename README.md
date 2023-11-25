# Test_Automation_Project
This Repository contains Test Automation project using Python and Selenium Webdriver.

# Requirements

* Python3
* Selenium
# Installation

* `pip install selenium`
* `pip install webdriver_manager`
  
# Configuration

By default, tests will be executed in Chrome (normal mode).
# Algorithm
* Gold bars will be divided in to three piles of equal length
* Load pile1 on the left side and pile2 on the right side.
* Get the result of the weighings.
* If the result is "=", then pile3 will be the lighter pile.
* If the result is "<", then pile1 will be the lighter pile, otherwise pile2 is the lighter pile.
* Similarly, weigh the coins in the pile to find the lighter coin.
* Varible fake_gold will contain the index of the fake gold bar. 

# Test Execution

From the project root directory run    `python test_automation.py`

# Results
* The algorithm will populate and weight the gold bars until it found a fake one.
* Fake bar number will be clicked.
* In the terminal, Fake bar number, alert message, number of weighings and list of the weighings are printed.





