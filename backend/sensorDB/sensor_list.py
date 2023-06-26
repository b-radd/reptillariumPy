def sensorList():

    sensors = {
        # UV Sensors for UV Index
        "uv_1.2": {
            "name": "UV Sensor V2",
            "sensorType": "uv sensor",
            "pin": "A0",
        },
        "uv_2.2": {
            "name": "UV Sensor V2",
            "sensorType": "uv sensor",
            "pin": "A1",
        },
        # DHT22 Sensors for Temperature and Humidity
        "th_1.3": {
            "name": "DHT22",
            "sensorType": "humidity & temperature sensor",
            "pin": "D33",
        },
        "th_2.3": {
            "name": "DHT22",
            "sensorType": "humidity & temperature sensor",
            "pin": "D43",
        },
        # OneWire Temperature Sensors
        "t_1.1": {
            "name": "DS18B20 OneWire",
            "sensorType": "temperature sensor",
            "pin": "D31",
        },
        "t_1.4": {
            "name": "DS18B20 OneWire",
            "sensorType": "temperature sensor",
            "pin": "D34",
        },
        "t_2.1": {
            "name": "DS18B20 OneWire",
            "sensorType": "temperature sensor",
            "pin": "D41",
        },
        "t_2.4": {
            "name": "DS18B20 OneWire",
            "sensorType": "temperature sensor",
            "pin": "D44",
        },
        # Relays to Switch On/Off Lights and Heating Elements
        # "relay1_1": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D22",
        # },
        # "relay1_2": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D23",
        # },
        #
        # "relay1_3": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D24",
        # },
        # "relay1_4": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D25",
        # },
        # "relay2_1": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D26",
        # },
        # "relay2_2": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D27",
        # },
        # "relay2_3": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D28",
        # },
        # "relay2_4": {
        #     "name": "4 Channel Relay",
        #     "sensorType": "relay",
        #     "pin": "D29",
        # },
    }

    return sensors

