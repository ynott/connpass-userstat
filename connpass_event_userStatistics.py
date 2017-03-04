#!/usr/bin/python
# coding: UTF-8

import csv
import os,sys
import pandas as pd
from functools import reduce

#C:\work\work\connpass-userstat\fulldata\utf8
path = 'C:/work/connpass-userstat/fulldata/utf8/meetup'

EventNo_Name = { 
  "41997": "もくもく勉強会 #1",
  "44092": "Meetup Tokyo #2",
  "46208": "Meetup Tokyo #2懇親会",
  "45768": "Meetup Tokyo #3",
  "47871": "もくもく勉強会 #2",
  "47273": "Meetup Tokyo #4",
  "50977": "Meetup Tokyo #4懇親会",
  "49891": "もくもく勉強会 #3",
  "50984": "もくもく勉強会 #3懇親会",
  "49614": "Meetup Tokyo #5",
  "51641": "Meetup Tokyo #5懇親会"
}

FileList = os.listdir(path)
Events = []
results = pd.DataFrame()


for FileName in FileList:
    ReadFile = open(FileName, 'r')
    EventNo = FileName.split('_')[1]
    print(EventNo)
    dataset1 = pd.read_csv(ReadFile)
    dataset = dataset1.drop("参加枠名",axis=1).drop("受付番号",axis=1).drop("コメント",axis=1).drop("更新日時",axis=1).drop("出欠ステータス",axis=1)
    dataset.rename(columns = {'参加ステータス':'%s' % EventNo_Name[EventNo]},inplace = True)
#    dataset.rename(columns = {'出欠ステータス':'%s' % EventNo_Name[EventNo]},inplace = True)
    Events.append(dataset)
    ReadFile.close()


results = reduce(lambda left,right: pd.merge(left,right,on = ['ユーザー名','表示名'],how='outer'), Events)

print(results)

results.to_csv("events.csv")