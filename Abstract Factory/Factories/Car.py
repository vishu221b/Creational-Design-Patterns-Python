class Car:
	def drive(self):
		return {"response":"Car is being driven!!"}

	def get_mileage(self, car_name, mileage):
		return {"response": "Mileage for car {} is {}".format(str(car_name), str(mileage))}