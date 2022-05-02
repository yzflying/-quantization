from config import *

"""
获取最近n年的上市公司财务报表，按照公司申万各级分类，统计各级行业的各财务数据的均值
计算时应该包含当期所有上市公司(现退市),ST公司
同一个股票可能属于多个三级分类下
"""
# 上市公司上市时间、退市时间、上市状态
# data = pro.stock_basic(exchange='', list_status='D', fields='ts_code,symbol,name,industry,list_status,list_date,delist_date')
# data = data.sort_values(by=['delist_date'])
# print(data)
# data = data[data["delist_date"]>"20100101"]
# print(data)


# 上市公司所属申万分类
sw3_stocks = []
for line in open("sw3.txt", encoding="gbk"):
    sw3_stocks.append([line.split()[1], "".join(list(filter(str.isdigit, line.split()[2]))), "".join(line.split()[3:])])
df_class = pd.DataFrame(data=sw3_stocks, columns=["sw3_class", "code", "name"])
print(df_class)


code_s = []
for i in set(df_class["code"].tolist()):
    if i[:2] in ['60', '68']:
        code_s.append(i+".SH")
    elif i[:2] in ['00', '30']:
        code_s.append(i + ".SZ")
    else:  # '83', '87', '43'
        code_s.append(i + ".BJ")


# 上市公司财务数据
df_fina = pd.read_csv("fina.csv", encoding="gbk")
print(df_fina.head(30))

# fina_cols = ["ts_code", "ann_date", "end_date", "profit_dedt", "extra_item",
#                 "grossprofit_margin", "roe", "current_ratio", "quick_ratio", "debt_to_assets",
#                 "ocf_yoy", "ar_turn", "assets_turn", "ebt_yoy", "or_yoy", "tr_yoy", "eps", "bps"]
# df_fina = pd.DataFrame(columns=fina_cols)
#
# cnt = 0
# for code in code_s:
#     df = pro.fina_indicator(ts_code=code, start_date='20190101', end_date='20220501')
#     df = df[fina_cols]
#     df_fina = pd.concat([df_fina, df])
#     time.sleep(1)
#
#     cnt += 1
#     print(cnt)
#
# df_fina.to_csv("fina.csv", encoding="gbk")