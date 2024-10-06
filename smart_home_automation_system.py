
class SmartDevices:

    def turn_on(self):
        print("Smart Device is turning on.")

    def turn_off(self):
        print("Smart Device is turning off.")

    def reset(self):
        print("Smart Device is resetting.")

class SmartLight(SmartDevices):

    def turn_on(self):
        print("Smart Light is brightening.")

    def turn_off(self):
        print("Smart Light is dimming.")

class SmartThermostat(SmartDevices):

    def turn_on(self):
        print("Smart Thermostat is heating up.")

    def turn_off(self):
        print("Smart Thermostat is cooling down.")

class SmartCamera(SmartDevices):

    def reset(self):
        print("Smart Camera is recalibrating focus and angle.")

def manage_device(device):
    action = input("Enter action (turn on/turn off/reset):")
    if action == "turn on":
        device.turn_on()
    elif action == "turn off":
        device.turn_off()
    elif action == "reset":
        device.reset()
    else:
        print("Invalid action")

def main():
    devices = {
        "light": SmartLight(),
        "thermostat": SmartThermostat(),
        "camera": SmartCamera()
        }
    while True:
        device_name = input("Enter device (light/thermostat/camera): ").lower()
        if device_name == "exit":
            break
        if device_name in devices:
            manage_device(devices[device_name])
        else:
            print("Device not found.")

if __name__ == "__main__":
    main()