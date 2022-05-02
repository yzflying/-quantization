"""
上市公司财务指标分析(资产负债表)(利润表)(现金流量表)
公司财务指标纵向比较，与同行业平均水平比较；表中各子项的占比纵向变化
1.盈利能力:净利润 1亿;毛利率 20%;净资产收益率 20%
["profit_dedt":"扣非净利润", "extra_item":"非经常性损益","grossprofit_margin":"销售毛利率","roe":"净资产收益率"]
2.偿债能力：流动比率 >2;速动比率 >1;资产负债率 0.5-0.6;固定资产比率
["current_ratio":"流动比率","quick_ratio":"速动比率","debt_to_assets":"资产负债率"]
3.现金流量：经营活动现金流为正;主营业务现金流入/营业收入(销售收现率);主营业务现金流入/现金流入(主营业务占比)
["ocf_yoy":"经营活动产生的现金流量净额同比增长率(%)"]
4.运营能力：存货周转率;应收账款周转率;总资产周转率
["ar_turn":"应收账款周转率","assets_turn":"总资产周转率"]
5.增长能力：主营业务收入增长率;净利润增长率
["ebt_yoy":"利润总额同比增长率(%)","or_yoy":"营业收入同比增长率(%)","tr_yoy":"营业总收入同比增长率(%)"]
6.市场价值：每股收益;市盈率（股价/每股收益）;市净率(股价/每股净资产)
["eps":"基本每股收益", "bps":"每股净资产"]
"""

from config import *

fina_cols = ["ts_code", "ann_date", "end_date", "profit_dedt", "extra_item",
                "grossprofit_margin", "roe", "current_ratio", "quick_ratio", "debt_to_assets",
                "ocf_yoy", "ar_turn", "assets_turn", "ebt_yoy", "or_yoy", "tr_yoy", "eps", "bps"]



# 获取财务数据
df = pro.fina_indicator(ts_code='300059.SZ', start_date='20180101', end_date='20200101')
# df = df[fina_cols]
print(df)




