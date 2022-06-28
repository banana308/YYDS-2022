# -*- coding:utf-8 -*-
"""
@author:shanhai
@function: 基础路径获取
"""
import os
# 项目的路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 日志地址
log_dir = os.path.join(base_dir,'log')
#  基础配置文件地址
base_conf_dir =os.path.join(base_dir,'bfty_config','base_conf.ini')
#用例excel 地址
owner_backer_path  = os.path.join(base_dir,'YgLibrary','d0_comparison_report.xlsx')
# token_yaml_path = os.path.join(base_dir,'test_data','token.yaml')
# ball_report_name = os.path.join(base_dir,'test_data','report','ball_report','ball_name.yaml')
# ball_market_name = os.path.join(base_dir,'test_data','report','ball_report','ball_market_name.yaml')

if __name__ =='__main__':
    print(owner_backer_path)
