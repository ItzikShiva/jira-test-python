from selenium import webdriver


def get_chrome_driver():
    # this "option" because old writing is deprecated & to cancel an error of "USB: usb_device_handle..." 19-2-23
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(executable_path='C:\Drivers\chromedriver\chromedriver.exe', options=options)
