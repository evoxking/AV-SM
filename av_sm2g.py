import sys
import time
import random
import threading
from collections import deque
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer

# Yapay zeka denetleyici fonksiyonu
def ai_check(data):
    for key, value in data.items():
        if isinstance(value, (int, float)):
            if value < -10000 or value > 10000:
                return False
        elif isinstance(value, dict):
            if not ai_check(value):
                return False
    return True

# Sensor data class
class SensorData:
    def __init__(self):
        self.altitude = 0.0
        self.speed = 0.0
        self.position = (0.0, 0.0, 0.0)
        self.temperature = 0.0
        self.pressure = 0.0
        self.gyro = (0.0, 0.0, 0.0)
        self.accelerometer = (0.0, 0.0, 0.0)
        self.magnetometer = (0.0, 0.0, 0.0)
        self.weather = {"wind_speed": 0.0, "wind_direction": 0.0, "humidity": 0.0}
        self.fuel_level = 100.0
        self.engine_status = "ON"
        self.oil_pressure = 0.0
        self.hydraulic_pressure = 0.0
        self.battery_temperature = 0.0
        self.system_voltage = 0.0

    def update(self):
        self.altitude = random.uniform(1000, 10000)
        self.speed = random.uniform(200, 800)
        self.position = (
            random.uniform(-180, 180),
            random.uniform(-90, 90),
            random.uniform(0, 10000)
        )
        self.temperature = random.uniform(-50, 50)
        self.pressure = random.uniform(950, 1050)
        self.gyro = (
            random.uniform(-180, 180),
            random.uniform(-180, 180),
            random.uniform(-180, 180)
        )
        self.accelerometer = (
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            random.uniform(-10, 10)
        )
        self.magnetometer = (
            random.uniform(-100, 100),
            random.uniform(-100, 100),
            random.uniform(-100, 100)
        )
        self.weather["wind_speed"] = random.uniform(0, 100)
        self.weather["wind_direction"] = random.uniform(0, 360)
        self.weather["humidity"] = random.uniform(0, 100)
        self.fuel_level -= random.uniform(0.01, 0.1)
        self.fuel_level = max(self.fuel_level, 0)
        self.oil_pressure = random.uniform(20, 100)
        self.hydraulic_pressure = random.uniform(1000, 3000)
        self.battery_temperature = random.uniform(20, 50)
        self.system_voltage = random.uniform(24, 28)

        if ai_check(self.__dict__):
            print("Sensor data AI check passed")
        else:
            print("Sensor data AI check failed")

# Flight control system
class FlightControlSystem:
    def __init__(self):
        self.control_commands = {"pitch": 0.0, "roll": 0.0, "yaw": 0.0}
        self.error_history = deque(maxlen=10)

    def update(self, sensor_data):
        self.control_commands["pitch"] = self.calculate_pitch(sensor_data)
        self.control_commands["roll"] = self.calculate_roll(sensor_data)
        self.control_commands["yaw"] = self.calculate_yaw(sensor_data)

        if ai_check(self.control_commands):
            print("Flight control AI check passed")
        else:
            print("Flight control AI check failed")

    def calculate_pitch(self, sensor_data):
        return sensor_data.altitude / 10000

    def calculate_roll(self, sensor_data):
        return sensor_data.speed / 800

    def calculate_yaw(self, sensor_data):
        return sensor_data.position[0] / 180

    def get_commands(self):
        return self.control_commands

# Navigation system
class NavigationSystem:
    def __init__(self):
        self.destination = (50.0, 50.0, 10000.0)
        self.current_position = (0.0, 0.0, 0.0)
        self.route = []
        self.error_history = deque(maxlen=10)

    def update(self, sensor_data):
        self.current_position = sensor_data.position
        self.plan_route()
        self.follow_route()

        if ai_check({"current_position": self.current_position, "route": self.route}):
            print("Navigation AI check passed")
        else:
            print("Navigation AI check failed")

    def plan_route(self):
        self.route = [self.current_position, self.destination]

    def follow_route(self):
        pass

    def get_route(self):
        return self.route

# Built-In Test Equipment (BITE)
class BITE:
    def __init__(self):
        self.status = "OK"
        self.error_log = []

    def perform_test(self):
        if random.choice([True, False]):
            self.status = "OK"
        else:
            self.status = "ERROR"
            self.error_log.append("Error detected at " + time.strftime("%Y-%m-%d %H:%M:%S"))

        if ai_check({"status": self.status, "error_log": self.error_log}):
            print("BITE AI check passed")
        else:
            print("BITE AI check failed")

    def get_status(self):
        return self.status

    def get_error_log(self):
        return self.error_log

