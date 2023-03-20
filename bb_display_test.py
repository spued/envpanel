#!/usr/bin/python3
import time

from rgbmatrix import graphics,  RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
#options.hardware_mapping = self.args.led_gpio_mapping
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 3
#options.row_address_type = self.args.led_row_addr_type
options.multiplexing = 4
options.pwm_bits = 11
options.brightness = 10
#options.pwm_lsb_nanoseconds = self.args.led_pwm_lsb_nanoseconds
#options.led_rgb_sequence = self.args.led_rgb_sequence
#options.pixel_mapper_config = self.args.led_pixel_mapper
#options.show_refresh_rate = 1
options.gpio_slowdown = 4
#options.disable_hardware_pulsing = True
matrix = RGBMatrix(options = options)

offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("fonts/7x13.bdf")
yellow = graphics.Color(255, 255, 0)
white = graphics.Color(255, 255, 255)
blue = graphics.Color(0, 0, 255)
pink = graphics.Color(255,192,203)
black = graphics.Color(0,0,0)
pos = offscreen_canvas.width
my_text = 'default'

print('AA Env display start...')

def DrawRectangle(canvas,x1,y1,x2,y2,color):
    graphics.DrawLine(canvas,x1,y1,x2,y1, color)
    graphics.DrawLine(canvas,x2,y1,x2,y2, color)
    graphics.DrawLine(canvas,x1,y2,x2,y2, color)
    graphics.DrawLine(canvas,x1,y1,x1,y2, color)

def DrawFillRectangle(canvas,x1,y1,x2,y2,color):
    for y in range(y1,y2+1):
        for x in range(x1,x2):
            graphics.DrawLine(canvas,x1,y,x2,y,color)

while True:
    offscreen_canvas.Clear()
    DrawFillRectangle(offscreen_canvas,0,0,95,47,blue)
    #DrawFillRectangle(offscreen_canvas,0,0,95,15,pink)
    DrawRectangle(offscreen_canvas,0,32,95,47,white)
    len = graphics.DrawText(offscreen_canvas, font, pos, 10, black, my_text)
    pos -= 1
    if (pos + len < 0):
       pos = offscreen_canvas.width
    time.sleep(0.5)
    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
