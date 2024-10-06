class Smartphone:
    def __init__(self, model, __serial_number, operating_system):
        self.model = model # Public Attribute
        self.__serial_number = serial_number # Private Attribute
        self._operating_system = operating_system # Protected Attribute

    def show_info(self):
        print(f"Model: {self.model}")
        print("Serial Number: Hidden for security")
        print(f"Operating System: {self._operating_system}")

my_phone = Smartphone("Pixel 5", "123456ABC", "Android")

print(my_phone.model)