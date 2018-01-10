from gpiozero import Button
import pygame.camera
import pygame.image
from time import gmtime, strftime
from overlay_functions import *

def next_overlay():
    global overlay
    overlay = next(all_overlays)
    preview_overlay(camera, overlay)

def take_picture():
          camera_capture = ()
          camera_stop_preview = ()
          print("pic")

next_overlay_btn = Button(23)
take_pic_btn = Button(25)

next_overlay_btn.when_pressed = next_overlay
take_pic_btn.when_pressed = take_picture
pygame.camera.init()
camera = pygame.camera.Camera("/dev/video0")
camera_resution = (800, 480)
camera_hflip = True
camera.start()
camera_start_preview = ()
image = camera.get_image()
pygame.image.save((image), "photo.png")
output = (('strf_time'),"/home/pi/robobooth/image-%d-%m- %H:%M.png", (gmtime))





