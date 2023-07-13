from PIL import Image
from ultralytics import YOLO

from src.utils.tracker import Tracker

model_path = "E:/AllProject/dronetrackingyolo/src/model/weights/best.pt"
model = YOLO(model_path)
video_path = "E:/AllProject/dronetrackingyolo/src/runsvideos/video.mp4"
video_input_path = "E:/AllProject/dronetrackingyolo/src/inputvideos/inputvideo.mp4"
image_path = "E:/AllProject/dronetrackingyolo/src/runs/image.png"
tracker = Tracker()

outputs = {
    "predictions": []
}

"""
image_input = Image.new("RGB", (500, 500))  # Get image detect


def initialize_outputs_content():
    global outputs, image_input

    outputs = {
    "predictions": []
}

image_input = Image.new("RGB", (500, 500))  


"""

