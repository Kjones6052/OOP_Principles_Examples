class Smartphone:
    def __init__(self, model, serial_number):
        self.model = model 
        self.__serial_number = serial_number

    def get_serial_number(self):
        return self.__serial_number

    def set_serial_number(self, new_number):
        self.__serial_number = new_number

my_phone = Smartphone("Pixel 5", "123456ABC")

print(f"Serial Number: {my_phone.get_serial_number()}")

my_phone.set_serial_number("98765XYZ")
print(f"Updated Serial Number: {my_phone.get_serial_number()}")