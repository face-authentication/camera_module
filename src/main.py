# coding: utf-8
import os, sys
import argparse

from logging import getLogger, StreamHandler, INFO, DEBUG

import commons.functions as common
import modules.pycamera as py_camera

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def main(args):
  """
  最初に実行される関数.
  @param args コンソールで渡された引数をdict型にしたもの
  """

  # 設定ファイルをロード
  env_conf = common.read_config(os.path.abspath(os.path.dirname(__file__)) + "/../config/" + args.environments)
  module_conf = common.read_config(os.path.abspath(os.path.dirname(__file__)) + "/../config/" + args.module_name + ".json")

  # ラズパイ用カメラモジュールの処理
  if args.module_name == "pycamera":
    py_camera.main(args, env_conf[args.stage], module_conf);

if __name__ == '__main__':
  # 引数のチェック、dictの作成
  parser = argparse.ArgumentParser()

  parser.add_argument("-module_name", "-m", help="please input module_name", required=True)
  parser.add_argument("-program_name", "-p", help="please input program_name", required=False)
  parser.add_argument("-environments", "-e", help="example ... environments.json", default="environments.json")
  parser.add_argument("-stage", "-s", help="local, staging, production", default="local")

  parser.add_argument("-cascade_path", "-c", help="", default="files/cascades/haarcascade_frontalface_default.xml")

  args = parser.parse_args()

  # main実行
main(args)
