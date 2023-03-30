#!/usr/bin/env python3
import time
import sqlite3 

from datetime import datetime
from rgbmatrix import graphics,  RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics,  RGBMatrix, RGBMatrixOptions

def get_db_connection():
    conn = sqlite3.connect('/home/sunya/envpanel/database.db')
    conn.row_factory = sqlite3.Row
    return conn

now = datetime.now() # current date and time
date_time = now.strftime("%a %d %b %Y %H:%M")
hour = int(now.strftime("%H"))
p_brightness = "50"
# get brightness time
conn = get_db_connection()
rows = conn.execute('SELECT brightness FROM setting_data LIMIT 1').fetchone()[0]
brightness = str(rows).split(",")
#print(brightness)

if( 0 < hour <= 6):
  p_brightness = brightness[4]
elif( 6 < hour <= 8):
  p_brightness = brightness[0]
elif( 8 < hour <= 12):
  p_brightness = brightness[1]
elif( 12 < hour <= 17):
  p_brightness = brightness[2]
elif( 17 < hour <= 23):
  p_brightness = brightness[3]
else:
  p_brightness = "25"

conn.close()

#print( hour, p_brightness)
options = RGBMatrixOptions()
#options.hardware_mapping = self.args.led_gpio_mapping
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 3
#options.row_address_type = self.args.led_row_addr_type
options.multiplexing = 4
options.pwm_bits = 11
options.brightness = int(p_brightness)
#options.pwm_lsb_nanoseconds = self.args.led_pwm_lsb_nanoseconds
#options.led_rgb_sequence = self.args.led_rgb_sequence
#options.pixel_mapper_config = self.args.led_pixel_mapper
#options.show_refresh_rate = 1
options.gpio_slowdown = 4
#options.disable_hardware_pulsing = True
matrix = RGBMatrix(options = options)

offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("/home/sunya/envpanel/fonts/7x13.bdf")
font_small = graphics.Font()
font_small.LoadFont("/home/sunya/envpanel/fonts/5x8.bdf")
font_big = graphics.Font()
font_big.LoadFont("/home/sunya/envpanel/fonts/8x13B.bdf")

yellow = graphics.Color(190, 198, 16)
white = graphics.Color(180, 180, 255)
half_white = graphics.Color(90, 90, 128)
cyan = graphics.Color(0, 255, 255)
magenta = graphics.Color(190, 0, 190)
green = graphics.Color(0, 198, 32)
dark_green = graphics.Color(10, 56, 16)
pink = graphics.Color(190, 128, 160)
blue = graphics.Color(0, 16, 255)
navy = graphics.Color(8, 16, 86)
black = graphics.Color(0, 0, 0)
orange = graphics.Color(255, 128, 0)
red = graphics.Color(255, 0, 0)
dark_red = graphics.Color(64, 0, 0)

day_colors = [red,yellow,pink,green,orange,blue,magenta]

pos = offscreen_canvas.width

def DrawRectangle(canvas,x1,y1,x2,y2,color):
    graphics.DrawLine(canvas,x1,y1,x2,y1, color)
    graphics.DrawLine(canvas,x2,y1,x2,y2, color)
    graphics.DrawLine(canvas,x1,y2,x2,y2, color)
    graphics.DrawLine(canvas,x1,y1,x1,y2, color)

def DrawFillRectangle(canvas,x1,y1,x2,y2,color):
    for y in range(y1,y2+1):
        for x in range(x1,x2):
            graphics.DrawLine(canvas,x1,y,x2,y,color)

def DrawFrameRectangle(canvas,x1,y1,x2,y2,color):
    DrawRectangle(canvas,x1,y1,x2,y2,color)
    DrawRectangle(canvas,x1+1,y1+1,x2-1,y2-1,color)
    #DrawRectangle(canvas,x1+2,y1+2,x2-2,y2-2,color)

