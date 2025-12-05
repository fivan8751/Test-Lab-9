from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import pytest

@pytest.fixture(scope="session")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.google.android.deskclock"
    options.app_activity = "com.android.deskclock.DeskClock"
    options.no_reset = True
    
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

def test_open_clock_app(driver):
    time.sleep(5)
    
    #Приложение запустилось 
    print(f"Текущая активность: {driver.current_activity}")
    print(f"Пакет: {driver.current_package}")
    
    #Найдены любые элементы UI
    elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
    assert len(elements) > 0, "Интерфейс приложения загружен"
    
    #Приложение отвечает на тапы
    if elements:
        elements[0].click()
        print("Тап выполнен")
    
    print("Тест выполнен")
