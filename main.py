import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# 1
def first_task():
    print("Start")
    driverChrome = webdriver.Chrome()
    driverChrome.get("http://www.walla.co.il")

    driverFirefox = webdriver.Firefox()
    driverFirefox.get("http://www.ynet.co.il")

    driverChrome.quit()
    driverFirefox.quit()
    print("Finish")

# 2
def second_task():
    print("Start")
    driverChrome = webdriver.Chrome()
    driverChrome.get("http://www.walla.co.il")

    websiteTitle = driverChrome.title
    driverChrome.refresh()
    websiteName = driverChrome.title

    isEqual = websiteName == websiteTitle
    driverChrome.quit()
    print(f"The answer: {isEqual}")
    print("Finish")

# 3
def third_task():
    print("Start")
    driverChrome = webdriver.Chrome()
    driverChrome.get("http://www.walla.co.il")
    driverChrome2 = webdriver.Chrome()
    driverChrome2.get("http://www.walla.co.il")
    try:
        humanImage = driverChrome.find_element(By.CLASS_NAME, "ally-icon")
        humanImage2 = driverChrome2.find_element(By.CLASS_NAME, "ally-icon")
    except:
        print("One of the human images was not found :(")

    print("answer:")
    print("yes, they have the same locators in the other browser (but also some of them can be different)")

    driverChrome.close()
    driverChrome2.close()
    print("Finish")

# 4
def forth_task():
    print("Start")
    driverChrome = webdriver.Chrome()
    driverChrome.get("https://translate.google.com/")
    time.sleep(2)
    driverChrome.maximize_window()

    try:
        # wait 10 seconds before looking for element
        rejectAllBtn = (WebDriverWait(driverChrome, 10)
                        .until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label ='Reject all']"))))
        rejectAllBtn.submit()
    except:
        print("Reject ALL Button was not found. Trying to find text area...")

    try:
        # wait 10 seconds before looking for element
        textArea = (WebDriverWait(driverChrome, 10)
                    .until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Source text']"))))
        textArea.send_keys("שלום עולם!")

    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'textArea': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'textArea': {ex.msg}")
        else:
            print(ex)

    time.sleep(5)
    driverChrome.quit()
    print("Finish")


# 5
def fifth_task(songName="RKS - Goodnight Chicago"):
    print("Start")
    userInput = input("Enter a song name to find\n(if you'll enter nothing the script will find a default one):")
    if userInput.strip(' \t\n\r') != "":
        songName = userInput
    print(f"The script will find '{songName}'")
    driverChrome = webdriver.Chrome()
    driverChrome.get("https://youtube.com/")
    time.sleep(2)
    driverChrome.maximize_window()
    time.sleep(2)
    try:
        # wait 10 seconds before looking for element
        rejectAllBtn = (WebDriverWait(driverChrome, 10)
                        .until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label ='Reject the use of cookies and other data for the purposes described']"))))
        rejectAllBtn.click()
    except:
        print("Reject ALL Button was not found. Trying to find search field ...")

    time.sleep(2)

    n = 3
    for x in range(n):
        try:
            # wait 10 seconds before looking for element
            searchField = (WebDriverWait(driverChrome, 10)
                        .until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))))
            searchField.send_keys(songName)
            for _ in range(3):
                value = searchField.get_attribute("value")
                if value != songName:
                    time.sleep(1)
                else:
                    break
            break
        except Exception as ex:
            time.sleep(2)
            if x < n-1:
                continue
            if hasattr(ex, 'message'):
                print(f"Exception message about 'searchField': {ex.message}")
            elif hasattr(ex, 'msg'):
                print(f"Exception message about 'searchField': {ex.msg}")
            else:
                print(ex)

    time.sleep(2)

    try:
        # wait 10 seconds before looking for element
        searchBtn = (WebDriverWait(driverChrome, 10)
                        .until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label ='Search']"))))
        searchBtn.click()
    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'searchBtn': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'searchBtn': {ex.msg}")
        else:
            print(ex)

    time.sleep(10)
    driverChrome.quit()
    print("Finish")

