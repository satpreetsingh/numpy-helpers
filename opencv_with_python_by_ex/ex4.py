import pprint
import cv2

color_spaces = []
for attr in dir(cv2):
    if attr.startswith("COLOR_"):
        color_spaces.append(attr)

pprint.pprint("Number of color spaces " + str(len(color_spaces)))
pprint.pprint(color_spaces)
