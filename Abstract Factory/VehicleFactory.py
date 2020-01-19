from Factories.CarFactory import CarFactory
from Factories.BusFactory import BusFactory

car_factory = CarFactory()
bus_factory = BusFactory()


class VehicleStore:
	def __init__(self, vehicle_type=None):
		self._vehicle_type = vehicle_type

	def drive(self):
		if self._vehicle_type:
			return self._vehicle_type.get().drive()
		return "No Vehicles Found."

	def get_mileage(self, name, mileage):
		if self._vehicle_type:
			return self._vehicle_type.get().get_mileage(name, mileage)


car = VehicleStore(car_factory)
print({"response": car.drive()})
print({"response": car.get_mileage("Suzuki", "20")})

print("========================================================")

bus = VehicleStore(bus_factory)
print({"response": bus.drive()})
print({"response": bus.get_mileage("Suzuki", "20")})
