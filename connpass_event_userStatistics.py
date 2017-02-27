#!/usr/bin/python
# coding: UTF-8

import csv
import os,sys
import pandas as pd

#C:\work\rancherjp.connpass\fulldata\utf8
path = 'C:/work/rancherjp.connpass/fulldata/utf8/'

# CSV
# 0       ,1         ,2     ,3       ,4             ,5             ,6       ,7
# 参加枠名,ユーザー名,表示名,コメント,参加ステータス,出欠ステータス,更新日時,受付番号
#                                     参加
#                                     参加キャンセル
#                                     補欠
#          (退会ユーザー)

FileList = os.listdir(path)

#EventUsers = collections.defaultdict(int)
EventUsers = {}

# EventUsers
#     userid = > 
#                DisplayName : 
#                EventNo => status : {1 = "参加",2 = "参加キャンセル",3 = "補欠"}
#                           update : datetime
#                           


for FileName in FileList:
    ReadFile = open(FileName, 'r')
    EventNo = FileName.split('_')[1]
    print(EventNo)
#    EventUsers[EventNo] = {}
    reader = csv.reader(ReadFile)
    for row in reader:
        # print(row)
        UserID = row[1]
        print(UserID)

        DisplayName = row[2]
        print(DisplayName)
#        EventUsers[UserID][EventNo]["update"] = row[6]
    
    ReadFile.close()
