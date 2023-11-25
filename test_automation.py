from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Function to load the left and right bowls
def load_bowl(bowl, arr):
    for n in arr:
        id = bowl + "_" + str(n)
        driver.find_element(By.ID, id).send_keys(n)

# Function to get the result
def get_result():
    """
    Retrieves the result from a web page.

    This function finds an element with the class name 'result'
    containing a button element. It waits for the button text to change from '?'
    and then returns the updated text.

    Returns:
    - str: The text of the result button(It can be =, < or >).

    Note:
    - The function uses an implicit wait of 3 seconds for the button text to change.
    """
    result_div = driver.find_element(By.CLASS_NAME, "result")
    result_button = result_div.find_element(By.TAG_NAME, "button")
    while result_button.text == '?':
        driver.implicitly_wait(3)    
    return result_button.text

# Function to click the reset button
def reset_bowls():
    reset_button = driver.find_element(By.XPATH, '//button[normalize-space()="Reset"]').click()

# Function to click on the fake bar number at the bottom of the website
def click_fake_bar(fake_bar_number):
    id = "coin" + "_" + str(fake_bar_number)
    fake_bar_button = coins.find_element(By.ID, id).click()

# Function to get the alert message after clicking the fake bar number
def get_alert_message():
    alert = driver.switch_to.alert
    alert_text =  alert.text
    driver.switch_to.alert.accept()
    return alert_text

#  Function to find the fake bar
def find_fake_bar():
    fake_gold = -1
    gold_bars = [i for i in range(len(buttons))]
    weigh_button = driver.find_element(By.ID, "weigh")

    # Split the coins into three piles
    pile1, pile2, pile3 = gold_bars[:3], gold_bars[3:6], gold_bars[6:]
    load_bowl("left", pile1)
    load_bowl("right", pile2)
    weigh_button.click()
    result = get_result()
    reset_bowls()

    if result == "=":
        # If left and right pile are equal, then pile3 will be the lighter pile
        lighter_pile = pile3
    else:
        # Otherwise update the lighter pile
        lighter_pile = pile1 if result == "<" else pile2

    # weigh the coins in the lighter pile
    coin1, coin2, coin3 = lighter_pile[:]
    load_bowl("left", [coin1])
    load_bowl("right", [coin2])
    weigh_button.click()
    result = get_result()
    reset_bowls()
    if result == "=":
        # If coin1 is equal to coin2, then coin3 will be the fake coin
        fake_gold = coin3
    else:
        # Otherwise, update the fake coin
        fake_gold = coin1 if result == "<" else coin2
    return fake_gold

# Function to get the weighing list
def get_weighing_list():
    weighing_list = driver.find_elements(By.CSS_SELECTOR, 'div.game-info > ol > li')
    return weighing_list

# Open the website
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
driver.get("http://sdetchallenge.fetch.com/")

# To Read the length of the coins
coins= driver.find_element(By.CLASS_NAME, "coins")
buttons = coins.find_elements(By.TAG_NAME, "button")

# Find fake gold bar/Coin using the algorithm
fake_gold = find_fake_bar()
click_fake_bar(fake_gold)              # To click the Fake fake bar number at the bottom of the website 
alert_message = get_alert_message()    # To get the alert Message 
weighing_list = get_weighing_list()    #To get the list of weighings 

# Output the results
print(f"Fake gold number: {fake_gold}")
print(f"Alert message: {alert_message}")
print(f"Number of weighings:{len(weighing_list)}")
print(f"List of weighings Made:")
for li in weighing_list:
    print(li.text)




