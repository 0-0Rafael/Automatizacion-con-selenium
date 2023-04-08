from lollogin import LolLogin  # Importar la clase LolLogin desde el archivo lollogin.py

# Ruta del driver de Chrome


# Crear una instancia de LolLogin
lol_login = LolLogin()

# Iniciar sesión en LoL Esports

lol_login.test_login()

# Seleccionar ligas LCK y LEC
lol_login.test_select_lck_lec()

lol_login.test_vod_lck_lec()

lol_login.test_posiciones_lck_lec()

lol_login.test_salir()

# Cerrar la sesión y cerrar el navegador
lol_login.logout() 
