import pytest
import csv
import time
from appium import webdriver

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

APPIUM_PORT = 4723
APPIUM_HOST = '192.168.0.221' #'127.0.0.1'
START_TIME = 0
count_global = 0
count_printer_times = 0
bot_IP = "192.168.123.11"
TIMEOUT = str(0)
total_tape_times = 1

@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    global START_TIME 
    START_TIME= time.perf_counter_ns()

    yield service
    service.stop()


def create_ios_driver(custom_opts = None):
    options = XCUITestOptions()
    options.platformVersion = '13.4'
    options.udid = '123456789ABC'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


def create_android_driver(custom_opts = None):
    options = UiAutomator2Options()
    options.platformVersion = '13'
    #options.udid = '123456789ABC'
    custom_opts = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='pixel 4',
        #deviceName="27121FDH2000AG", #Pixel 7-27121FDH2000AG,
        #appPackage='us.newellbrands.dymoletratagconnect',
        appPackage= 'us.newellbrands.dymolabelmanagerconnect',
        appActivity='com.pegusapps.MainActivity',
        language='en',
        locale='US',
        noReset=True,
    )
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


@pytest.fixture
def ios_driver_factory():
    return create_ios_driver


@pytest.fixture
def ios_driver():
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_ios_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def android_driver_factory():
    return create_android_driver


@pytest.fixture(scope="function")
def android_driver():
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_android_driver()
    yield driver
    driver.quit()



def test_ios_click(appium_service, ios_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with ios_driver_factory({
        'appium:app': '/path/to/app/UICatalog.app.zip'
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
        el.click()


def test_android_click(appium_service, android_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with android_driver_factory({
        'appium:app': '/path/to/app/test-app.apk',
        'appium:udid': '567890',
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
        el.click()


@pytest.fixture(scope='session')
def bot_connect():
    global START_TIME 
    START_TIME= time.perf_counter_ns()
    client = modbus_connect()
    client.connect() 
    yield  client
    client.close()


#@pytest.fixture(scope="session")
def total_cassette_check():
    global total_tape_times
    if total_tape_times > 8:
        pytest.exit("No cassette in the bot")
    total_tape_times += 1
    #print(total_tape_times)

#@pytest.fixture(scope="session")
def print_num_labels_check():
    global count_global 
    count_global += 1
    return count_global

def print_num_labels_default():
    global count_global
    count_global = 1
    return count_global

@pytest.fixture(scope="function")
def check_cassette_empty(bot_connect):
    #current_time = time.perf_counter_ns()
    #count = round(current_time) - round(START_TIME)
    count = print_num_labels_check()
    client = bot_connect 
    client.write_coil(16,False)
    if count == 1:
        time.sleep(1)
        print("send a msg to bot")
        client.write_coil(16,True)
        while True:
            status_bot = client.read_coils(17,1)
            if (status_bot.bits[0]):
                print('get a msg from bot')
                client.write_coil(16,False)
                print('The app will restart printing')
                break     
            time.sleep(1)  
    if count > 45:
        print("send a msg to machine")
        client.write_coil(16,True)
        while True:
            status_bot = client.read_coils(17,1)
            if (status_bot.bits[0]):
                print('get a msg from bot')
                client.write_coil(16,False)
                print('write to false')
                break  
            print('Wait for a singnal from bot')
            print(status_bot)
            time.sleep(1)  
        #count = 0
        print_num_labels_default()
        total_cassette_check()
        return False
    return False 
