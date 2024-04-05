from cura.health_care import Appointment
import time

with Appointment() as cita:
	cita.land_first_page()
	cita.make_appointment()
	cita.login()
	cita.select_facility()
	cita.select_date("5/4/2024")



time.sleep(3000)
