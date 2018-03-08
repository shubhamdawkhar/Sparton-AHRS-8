import serial
import time as tim
import datetime

def time():
    t =  datetime.datetime.now()
    t = str(t)
    t = t[17:]
    t = float(t)
    return t

def portdetect():
    port = "/dev/ttyUSB"
    p = 0
    flag = 0
    while flag == 0:
        try:
            tim.sleep(0.01)
            port = port + str(p)
            serimu = serial.Serial(port,baudrate=115200)
            t = time()
            while flag == 0 and t-time() < 0.1:
                serimu.write("yaw di.\r\n")
                t = time()
                while abs(t-time() < 0.01) and flag == 0 : 
                    read = serimu.readline()
                    for line in read.split('\r') :
                        if line.startswith ("yaw ="):
                            yaw = line.split("=")
                            yaw = float(yaw[1])         
                            flag = 1
        except:
            p = p+1
            port = "/dev/ttyUSB"
    return port

def serimu():
    port = portdetect()
    return serial.Serial(port,baudrate=115200)

def sergps():
    return serial.Serial(port='/dev/ttyUSB0',baudrate=38400)

def serard():
    return serial.Serial(port='/dev/ttyACM0',baudrate=115200)
