# SqaEdwinTovar
# Para Ejecutar el proyecto es importante actualizar la ruta del WebDriver ubicada en archivo SqaEdwinTovar, ya que esta seteada a la ruta del computador personal.
      @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path= r"C:\Program Files\Python310\Chome_Driver\chromedriver.exe")
    cls.driver.maximize_window()
# Este proyecto se realizo bajo el lenguaje Python y Selenium Web Driver.
