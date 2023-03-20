#!/usr/bin/env python3
import minimalmodbus
import serial
import sqlite3 

sensors = minimalmodbus.Instrument('/dev/ttyUSB0', 11)  #port and slave
sensors.serial.port
sensors.serial.baudrate = 4800
sensors.serial.parity = serial.PARITY_NONE
sensors.serial.bytesize = 8
sensors.serial.stopbits = 1
sensors.mode = minimalmodbus.MODE_RTU
sensors.serial.timeout = 0.2

#sensors.debug = True

def get_db_connection():
    conn = sqlite3.connect('/home/sunya/envpanel/database.db')
    conn.row_factory = sqlite3.Row
    return conn

val = sensors.read_registers(500,5,3)
msg_values = ["{0} PPM".format(val[3]), "{0} PPM".format(val[4]), "{0} C".format(val[1]/10), "{0} %".format(val[0]/10), "{0:.1f}dB".format(val[2]/10) ]
# insert data to db
conn = get_db_connection()
conn.execute("INSERT INTO env_data (pm25, pm10, temperature, humidity, noise) VALUES (?, ?, ?, ?, ?)",( val[3], val[4], val[1]/10, val[0]/10, val[2]/10 ))
conn.commit()
conn.close()
