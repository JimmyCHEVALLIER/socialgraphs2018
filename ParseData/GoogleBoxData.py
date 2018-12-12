from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Get the categorie of a celebrity
# param get the name of the celebrity
# return a string representing the categorie
def getGoogleCategorie(name):
    url = "https://www.google.com/search?q="+ name +"&oq="+ name +"&ie=UTF-8&lr=lang_fr"
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome("/Users/jimmy/Desktop/Social_Graph_Git/PerseData/chromedriver", chrome_options=options)
    driver.get(url)
    p_element = driver.find_element_by_class_name("wwUB2c")
    if type(p_element) != dict:
        return p_element.text
    return "notFound"

# get google category
# print(getGoogleCategorie("Lionel Messi"))