display_message = 'Starting ...'
month_name_full = ["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน","กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]
month_name_brief = ["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]
day_name_full = ["วันจันทร์", "งันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์", "วันอาทิตย์"]
day_name_half = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
day_name_brief = ["จ", "อ", "พ", "พฤ", "ศ", "ส", "อ"]
msg = ["พีเอ็ม25", "พีเอ็ม10", "อุณหภูมิ", "ความชื้น", "เสียง"]

read_round = 0
show_round = 0
show_number = 0

day_number = 0
month_number = 0

#msg_values = ["{0} PPM".format(val[3]), "{0} PPM".format(val[4]), "{0} C".format(val[1]/10), "{0} %".format(val[0]/10), "{0:.1f}dB".format(val[2]/10) ]
conn = get_db_connection()
env_rows = conn.execute('SELECT * FROM env_data ORDER BY id LIMIT 1').fetchone()
msg_values = ["{0:.0f} PPM".format(env_rows['pm25']), "{0:.0f} PPM".format(env_rows['pm10']), "{0} C".format(env_rows['temperature']), 
    "{0} %".format(env_rows['humidity']), "{0:.1f}dB".format(env_rows['noise']) ]
#print(msg_values)
conn.close()
print('AA Env display start...')
while True:
    #time.sleep(1)
    if (read_round > 500):
        #print("Read sensors :",val)
        # read data from db
        conn = get_db_connection()
        env_rows = conn.execute('SELECT * FROM env_data ORDER BY id LIMIT 1').fetchone()
        msg_values = ["{0:.0f} PPM".format(env_rows['pm25']), "{0:.0f} PPM".format(env_rows['pm10']), "{0} C".format(env_rows['temperature']),
            "{0} %".format(env_rows['humidity']), "{0:.1f}dB".format(env_rows['noise']) ]
        conn.close()
        read_round = 0
    now = datetime.now() # current date and time
    date_message = now.strftime("%A").upper()
    date_message_2 = now.strftime("%d/%m/%Y")
    day_number = int(now.strftime("%w"))
    #date_message_t = day_name_brief[day_number]
    #month_number = int(now.strftime("%m"))-1
    #date_message_2_t = now.strftime("%d ") + month_name_brief[month_number] + str(int(now.strftime("%Y")) + 543)
    time_message = now.strftime("%H:%M")

    offscreen_canvas.Clear()
    DrawFillRectangle(offscreen_canvas, 0, 0, 95, 47, navy)
    DrawRectangle(offscreen_canvas, 0, 0, 95, 15, white)
    DrawFillRectangle(offscreen_canvas, 0, 16, 95, 29, dark_green)
    DrawRectangle(offscreen_canvas, 0, 29, 95, 47, half_white)
    graphics.DrawText(offscreen_canvas, font_small, 2, 7, day_colors[day_number], date_message)
    graphics.DrawText(offscreen_canvas, font_small, 2, 14, cyan, date_message_2)
    graphics.DrawText(offscreen_canvas, font_big, 55, 13, orange, time_message)

    len1 = graphics.DrawText(offscreen_canvas, font, pos, 27, white, display_message)

    if(int(env_rows['pm25']) > 100):
        graphics.DrawText(offscreen_canvas, font, 2 , 42, red, msg[show_number])
        graphics.DrawText(offscreen_canvas, font, 51 , 43, red, msg_values[show_number])
    else :
        graphics.DrawText(offscreen_canvas, font, 2 , 42, green, msg[show_number])
        graphics.DrawText(offscreen_canvas, font, 51 , 43, green, msg_values[show_number])

    if (show_round > 200):
      hour = int(now.strftime("%H"))
      conn = get_db_connection()
      rows = conn.execute('SELECT * FROM posts').fetchall()
      for row in rows:
          _period = row['title'].split('-')
          _p_start = int(_period[0].replace(':00',''))
          _p_end = int(_period[1].replace(':00',''))
          #print(hour,_p_start,_p_end)
          if(_p_start < hour <= _p_end):
              #print('We show display: ', row['content']);
              display_message = str(row['content'])
      conn.close()
      show_round = 0
      show_number += 1
      if(show_number > 4):
          show_number = 0
    pos -= 1
    read_round += 1
    show_round += 1
    if (pos + len1 < 0):
       pos = offscreen_canvas.width
    time.sleep(0.05)
    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
