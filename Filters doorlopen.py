from PIL import Image
from itertools import cycle

overlays_dir = "/home/pi/allseeinggpi/overlays"
overlays = ['blank','elvis','flowers','girl','glassesnose','moustache','music','sunglasses','top']

overlay = overlays[0]

def _get_overlay_image(overlay):
    return Image.open(overlays_dir + "/" + overlay + ".png")

    def _pad(resolution, width=32, height=16):
        return (
            ((resolution[0] + (width - 1)) //width) * width
            ((resolution[1] + (height - 1)) //height) * heigth,

        )

    def remove_overlays(camera):
        for overlay in camera_overlays:
            camera_remove_ovelay()
        def __Camera__():


              

          def preview_overlay(camera=None, overlay=None):
              remove_overlays(camera)
              overlay_img = _get_overlay_image(overlay)
              pad = Image.new('RGB', _pad(camera.resolution))
              pad.paste(overlay_img, (0, 0))
              camera.add_overlay(pad.tobytes(), alpha=128, layer=3)
    

        def output_overlay(output=None, overlay=None):
            overlay_img = _get_overlay_image(overlay)
            output_img = Image.open(output).convert('RGBA')
            new_output = Image.alpha_composite(output_img, overlay_img)
            new_output.savce(output)

            all_overlays = cycle(overlays)  
