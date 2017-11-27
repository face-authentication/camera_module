# coding: utf-8

from picamera.array import PiRGBArray
from picamera import PiCamera
import sys, os
import time
import cv2

from logging import getLogger, StreamHandler, INFO, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def main(args, env_conf, module_conf):
  logger.debug("## %s %s()", __file__, sys._getframe().f_code.co_name)
  logger.debug(args)
  logger.debug(env_conf)
  logger.debug(module_conf)
  camera, rawCapture = initialize(args, env_conf, module_conf)

  # get cascade
  cascPath = args.cascade_path
  faceCascade = cv2.CascadeClassifier(cascPath)

  # allow the camera to warmup
  time.sleep(0.1)

  # capture frames from the camera
  for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
      gray,
      scaleFactor=1.1,
      minNeighbors=5,
      minSize=(30, 30),
      flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
      cv2.rectangle( image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
      break

def initialize(args, env_conf, module_conf):
  """
  カメラの初期設定を行う。
  """

  camera = PiCamera()
  camera.resolution = (module_conf["window"]["size"]["x"], module_conf["window"]["size"]["y"])
  camera.framerate = module_conf["camera"]["framerate"]
  rawCapture = PiRGBArray(camera, size=(module_conf["window"]["size"]["x"], module_conf["window"]["size"]["y"]))

  return camera, rawCapture


