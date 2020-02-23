import serial
import datetime
import time as tim
import globalv
import csv
cmd_yaw = "yaw di.\r\n"
cmd_roll = "roll di.\r\n"
cmd_pitch = "pitch di.\r\n"
cmd_accelero = "accelp di.\r\n"
cmd_gyro = "gyrop di.\r\n"
cmd_temp = "temperature di.\r\n"

def time():
    t =  datetime.datetime.now()
    t = str(t)
    t = t[17:]
    t = float(t)
    return t

def yaw():
    serimu = globalv.serimu()
    flag = 0
    serimu.flush()
    while flag == 0:
        serimu.write(cmd_yaw)
        t = time()
        while abs(t-time() < 0.01) and flag == 0 : 
            read = serimu.readline()
            for line in read.split('\r') :
                if line.startswith ("yaw ="):
                    yaw = line.split("=")
                    yaw = float(yaw[1])
                    #print "yaw : "+str(yaw)
                    flag = 1
    return yaw

def roll():
    serimu = globalv.serimu()
    flag = 0
    serimu.flush()
    while flag == 0:
        serimu.write(cmd_roll)
        t = time()
        while abs(t-time() < 0.01) and flag == 0: 
            read = serimu.readline()
            for line in read.split('\r') :
                if line.startswith ("roll ="):
                    roll = line.split("=")
                    roll = float(roll[1])
                    #print "roll : "+str(roll)
                    flag = 1
    return roll

def pitch():
    serimu = globalv.serimu()
    flag = 0
    serimu.flush()
    while flag == 0:
        serimu.write(cmd_pitch)
        t = time()
        while abs(t-time() < 0.01) and flag == 0 : 
            read = serimu.readline()
            for line in read.split('\r') :
                if line.startswith ("pitch ="):
                    pitch = line.split("=")
                    pitch = float(pitch[1])
                    #print "pitch : "+str(pitch)
                    flag = 1
    return pitch

def gyro():
    serimu = globalv.serimu() 
    flagx = 0
    flagy = 0
    flagz = 0
    serimu.flush()
    while flagx == 0 or flagy == 0 or flagz == 0:
        serimu.write(cmd_gyro)
        t = time()
        while abs(t-time() < 0.01) and (flagx == 0 or flagy == 0 or flagz == 0) : 
            read = serimu.readline()
            for line in read.split('\r') :
                if line.startswith ("gyrop = 00--"):
                    gx = line.split("--")
                    gx = float(gx[1])
                    #print "gx : "+str(gx)
                    flagx = 1
                if line.startswith ("01--"):
                    gy = line.split("--")
                    gy = float(gy[1])
                    #print "gy : "+str(gy)
                    flagy = 1
                if line.startswith ("02--"):
                    gz = line.split("--")
                    gz = float(gz[1])
                    #print "gz : "+str(gz)
                    flagz = 1
    g = [gx,gy,gz]
    return g

def accelerometer():
    serimu = globalv.serimu()
    flagx = 0
    flagy = 0
    flagz = 0
    serimu.flush()
    while flagx == 0 or flagy == 0 or flagz == 0:
        serimu.write(cmd_accelero)
        t = time()
        while abs(t-time() < 0.01) and (flagx == 0 or flagy == 0 or flagz == 0) : 
            read = serimu.readline()
            for line in read.split('\r') :
                if line.startswith ("accelp = 00--"):
                    ax = line.split("--")
                    ax = float(ax[1])
                    #print "ax : "+str(ax)
                    flagx = 1
                if line.startswith ("01--"):
                    ay = line.split("--")
                    ay = float(ay[1])
                    #print "ay : "+str(ay)
                    flagy = 1
                if line.startswith ("02--"):
                    az = line.split("--")
                    az = float(az[1])
                    #print "az : "+str(az)
                    flagz = 1
        a = [ax,ay,az]
        return a
    
def temperature():
    serimu = globalv.serimu()
    flag = 0
    serimu.flush()
    while flag == 0:
        serimu.write(cmd_temp)
        t = time()
        while abs(t-time() < 0.01) and flag == 0 : 
            read = serimu.readline()
            for line in read.split('\r') :
                if line.startswith ("temperature ="):
                    temp = line.split("=")
                    temp = float(temp[1])
                    #print "temperature : "+str(temp)
                    flag = 1
    return temp
with open('imulog.csv', 'w') as file:
	fieldnames = ['ax', 'ay','az','yaw','pitch','roll', 'Gx', 'Gy', 'Gz']
	writer = csv.DictWriter(file, fieldnames=fieldnames)
	writer.writeheader()
	while(1):
		p = pitch()
		y = yaw()
		r = roll()
		g = gyro()
		print g
		a= accelerometer()
		writer.writerow({'ax':a[0], 'ay':a[1], 'az':a[2], 'yaw': y, 'pitch': p, 'roll': r,'Gx': g[0], 'Gy': g[1], 'Gz': g[2]})
