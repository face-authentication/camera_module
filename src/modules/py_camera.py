from picamera.array import PiRGBArray
from picamera import PiCamera
import sys, os
import time
import cv2

def main(args, env_conf, module_conf):
  camera = initialize(args, env_conf, module_conf)

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
  camera.resolution = (module_conf.window.size.x, module_conf.window.size.y)
  camera.framerate = module_conf.camera.framerate
  rawCapture = PiRGBArray(camera, size=(module_conf.window.size.x, module_conf.window.size.y))

  cascPath = args.cascade_path
  faceCascade = cv2.CascadeClassifier(cascPath)

  return camera