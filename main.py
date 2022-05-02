# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8

"""
股池：白马股、成长股，一般不超过300个
趋势：上升趋势的自动判断(3日均线的极值)
买卖点：K线突破回调，量增(量价抵扣，均线)，乖离率统计值，量、macd背离
仓位：凯利公式
基本面：财务指标
相关性：同一主题、行业股票之间的联动性
"""


code = []
for line in open("sw3.txt", encoding="gbk"):
    print(line.split()[2])
    code.append(line.split()[2])
print(len(list(set(code))))
#     sw3_vals.append(line.split("</a>")[0])
#
# print(sw3_vals)


