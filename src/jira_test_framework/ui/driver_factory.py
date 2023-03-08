from selenium import webdriver


def get_chrome_driver(without_gpu=False) -> webdriver:
    # this "option" because old writing is deprecated & to cancel an error of "USB: usb_device_handle..." 19-2-23
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--start-maximized")
    if without_gpu:
        options.headless = True
    return webdriver.Chrome(executable_path='C:\Drivers\chromedriver\chromedriver.exe', options=options)
