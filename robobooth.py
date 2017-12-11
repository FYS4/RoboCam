from gpiozero import Button
import pygame.camera
from time import gmtime, strftime

def next_overlay():
    print("Next overlay")

def take_picture():
    pygame_camera_capture = (output)
    pygame_camera_stop_preview = ()
    print("Picture has been taken")


next_overlay_btn = Button(23)
take_pic_btn = Button(25)

next_overlay_btn.when_pressed = next_overlay

take_pic_btn.when_pressed = take_picture
pygame.camera.init()
camera = pygame.camera.Camera("/dev/video0")
camera_resolution = (640, 480)
camera_hflip = True
camera.start()
camera_start_preview = ()
camera_get_image = ()
pygame_image_save = ("robobooth.jpg")
output = strftime ("/home/pi/robobooth/image-%d-%m %H:%M.jpg", gmtime())