# Communication system
class CommunicationSystem:
    def __init__(self):
        self.message_log = []

    def send_message(self, message):
        self.message_log.append(f"Sent: {message}")
        print(f"Communication: Sent message - {message}")

    def receive_message(self):
        if random.choice([True, False]):
            message = "Received: Acknowledgment"
            self.message_log.append(message)
            print(f"Communication: {message}")
            return message
        return None

    def get_message_log(self):
        return self.message_log

    def ai_check_messages(self):
        if ai_check({"message_log": self.message_log}):
            print("Communication AI check passed")
        else:
            print("Communication AI check failed")

# Power management system
class PowerManagementSystem:
    def __init__(self):
        self.battery_level = 100.0
        self.power_consumption = 0.0

    def update(self):
        self.power_consumption = random.uniform(0.1, 5.0)
        self.battery_level -= self.power_consumption * 0.01
        self.battery_level = max(self.battery_level, 0)

        if ai_check({"battery_level": self.battery_level, "power_consumption": self.power_consumption}):
            print("Power management AI check passed")
        else:
            print("Power management AI check failed")

    def get_power_status(self):
        return {
            "battery_level": self.battery_level,
            "power_consumption": self.power_consumption
        }

# Data logger for recording sensor data
class DataLogger:
    def __init__(self):
        self.log = []

    def log_data(self, sensor_data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "sensor_data": {
                "altitude": sensor_data.altitude,
                "speed": sensor_data.speed,
                "position": sensor_data.position,
                "temperature": sensor_data.temperature,
                "pressure": sensor_data.pressure,
                "gyro": sensor_data.gyro,
                "accelerometer": sensor_data.accelerometer,
                "magnetometer": sensor_data.magnetometer,
                "weather": sensor_data.weather,
                "fuel_level": sensor_data.fuel_level,
                "engine_status": sensor_data.engine_status,
                "oil_pressure": sensor_data.oil_pressure,
                "hydraulic_pressure": sensor_data.hydraulic_pressure,
                "battery_temperature": sensor_data.battery_temperature,
                "system_voltage": sensor_data.system_voltage
            }
        }
        self.log.append(entry)
        print(f"DataLogger: Logged data at {timestamp}")

    def get_log(self):
        return self.log

    def ai_check_log(self):
        if ai_check({"log": self.log}):
            print("Data logger AI check passed")
        else:
            print("Data logger AI check failed")

# Security system for monitoring and responding to threats
class SecuritySystem:
    def __init__(self):
        self.threat_level = "LOW"
        self.threat_log = []

    def update(self):
        if random.choice([True, False]):
            self.threat_level = random.choice(["LOW", "MEDIUM", "HIGH"])
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.threat_log.append(f"Threat detected at {timestamp}: Level {self.threat_level}")
            print(f"SecuritySystem: Threat level {self.threat_level} detected at {timestamp}")

        if ai_check({"threat_level": self.threat_level, "threat_log": self.threat_log}):
            print("Security system AI check passed")
        else:
            print("Security system AI check failed")

    def get_threat_level(self):
        return self.threat_level

    def get_threat_log(self):
        return self.threat_log

