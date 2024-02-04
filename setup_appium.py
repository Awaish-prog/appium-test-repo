import logging
import sys
import time
import os
from appium import webdriver
from selenium.webdriver.common.by import By as by
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec


# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='Android',
#     language='en',
#     locale='US',
#     browserName='Chrome',
#     chromedriverExecutable=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe'),
#     # appPackage='com.android.settings',
#     # appActivity='.Settings',
# )
capabilities_meta_mask = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    app=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meta-mask.apk'),
    newCommandTimeout=220000,
    uiautomator2ServerInstallTimeout=220000
)
appium_server_url = 'http://127.0.0.1:4723'

# driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

setup_executed = False
skip_test = False


def find_element_recursive(driver, xpath, time_out, i):
    if i <= 0:
        driver.quit()
        sys.exit()
    try:
        time.sleep(time_out)
        element = driver.find_element(AppiumBy.XPATH, xpath)
        print("Clicking...")
        element.click()
    except NoSuchElementException:
        print("retrying..., no such element")
        find_element_recursive(driver, xpath, time_out, i - 1)
    except:
        print("retrying..., unknown")
        find_element_recursive(driver, xpath, time_out, i - 1)


def setup_testnet():
    # driver.get(market_place_url)
    # wait.until(ec.presence_of_element_located((by.XPATH, "//*[contains(text(), 'Login with Web3 Wallet')]")))
    # wait.until(ec.presence_of_element_located((by.XPATH, "//*[contains(text(), 'Login with Web3 Wallet')]"))).click()
    # driver.activate_app("com.android.settings")

    # driver.activate_app("com.android.chrome")
    # driver.get(market_place_url)
    # wait.until(ec.presence_of_element_located((by.XPATH, "//*[contains(text(), 'Login with Web3 Wallet')]")))
    # wait.until(ec.presence_of_element_located((by.XPATH, "//*[contains(text(), 'Login with Web3 Wallet')]"))).click()
    # wait.until(ec.presence_of_element_located((by.XPATH, "//*[contains(text(), 'Login with Metamask')]")))
    # wait.until(ec.presence_of_element_located((by.XPATH, "//*[contains(text(), 'Login with Metamask')]"))).click()
    driver_meta_mask = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities_meta_mask))
    # driver_meta_mask.install_app(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meta-mask.apk'))
    # driver_meta_mask.activate_app("io.metamask")
    print("Opened app")
    time.sleep(30)
    # find_element_recursive(driver_meta_mask, "//*[contains(@text,'Get started')]", 2, 15)
    # find_element_recursive(driver_meta_mask, "//*[contains(@text,'Import using Secret Recovery Phrase')]", 2, 15)
    WebDriverWait(driver_meta_mask, 30).until(ec.presence_of_element_located(
        (AppiumBy.XPATH, "//*[contains(@text,'Get started')]"))).click()
    print("get started clicked")
    WebDriverWait(driver_meta_mask, 30).until(ec.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text,'Import using Secret Recovery Phrase')]"))).click()
    print("Crossed...")
    driver_meta_mask.quit()
    # print("Located button clicked")
    # wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text,'Import using Secret Recovery Phrase')]")))
    # import_button = driver_meta_mask.find_element(AppiumBy.XPATH, "//*[contains(@text,'Import using Secret Recovery Phrase')]")
    # import_button.click()
    # print("setup successful...")


setup_testnet()
