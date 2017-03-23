#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
弹幕fm主程序
"""
import argparse
import gettext
import io
import json
import logging
import os
import re
import sys
import time
from .settings import ROOT_PROJECT_DIR
#from .cmd_config import config
# from threading import Thread
# import subprocess
from .client.douyu_client import DouyuClient
import traceback

APP_DESC = """
    _____                                ______ __  __
    |  __ \                              |  ____|  \/  |
    | |  | | __ _ _ __  _ __ ___  _   _  | |__  | \  / |
    | |  | |/ _` | '_ \| '_ ` _ \| | | | |  __| | |\/| |
    | |__| | (_| | | | | | | | | | |_| |_| |    | |  | |
    |_____/ \__,_|_| |_|_| |_| |_|\__,_(_)_|    |_|  |_|

                        ---- A Terminal Tools For DouyuTV

    @author Micheal Gardner (twocucao@gmail.com)
                                    last_update 2016-08-01 08:58
"""

logger = logging.getLogger('danmu.fm')
config={}

def check_setting_and_env():
    logger.info("程序正在启动,检查环境配置")
    if sys.version_info < (3, 2):
        raise RuntimeError("at least Python 3.3 is required!!")
    # Session = scoped_session(sessionmaker(bind=ENGINE))
    # s = Session()
    # try:
    #     rs_version = s.execute("SELECT VERSION();")
    #     version = rs_version.fetchone()[0]
    #     env_infomation = """\
    #     ------------------------------------------------------------
    #     PostgreSQL 版本信息 : {0}
    #     ------------------------------------------------------------
    #     """.format(version)
    #     print(env_infomation)
    #     Session.remove()
    # except sqlalchemy.exc.OperationalError as e:
    #     logger.error("没有初始化数据库")
    #     # 貌似没什么作用?
    #     try:
    #         conn = ENGINE.connect()
    #         conn.execute("commit")
    #         conn.execute("create database danmufm")
    #         conn.close()
    #     except sqlalchemy.exc.OperationalError as e:
    #         logger.error("无法创建数据库,请检查配置")
    #         logger.info("程序退出")
    #         exit()
    #     pass

    logger.info("开始配置环境")



def parse_command(url):
    """
指定获取主播的房间地址对主播直播情况进行抓取与统计 (Mac and Ubuntu Only)

Example:

    danmu.fm -q 2 -v 1 http://www.douyu.com/qiuri

    danmu.fm -q 3 -m 0 -p "videos/20160609_1900_2240_小苍.mp4" -v 1 http://www.douyu.com/qiuri

    """

    # danmu.fm -q 3 -m 0 -p "videos/20160609_1900_2240_小苍.mp4"-v 1 http://www.douyu.com/qiuri
    #config["video_quality"] = quality if quality > -1 or quality < 4 else 0
    #config["danmu_mode"] = mode if mode > -1 and mode < 2 else 0
    config["danmu_mode"]=1
    #current_working_dir = os.getcwd()
    #config["video_stored_path"] = os.path.join(current_working_dir,path) if path != "." else current_working_dir
    #config["thread_num"] = thread if thread >= 2 or mode <= 50 else 10
    config["thread_num"] =4
    #config["verbose"] = 
    config["authadd"]=0
    # [TODO:如果等于1就普通,如果为4直接开启全局日志]
    config["zhubo_room_url"] = url
    logger.info("正在检查环境")
    check_setting_and_env()
    logger.info("环境检查完毕,正在开启斗鱼客户端(请等待15s~30s)")
    start_douyu_client()


def start_douyu_client():
    url = config["zhubo_room_url"]
    DouyuClient(url,config).start()


def main(url):
    #print(APP_DESC)
    parse_command(url)
    #url="http://www.douyu.com/156277"
    #start_douyu_client()


if __name__ == "__main__":
    main()
