class Bus:
	def drive(self):
		return {"response": "Bus is being driven!"}

	def get_mileage(self, bus_name, mileage):
		return {"response": "Mileage for bus {} is {}".format(str(bus_name), str(mileage))}