def sixth_task():
    print("Start")
    driverChrome = webdriver.Chrome()
    driverChrome.get("https://translate.google.com/")
    time.sleep(2)
    driverChrome.maximize_window()
    time.sleep(2)

    try:
        # wait 10 seconds before looking for element
        rejectAllBtn = (WebDriverWait(driverChrome, 10)
                        .until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label ='Reject all']"))))
        rejectAllBtn.submit()
    except:
        print("Reject ALL Button was not found. Trying to find text area...")

    try:
        print("TextArea is found using XPATH locator: ")
        # wait 10 seconds before looking for element
        textArea = (WebDriverWait(driverChrome, 10)
                    .until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Source text']"))))
        print(textArea)

    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'textArea': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'textArea': {ex.msg}")
        else:
            print(ex)

    try:
        print("TextArea is found using CLASS_NAME locator: ")
        # wait 10 seconds before looking for element
        textArea = (WebDriverWait(driverChrome, 10)
                    .until(EC.presence_of_element_located((By.CLASS_NAME, "er8xn"))))
        print(textArea)

    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'textArea': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'textArea': {ex.msg}")
        else:
            print(ex)

    try:
        print("TextArea is found using TAG_NAME locator: ")
        # wait 10 seconds before looking for element
        textArea = (WebDriverWait(driverChrome, 10)
                    .until(EC.presence_of_element_located((By.TAG_NAME, "textarea"))))
        print(textArea)

    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'textArea': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'textArea': {ex.msg}")
        else:
            print(ex)

    time.sleep(5)
    driverChrome.quit()
    print("Finish")


def seventh_task(userEmail = "UserName@gmail.com", password = "P4sS_w0rd"):
    print("Start")
    userInput = input("Enter a userEmail\n(if you'll enter nothing the script will use a default one):")
    if userInput.strip(' \t\n\r') != "":
        userEmail = userInput
    userInput = input("Enter a password\n(if you'll enter nothing the script will use a default one):")
    if userInput.strip(' \t\n\r') != "":
        password = userInput

    driverChrome = webdriver.Chrome()
    driverChrome.get("https://facebook.com/")
    time.sleep(2)
    driverChrome.maximize_window()
    time.sleep(2)

    try:
        # wait 5 seconds before looking for element
        declineOptionalBtn = (WebDriverWait(driverChrome, 5)
                        .until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label ='Decline optional cookies']"))))
        declineOptionalBtn.click()
    except:
        try:
            declineOptionalBtn = (WebDriverWait(driverChrome, 5)
                                  .until(EC.presence_of_element_located((By.XPATH, "//button[@title ='Decline optional cookies']"))))
            declineOptionalBtn.click()
        except:
            print("Reject ALL Button was not found. Trying to find text area...")

    time.sleep(2)

    try:
        # wait 5 seconds before looking for element
        emailInput = (WebDriverWait(driverChrome, 5)
                    .until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))))
        emailInput.send_keys(userEmail)

    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'emailInput': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'emailInput': {ex.msg}")
        else:
            print(ex)

    try:
        # wait 5 seconds before looking for element
        passInput = (WebDriverWait(driverChrome, 5)
                    .until(EC.presence_of_element_located((By.XPATH, "//input[@id='pass']"))))
        passInput.send_keys(password)

    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'passInput': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'passInput': {ex.msg}")
        else:
            print(ex)

    time.sleep(2)

    try:
        # wait s seconds before looking for element
        logInBtn = (WebDriverWait(driverChrome, 5)
                        .until(EC.presence_of_element_located((By.XPATH, "//button[@name ='login']"))))
        logInBtn.submit()
    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'logInBtn': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'logInBtn': {ex.msg}")
        else:
            print(ex)

    time.sleep(5)
    driverChrome.quit()
    print("Finish")


def eighth_task():
    print("Start")
    driverChrome = webdriver.Chrome()
    driverChrome.delete_all_cookies()
    print(f"All coockies: {driverChrome.get_cookies()}")
    time.sleep(5)
    driverChrome.quit()
    print("Finish")


def nineth_task():
    print("Start")
    driverChrome = webdriver.Chrome()
    driverChrome.get("https://github.com/")
    time.sleep(2)
    driverChrome.maximize_window()
    time.sleep(2)

    try:
        # wait 5 seconds before looking for element
        searchInput = (WebDriverWait(driverChrome, 5)
                    .until(EC.presence_of_element_located((By.XPATH, "//button[@placeholder='Search or jump to...']"))))
        searchInput.click()
        searchInput = (WebDriverWait(driverChrome, 5)
                       .until(EC.presence_of_element_located((By.XPATH, "//input[@id='query-builder-test']"))))
        searchInput.send_keys("Selenium")
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)

    except Exception as ex:
        if hasattr(ex, 'message'):
            print(f"Exception message about 'searchInput': {ex.message}")
        elif hasattr(ex, 'msg'):
            print(f"Exception message about 'searchInput': {ex.msg}")
        else:
            print(ex)

    time.sleep(7)
    driverChrome.quit()
    print("Finish")


def tenth_task():
    print("Start")
    print("Chrome...")
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    driverChrome = webdriver.Chrome(options=chrome_options)
    waitQ = ""
    while waitQ.lower().strip() != 'q':
        waitQ = input("Write 'Q' when quit this browser and go the next one...\n")
    driverChrome.quit()

    print("Firefox...")
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("-safe-mode")
    driverFirefox= webdriver.Firefox(options=firefox_options)
    waitQ = ""
    while waitQ.lower().strip() != 'q':
        waitQ = input("Write 'Q' when quit this browser and go the next one...\n")
    driverFirefox.quit()

    print("Edge...")
    edge_options = EdgeOptions()
    edge_options.add_argument("–-disable-extensions")
    driverEdge= webdriver.Edge(options=edge_options)
    waitQ = ""
    while waitQ.lower().strip() != 'q':
        waitQ = input("Write 'Q' when quit this browser and go the next one...\n")
    driverEdge.quit()


def get_digit_if_its_in_range(number, range_to_check):
    while not number.isdigit():
        number = input("You wrote smth wrong. Try again. Your choice: ")

    number_int = int(number)

    if not (number_int in range_to_check):
        number_int = get_digit_if_its_in_range("", range_to_check)

    return number_int

def main():
    main_flag = True
    while main_flag:
        print("Hi, Teacher! Which task do you want to check?\nWrite the number from 1 to 10 [write 11 if you want to exit.]: ")
        teachers_input = input()
        task_num = get_digit_if_its_in_range(teachers_input, range(1, 12))

        match task_num:
            case 1:
                first_task()
            case 2:
                second_task()
            case 3:
                third_task()
            case 4:
                forth_task()
            case 5:
                fifth_task()
            case 6:
                sixth_task()
            case 7:
                seventh_task()
            case 8:
                eighth_task()
            case 9:
                nineth_task()
            case 10:
                tenth_task()
            case 11:
                print("Thank you for checking my hometasks!")
                main_flag = False
                continue

        print("\nDo you want to check one more task?\n"
              "Press 'Y' if yes, press 'N' if no: ")
        choice = input()
        if choice.lower().strip() != "y":
            print("Thank you for checking my hometasks!")
            main_flag = False

if __name__ ==  "__main__":
    main()


