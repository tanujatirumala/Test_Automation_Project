# Test_Automation_Project

This Repository contains Test Automation project using Python and Selenium Webdriver.

# Requirements

* Python3
* Selenium

# Create and activate virtual environment

<pre>
`python -m venv <ENVIRONMENT_NAME>`
`<ENVIRONMENT_NAME>\scripts\activate`</pre>
  
# Installation

`pip install -r requirements.txt`

# Test Execution

From the project root directory run    `python test_automation.py`

# Configuration

By default, tests will be executed in Chrome.

# Algorithm

*Problem Statement:* Given a balanced scale and 9 gold bars of same size and look of which one is a fake gold bar with less weight. Find the fake bar with minimum comparisons.

*Solution:*

* Gold bars will be divided in to three piles of equal length
* Load pile1 on the left side and pile2 on the right side.
* Get the result of the weighings.
* If the result is "=", then pile3 will be the lighter pile.
* If the result is "<", then pile1 will be the lighter pile, otherwise pile2 is the lighter pile.
* Similarly, weigh the coins in the pile to find the lighter coin.
* Varible fake_gold will contain the index of the fake gold bar. 


# Results

* The algorithm will populate and weight the gold bars until it found a fake one.
* Fake bar number will be clicked.
* In the terminal, Fake bar number, alert message, number of weighings and list of the weighings are printed.





