#!/usr/bin/python
# coding: UTF-8

import csv
import os,sys
import yaml
import pandas as pd
from functools import reduce

path = 'C:/work/connpass-userstat/fulldata/'

EventNo_Name = yaml.load(open(path + "EventNo_Name.yaml"))
#UserDetail = yaml.load(open(path + "UserDetail.yaml"))

Events = []
results = pd.DataFrame()

for EventNo in EventNo_Name.keys():
    ReadFile = open(path + 'event_' + str(EventNo) + '_participants.csv', 'r')
    print(EventNo)
    dataset1 = pd.read_csv(ReadFile)
    dataset = dataset1.drop("参加枠名",axis=1).drop("受付番号",axis=1).drop("コメント",axis=1).drop("更新日時",axis=1).drop("出欠ステータス",axis=1)
    dataset.rename(columns = {'参加ステータス':'%s' % EventNo_Name[EventNo]},inplace = True)
    Events.append(dataset)
    ReadFile.close()

results = reduce(lambda left,right: pd.merge(left,right,on = ['ユーザー名','表示名'],how='outer'), Events)

print(results)

results.to_csv("events.csv")