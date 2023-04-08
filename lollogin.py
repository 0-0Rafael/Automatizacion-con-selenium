import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LolLogin(unittest.TestCase):
    def setUp(self):
        
        # Iniciar el Service de Chrome
        self.cdriver = webdriver.Chrome(executable_path=r"C:\Users\18294\Desktop\Proyecto_automatizacion_con_selenium\chromedriver.exe")
        self.wait = WebDriverWait(self.cdriver, 10)

    def test_01_login_mala(self,):
        self.cdriver.maximize_window()
        self.cdriver.get("https://lolesports.com")

        # Iniciar sesión en LoL Esports
        self.btn_iniciar = self.cdriver.find_element(By.XPATH, "//a[@class='_2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action _1SFUgr_Ul0xq7X3IdHVHrL theme-button']")
        self.btn_iniciar.click()

        self.btn_usuario = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'username')]")
        self.btn_usuario.send_keys("arabeBOOMSS")

        self.btn_contraseña = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        self.btn_contraseña.send_keys("ariel200333")

        self.btn_mantenerinicio = self.cdriver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]")
        self.btn_mantenerinicio.click()

        time.sleep(10)
        self.btn_entrar = self.cdriver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        self.btn_entrar.click()

        time.sleep(5)
        self.cdriver.save_screenshot('no_login.png')
        time.sleep(5)  

    def test_02_login_buena(self,):
        self.cdriver.maximize_window()
        self.cdriver.get("https://lolesports.com")

        # Iniciar sesión en LoL Esports
        self.btn_iniciar = self.cdriver.find_element(By.XPATH, "//a[@class='_2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action _1SFUgr_Ul0xq7X3IdHVHrL theme-button']")
        self.btn_iniciar.click()

        time.sleep(10)

        self.btn_usuario = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'username')]")
        self.btn_usuario.send_keys("arabeBOOMS")

        self.btn_contraseña = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        self.btn_contraseña.send_keys("ariel20033")

        self.btn_mantenerinicio = self.cdriver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]")
        self.btn_mantenerinicio.click()

        time.sleep(10)

        #captura
        self.cdriver.save_screenshot('login.png')
        self.btn_entrar = self.cdriver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        self.btn_entrar.click()

        time.sleep(10)     


    def test_03_select_lck_lec(self):
        self.cdriver.maximize_window()
        self.cdriver.get("https://lolesports.com")

        # Iniciar sesión en LoL Esports
        self.btn_iniciar = self.cdriver.find_element(By.XPATH, "//a[@class='_2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action _1SFUgr_Ul0xq7X3IdHVHrL theme-button']")
        self.btn_iniciar.click()

        time.sleep(10)

        self.btn_usuario = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'username')]")
        self.btn_usuario.send_keys("arabeBOOMS")

        self.btn_contraseña = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        self.btn_contraseña.send_keys("ariel20033")

        self.btn_mantenerinicio = self.cdriver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]")
        self.btn_mantenerinicio.click()

        time.sleep(10)
        self.btn_entrar = self.cdriver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        self.btn_entrar.click()

        time.sleep(10)  
        
        self.cdriver.save_screenshot('pagina_principal.png')

        self.selec_calendario = self.cdriver.find_element(By.XPATH, "//a[@data-testid='riotbar:desktopNav:link-internal-schedule']")
        self.selec_calendario.click()

        time.sleep(10)

        self.cdriver.save_screenshot('calendario.png')

        self.elemento_lck = self.cdriver.find_element(By.XPATH, "//button[@class='button league'][contains(.,'LCKCOREA')]")
        self.cdriver.execute_script("arguments[0].scrollIntoView();", self.elemento_lck)

        time.sleep(5)

        lck = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='button league'][contains(.,'LCKCOREA')]")))
        lck.click()

        time.sleep(5)
        self.cdriver.save_screenshot('calendario_lck.png')

        time.sleep(10)

        self.elemento_lec = self.cdriver.find_element(By.XPATH, "//button[@class='button league'][contains(.,'LECEMEA')]")
        self.cdriver.execute_script("arguments[0].scrollIntoView();", self.elemento_lec)

        time.sleep(5)
        lec = self.cdriver.find_element(By.XPATH, "//button[@class='button league'][contains(.,'LECEMEA')]")
        lec.click()  

        time.sleep(5)
        self.cdriver.save_screenshot('calendario_lec.png')
        time.sleep(5)

    def test_04_vod(self,):
        self.cdriver.maximize_window()
        self.cdriver.get("https://lolesports.com")

        # Iniciar sesión en LoL Esports
        self.btn_iniciar = self.cdriver.find_element(By.XPATH, "//a[@class='_2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action _1SFUgr_Ul0xq7X3IdHVHrL theme-button']")
        self.btn_iniciar.click()

        time.sleep(10)

        self.btn_usuario = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'username')]")
        self.btn_usuario.send_keys("arabeBOOMS")

        self.btn_contraseña = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        self.btn_contraseña.send_keys("ariel20033")

        self.btn_mantenerinicio = self.cdriver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]")
        self.btn_mantenerinicio.click()

        time.sleep(10)
        self.btn_entrar = self.cdriver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        self.btn_entrar.click()

        time.sleep(10)     
        selec_vod = self.cdriver.find_element(By.XPATH, "//a[@data-testid='riotbar:desktopNav:link-internal-vods']")
        selec_vod.click()

        time.sleep(10)

        self.cdriver.save_screenshot('vod.png')

        vod_lck = self.cdriver.find_element(By.XPATH, "//button[@class='info button'][contains(.,'LCKCOREA')]")
        self.cdriver.execute_script("arguments[0].scrollIntoView();", vod_lck)
        time.sleep(5)


        lck = self.cdriver.find_element(By.XPATH, "//button[@class='info button'][contains(.,'LCKCOREA')]")
        lck.click()

        time.sleep(5)
        self.cdriver.save_screenshot('vod_lck.png')
        time.sleep(10)

        vod_lec = self.cdriver.find_element(By.XPATH, "//button[@class='info button'][contains(.,'LECEMEA')]")
        self.cdriver.execute_script("arguments[0].scrollIntoView();", vod_lec)

        time.sleep(5)
        lec = self.cdriver.find_element(By.XPATH, "//button[@class='info button'][contains(.,'LECEMEA')]")
        lec.click()

        time.sleep(5)
        self.cdriver.save_screenshot('vod_lec.png')
        time.sleep(5)

    def test_05_posiciones(self,):
        self.cdriver.maximize_window()
        self.cdriver.get("https://lolesports.com")

        # Iniciar sesión en LoL Esports
        self.btn_iniciar = self.cdriver.find_element(By.XPATH, "//a[@class='_2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action _1SFUgr_Ul0xq7X3IdHVHrL theme-button']")
        self.btn_iniciar.click()

        time.sleep(10)

        self.btn_usuario = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'username')]")
        self.btn_usuario.send_keys("arabeBOOMS")

        self.btn_contraseña = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        self.btn_contraseña.send_keys("ariel20033")

        self.btn_mantenerinicio = self.cdriver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]")
        self.btn_mantenerinicio.click()

        time.sleep(10)
        self.btn_entrar = self.cdriver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        self.btn_entrar.click()

        time.sleep(10)    

        selec_posiciones = self.cdriver.find_element(By.XPATH, "//a[@data-testid='riotbar:desktopNav:link-internal-standings']")
        selec_posiciones.click()

        
        self.cdriver.save_screenshot('posicion.png')
        time.sleep(10)

        posicion_lck = self.cdriver.find_element(By.XPATH, "//button[@class='button info'][contains(.,'LCKCOREA')]")
        self.cdriver.execute_script("arguments[0].scrollIntoView();", posicion_lck)
        time.sleep(10)
        
        posicion_lck.click()

        time.sleep(5)
        self.cdriver.save_screenshot('posicion_lck.png')

        time.sleep(10)

        posicion_lec = self.cdriver.find_element(By.XPATH, "//button[@class='button info'][contains(.,'LECEMEA')]")
        self.cdriver.execute_script("arguments[0].scrollIntoView();", posicion_lec)

        time.sleep(5)
        lec = self.cdriver.find_element(By.XPATH, "//button[@class='button info'][contains(.,'LECEMEA')]")
        lec.click()

        time.sleep(5)
        self.cdriver.save_screenshot('posicion_lec.png')
        time.sleep(5)

    def test_06_salir(self):
        time.sleep(5)
        self.cdriver.maximize_window()
        self.cdriver.get("https://lolesports.com")

        # Iniciar sesión en LoL Esports
        self.btn_iniciar = self.cdriver.find_element(By.XPATH, "//a[@class='_2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action _1SFUgr_Ul0xq7X3IdHVHrL theme-button']")
        self.btn_iniciar.click()

        time.sleep(10)

        self.btn_usuario = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'username')]")
        self.btn_usuario.send_keys("arabeBOOMS")

        self.btn_contraseña = self.cdriver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        self.btn_contraseña.send_keys("ariel20033")

        self.btn_mantenerinicio = self.cdriver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]")
        self.btn_mantenerinicio.click()

        time.sleep(10)
        self.btn_entrar = self.cdriver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        self.btn_entrar.click()

        time.sleep(10)  
        btn_perfi = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'_16YqTG4Iq4iNJMhvvUCe3k riotbar-summoner-name')]")))
        btn_perfi.click()

        time.sleep(2)
        self.cdriver.save_screenshot('opcion_salir.png')

        btn_cerrar = self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='Roe30JJ8Opt7OrRHbXpyI riotbar-account-dropdown-link-text'][contains(.,'Cerrar sesión')]")))
        btn_cerrar.click()

        self.cdriver.save_screenshot('opcion_cerrar.png')
        time.sleep(5)
        
        

        

# Crear una instancia del objeto LolLogin y utilizar sus métodos para iniciar sesión y seleccionar la liga LCK y LEC
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reporte test'))
    