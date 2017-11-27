# coding: utf-8
import os, sys
import json, re

from logging import getLogger, StreamHandler, INFO, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def read_config(config_path):
  """
  設定ファイルを読み込む。指定がない場合は、デフォルトの設定ファイルを読み込む。
  @param config_path - configファイルのパス
  @return 読み込んだ設定ファイルのdict型オブジェクト
  """
  logger.debug("## %s %s()", __file__, sys._getframe().f_code.co_name)
  logger.debug(config_path)

  # 指定がない場合
  if config_path == None:
    return None

  r_file = open(config_path, 'r')
  j_dict = json.load(r_file)

  return j_dict

def read_file(file_path):
  """
  ファイルを読み込んで一行ずつyieldで返す
  //が先頭についている行は対象外とする。
  @param file_path 読み込むファイルのパス
  @yield (行番号、読み込んだ行内容)
  """
  logger.debug("## %s %s()", __file__, sys._getframe().f_code.co_name)

  for (i, line) in enumerate(open(file_path, 'r')):
    if re.match(r"\/\/", line) == None:
      yield(i, line)
