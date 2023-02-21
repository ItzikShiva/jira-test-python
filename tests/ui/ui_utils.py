from selenium import webdriver


def setup_driver_options():
    # this "option" because old writing is deprecated & to cancel an error of "USB: usb_device_handle..." 19-2-23
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)
