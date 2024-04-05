from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import cura.constants as const
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Appointment(webdriver.Chrome):
	
	def __init__(self, driver_path=r"x", teardown=False):
		self.driver_path = driver_path
		self.teardown = teardown
		os.environ['PATH'] += self.driver_path
		super(Appointment, self).__init__()
		self.implicitly_wait(15)
		self.maximize_window()

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.teardown:
			self.quit()

	def land_first_page(self):
		# Self explanatory, land first page of said website
		self.get(const.BASE_URL)

	def make_appointment(self):
		# Find and click the make appointment button
		date = self.find_element(By.ID,
			"btn-make-appointment")
		self.implicitly_wait(5)
		date.click()

	def login(self):
		# Hardcoding credentials
		usuario = "John Doe"
		contrasena = "ThisIsNotAPassword"
		# Find input boxes
		user_input = self.find_element(By.ID,
			"txt-username")
		password_input = self.find_element(By.ID,
			"txt-password")
		# Fill in the boxes
		user_input.send_keys(usuario)
		password_input.send_keys(contrasena)
		self.implicitly_wait(5)
		# find and click the login button
		login_button = self.find_element(By.ID,
			"btn-login")
		login_button.click()

	def select_facility(self):
		elegir_hospital = self.find_element(By.ID,
			"combo_facility")
		elegir_hospital.click()
		self.implicitly_wait(5)
		select = Select(self.find_element(By.ID,
			"combo_facility"))
		select.select_by_visible_text("Seoul CURA Healthcare Center")
		medicaid = self.find_element(By.ID,
			"radio_program_medicaid")
		medicaid.click()

	def select_date(self, date):
		calendario = self.find_element(By.CLASS_NAME,
			"input-group-addon")
		calendario.click()
		fecha = self.find_element(By.ID,
			"txt_visit_date")
		fecha.send_keys(date)
		comentario = self.find_element(By.ID,
			"txt_comment")
		self.implicitly_wait(5)
		comentario.send_keys("Sprained ankle")
		boton_cita = self.find_element(By.ID,
			"btn-book-appointment")
		boton_cita.click()
		print("Appointment booked succesfully!")

			
		
