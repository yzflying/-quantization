import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts   # 获取行情数据
ts.set_token('7c147a1be123c77a94becb77e4943329d945c8008db2a345c8e69163')  # tushare账号token认证
import talib as ta     # 计算技术指标值
import time

pro = ts.pro_api()
pd.set_option('display.max_columns', None)   # 显示所有的列
pd.set_option('display.max_rows', None)      # 显示所有的行
pd.set_option('display.width', 1000)         # 不换行显示