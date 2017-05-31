#coding:utf-8
"""
这里是实盘的时候可能用到的一些函数

- 历史数据和实盘数据的合并
- 账户信息的监控
- 风险监控
- 消息的传递
"""

import zmq
import requests
import json,sys,os,datetime,time
import pymongo
import tushare as ts
from QA_trade_stock import QA_Stock
import QUANTAXIS as QA


def QA_get_hist_data(code,date):
    return QA.QA_fetch_get_stock_day('ts',code,date[0],date[1])
def QA_get_realtime_data():
    return QA.QA_fetch_get_stock_realtime('ts')
def QA_get_now_data(client,st,code):

    data=st.QA_trade_stock_get_quote(client,code)
    print(data.split('\n')[1].split('\t')[5])
def QA_combind_data(code,gap):
    data1=QA_get_hist_data('603999',[str(datetime.date.today()-datetime.timedelta(days=20)),str(datetime.date.today())])
    data2=QA_get_realtime_data()
    for item in data2:
        if item['code']=='603999':
            print(item)
def QA_get_account_assest():
    pass
def QA_risk_analysis():
    pass


if __name__=='__main__':
    st=QA_Stock()
    st.get_config()
    client = st.QA_trade_stock_login()
    QA_get_hist_data('603999',[str(datetime.date.today()-datetime.timedelta(days=20)),str(datetime.date.today())])
    data=QA_get_realtime_data()



    
    #print(ts.get_today_all())