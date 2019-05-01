import time
import Adafruit_DHT as dht

sensor1 = 22
pin1 = 14
sensor2 = 11
pin2 = 4

while True:
    humidity, temperature = dht.read_retry(sensor1, pin1)
    if (humidity is not None) and (temperature is not None):
        temperature = str(temperature)
        humidity = str(humidity)
        print("============================DHT22=========================")
        print("����������� " + temperature + "C  " + "�������� " + humidity +"%")
        humidity, temperature = dht.read_retry(sensor2, pin2)
        temperature = str(temperature)
        humidity = str(humidity)
        print("============================DHT11=========================")
        print("����������� " + temperature + "2C  " + "�������� " + humidity +"2%")
        time.sleep(2)