# Error management system for handling errors and alerts
class ErrorManagementSystem:
    def __init__(self):
        self.error_log = []

    def log_error(self, error_message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.error_log.append(f"{timestamp}: {error_message}")
        print(f"ErrorManagement: {error_message} logged at {timestamp}")

    def get_error_log(self):
        return self.error_log

    def ai_check_errors(self):
        if ai_check({"error_log": self.error_log}):
            print("Error management AI check passed")
        else:
            print("Error management AI check failed")

# Maintenance and fault reporting system
class MaintenanceSystem:
    def __init__(self):
        self.maintenance_log = []

    def log_maintenance(self, maintenance_message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.maintenance_log.append(f"{timestamp}: {maintenance_message}")
        print(f"MaintenanceSystem: {maintenance_message} logged at {timestamp}")

    def get_maintenance_log(self):
        return self.maintenance_log

    def schedule_maintenance(self, component, date):
        maintenance_message = f"Scheduled maintenance for {component} on {date}"
        self.log_maintenance(maintenance_message)

    def ai_check_maintenance(self):
        if ai_check({"maintenance_log": self.maintenance_log}):
            print("Maintenance AI check passed")
        else:
            print("Maintenance AI check failed")

# Flight scenario management system
class FlightScenario:
    def __init__(self):
        self.scenario_log = []

    def simulate_scenario(self):
        scenarios = [
            "Normal flight",
            "Engine failure",
            "Hydraulic system failure",
            "Extreme weather",
            "Navigation system error",
            "Low fuel"
        ]
        scenario = random.choice(scenarios)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.scenario_log.append(f"{timestamp}: {scenario}")
        print(f"FlightScenario: {scenario} at {timestamp}")

    def get_scenario_log(self):
        return self.scenario_log

    def ai_check_scenarios(self):
        if ai_check({"scenario_log": self.scenario_log}):
            print("Flight scenario AI check passed")
        else:
            print("Flight scenario AI check failed")

# Avionics Mission Computer
class AvionicsMissionComputer:
    def __init__(self):
        self.sensor_data = SensorData()
        self.flight_control_system = FlightControlSystem()
        self.navigation_system = NavigationSystem()
        self.bite = BITE()
        self.communication_system = CommunicationSystem()
        self.power_management_system = PowerManagementSystem()
        self.data_logger = DataLogger()
        self.security_system = SecuritySystem()
        self.error_management_system = ErrorManagementSystem()
        self.maintenance_system = MaintenanceSystem()
        self.flight_scenario = FlightScenario()
        self.backup_sensor_data = SensorData()
        self.running = True
        self.failover = False
        self.flight_mode = "NORMAL"

    def sensor_data_task(self):
        while self.running:
            try:
                self.sensor_data.update()
                self.data_logger.log_data(self.sensor_data)
                time.sleep(0.01)
            except Exception as e:
                error_message = f"Sensor Data Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)
                self.failover = True

    def backup_sensor_data_task(self):
        while self.running:
            try:
                self.backup_sensor_data.update()
                if self.failover:
                    self.sensor_data = self.backup_sensor_data
                    self.failover = False
                    print("Failover to backup sensor data")
                time.sleep(0.01)
            except Exception as e:
                error_message = f"Backup Sensor Data Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def flight_control_task(self):
        while self.running:
            try:
                self.flight_control_system.update(self.sensor_data)
                time.sleep(0.01)
            except Exception as e:
                error_message = f"Flight Control Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def navigation_task(self):
        while self.running:
            try:
                self.navigation_system.update(self.sensor_data)
                time.sleep(0.01)
            except Exception as e:
                error_message = f"Navigation Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def bite_task(self):
        while self.running:
            try:
                self.bite.perform_test()
                if self.bite.get_status() == "ERROR":
                    print(f"BITE Error Log: {self.bite.get_error_log()}")
                    self.error_management_system.log_error("BITE Test Failed")
                time.sleep(10)
            except Exception as e:
                error_message = f"BITE Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def communication_task(self):
        while self.running:
            try:
                self.communication_system.send_message("Flight data update")
                received_message = self.communication_system.receive_message()
                time.sleep(2)
            except Exception as e:
                error_message = f"Communication Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def power_management_task(self):
        while self.running:
            try:
                self.power_management_system.update()
                time.sleep(3)
            except Exception as e:
                error_message = f"Power Management Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def security_task(self):
        while self.running:
            try:
                self.security_system.update()
                time.sleep(5)
            except Exception as e:
                error_message = f"Security System Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def monitor_flight_mode(self):
        while self.running:
            try:
                if self.sensor_data.altitude > 9000 and self.flight_mode != "HIGH_ALTITUDE":
                    self.flight_mode = "HIGH_ALTITUDE"
                    print(f"Flight mode changed to {self.flight_mode}")
                elif self.sensor_data.altitude <= 9000 and self.flight_mode != "NORMAL":
                    self.flight_mode = "NORMAL"
                    print(f"Flight mode changed to {self.flight_mode}")
                time.sleep(1)
            except Exception as e:
                error_message = f"Flight Mode Monitoring Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def maintenance_task(self):
        while self.running:
            try:
                if self.sensor_data.fuel_level < 10:
                    self.maintenance_system.log_maintenance("Fuel level low, schedule refueling.")
                if self.sensor_data.oil_pressure < 30:
                    self.maintenance_system.log_maintenance("Oil pressure low, schedule maintenance.")
                if self.sensor_data.battery_temperature > 45:
                    self.maintenance_system.log_maintenance("Battery temperature high, schedule cooling.")
                if self.sensor_data.system_voltage < 24:
                    self.maintenance_system.log_maintenance("System voltage low, schedule check.")
                time.sleep(5)
            except Exception as e:
                error_message = f"Maintenance System Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def flight_scenario_task(self):
        while self.running:
            try:
                self.flight_scenario.simulate_scenario()
                time.sleep(15)
            except Exception as e:
                error_message = f"Flight Scenario Error: {e}"
                print(error_message)
                self.error_management_system.log_error(error_message)

    def start(self):
        self.sensor_thread = threading.Thread(target=self.sensor_data_task)
        self.backup_sensor_thread = threading.Thread(target=self.backup_sensor_data_task)
        self.flight_control_thread = threading.Thread(target=self.flight_control_task)
        self.navigation_thread = threading.Thread(target=self.navigation_task)
        self.bite_thread = threading.Thread(target=self.bite_task)
        self.communication_thread = threading.Thread(target=self.communication_task)
        self.power_management_thread = threading.Thread(target=self.power_management_task)
        self.security_thread = threading.Thread(target=self.security_task)
        self.flight_mode_thread = threading.Thread(target=self.monitor_flight_mode)
        self.maintenance_thread = threading.Thread(target=self.maintenance_task)
        self.flight_scenario_thread = threading.Thread(target=self.flight_scenario_task)

        self.sensor_thread.start()
        self.backup_sensor_thread.start()
        self.flight_control_thread.start()
        self.navigation_thread.start()
        self.bite_thread.start()
        self.communication_thread.start()
        self.power_management_thread.start()
        self.security_thread.start()
        self.flight_mode_thread.start()
        self.maintenance_thread.start()
        self.flight_scenario_thread.start()

    def stop(self):
        self.running = False
        self.sensor_thread.join()
        self.backup_sensor_thread.join()
        self.flight_control_thread.join()
        self.navigation_thread.join()
        self.bite_thread.join()
        self.communication_thread.join()
        self.power_management_thread.join()
        self.security_thread.join()
        self.flight_mode_thread.join()
        self.maintenance_thread.join()
        self.flight_scenario_thread.join()

# PyQt5 GUI
class AvionicsGUI(QMainWindow):
    def __init__(self, avionics_computer):
        super().__init__()
        self.avionics_computer = avionics_computer
        self.initUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)
        self.timer.start(10)

    def initUI(self):
        self.setWindowTitle('Avionics Mission Computer')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        self.altitude_label = QLabel('Altitude: 0')
        self.speed_label = QLabel('Speed: 0')
        self.fuel_level_label = QLabel('Fuel Level: 100')
        self.engine_status_label = QLabel('Engine Status: ON')
        self.oil_pressure_label = QLabel('Oil Pressure: 0')
        self.hydraulic_pressure_label = QLabel('Hydraulic Pressure: 0')
        self.battery_temperature_label = QLabel('Battery Temperature: 0')
        self.system_voltage_label = QLabel('System Voltage: 0')

        self.layout.addWidget(self.altitude_label)
        self.layout.addWidget(self.speed_label)
        self.layout.addWidget(self.fuel_level_label)
        self.layout.addWidget(self.engine_status_label)
        self.layout.addWidget(self.oil_pressure_label)
        self.layout.addWidget(self.hydraulic_pressure_label)
        self.layout.addWidget(self.battery_temperature_label)
        self.layout.addWidget(self.system_voltage_label)

    def update_display(self):
        sensor_data = self.avionics_computer.sensor_data
        self.altitude_label.setText(f'Altitude: {sensor_data.altitude:.2f}')
        self.speed_label.setText(f'Speed: {sensor_data.speed:.2f}')
        self.fuel_level_label.setText(f'Fuel Level: {sensor_data.fuel_level:.2f}')
        self.engine_status_label.setText(f'Engine Status: {sensor_data.engine_status}')
        self.oil_pressure_label.setText(f'Oil Pressure: {sensor_data.oil_pressure:.2f}')
        self.hydraulic_pressure_label.setText(f'Hydraulic Pressure: {sensor_data.hydraulic_pressure:.2f}')
        self.battery_temperature_label.setText(f'Battery Temperature: {sensor_data.battery_temperature:.2f}')
        self.system_voltage_label.setText(f'System Voltage: {sensor_data.system_voltage:.2f}')

if __name__ == "__main__":
    avionics_computer = AvionicsMissionComputer()
    avionics_computer.start()

    app = QApplication(sys.argv)
    gui = AvionicsGUI(avionics_computer)
    gui.show()
    sys.exit(app.exec_())
