from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class SeleniumHelper:

    @staticmethod
    def existe_elemento(driver, by, ignore_displayed_attribute=False):
        try:
            elemento = driver.find_element(*by)  # Deve passar uma tupla (By.<método>, 'valor')
            if not ignore_displayed_attribute and not elemento.is_displayed():
                return None
            return elemento
        except NoSuchElementException:
            return None

    @staticmethod
    def existe_elemento_web_element(web_element, by, ignore_displayed_attribute=False):
        try:
            elemento = web_element.find_element(*by)  # Deve passar uma tupla (By.<método>, 'valor')
            if not ignore_displayed_attribute and not elemento.is_displayed():
                return None
            return elemento
        except NoSuchElementException:
            return None

    @staticmethod
    def existe_elementos(driver, by):
        try:
            return driver.find_elements(*by)  # Deve passar uma tupla (By.<método>, 'valor')
        except NoSuchElementException:
            return []

    @staticmethod
    def existe_elementos_web_element(web_element, by):
        try:
            return web_element.find_elements(*by)  # Deve passar uma tupla (By.<método>, 'valor')
        except NoSuchElementException:
            return []

    @staticmethod
    def aguardar_ate_carregar_elemento(driver, by, ignore_displayed_attribute=False):
        elemento = None
        while elemento is None:
            elemento = SeleniumHelper.existe_elemento(driver, by, ignore_displayed_attribute)
        return elemento

    @staticmethod
    def existe_select(driver, by):
        try:
            elemento = driver.find_element(*by)  # Deve passar uma tupla (By.<método>, 'valor')
            if not elemento.is_displayed():
                return None
            return Select(elemento)
        except NoSuchElementException:
            return None

    @staticmethod
    def existe_alerta(driver):
        try:
            return driver.switch_to.alert
        except NoAlertPresentException:
            return None

    @staticmethod
    def selecionar_frame(driver, frame=""):
        time.sleep(3)
        try:
            driver.switch_to.default_content()
            if frame:
                driver.switch_to.frame(frame)
        except Exception as e:
            raise Exception("Não conseguiu acessar o frame interno da consulta") from e

    @staticmethod
    def selecionar_frames(driver, *frames):
        time.sleep(2)
        try:
            driver.switch_to.default_content()
            for frame in frames:
                driver.switch_to.frame(frame)
        except Exception as e:
            raise Exception("Não conseguiu acessar o frame interno da consulta") from e

    @staticmethod
    def resetar_eventos(js_executor, elemento):
        js_executor.execute_script("arguments[0].setAttribute('onkeydown', '')", elemento)
        js_executor.execute_script("arguments[0].setAttribute('onfocus', '')", elemento)
        js_executor.execute_script("arguments[0].setAttribute('onkeypress', '')", elemento)

    @staticmethod
    def scroll_para_elemento(js_executor, elemento):
        js_executor.execute_script("arguments[0].scrollIntoView(true);", elemento)

    @staticmethod
    def scroll_para_o_topo(js_executor):
        js_executor.execute_script("window.scrollTo(0, 0);")

    @staticmethod
    def tirar_screenshot_da_tela(driver, path="screenshot.png"):
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot))
        image.save(path)
        return image

    @staticmethod
    def obter_cookies_do_navegador(driver):
        cookies = driver.get_cookies()
        return "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

    @staticmethod
    def quantidade_de_janelas_abertas(driver):
        return len(driver.window_handles)

    @staticmethod
    def fechar_todas_as_popups(driver):
        num_janelas = SeleniumHelper.quantidade_de_janelas_abertas(driver)
        if num_janelas > 1:
            for i in range(1, num_janelas):
                popup = driver.switch_to.window(driver.window_handles[i])
                popup.close()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[0])

    @staticmethod
    def abrir_janelas(js_executor, urls):
        for url in urls:
            js_executor.execute_script(f"window.open('{url}')")

    @staticmethod
    def maximizar_janela(driver):
        try:
            driver.maximize_window()
        except:
            pass
