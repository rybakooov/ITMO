import pandas as pd
import numpy as np
import requests
from pandas import DataFrame

dataFr = pd.read_csv('temp.csv', delimiter=',')

dataFr['Округ'] = 0



for i in range(len(dataFr["Адрес УИК"])):
  if ('Адрес' in dataFr["Адрес УИК"][i]):
    dataFr["Адрес УИК"][i] = dataFr["Адрес УИК"][i][129:]
    indexZap = dataFr["Адрес УИК"][i].index(',')
    dataFr['Округ'][i] =  dataFr["Адрес УИК"][i][:indexZap]


dataFr.drop(["Номер УИК", "index"], axis='columns', inplace=True)
dataFr.drop(["Число недействительных избирательных бюллетеней", "Число действительных избирательных бюллетеней", "Число избирательных бюллетеней, содержащихся в переносных ящиках для голосования", "Число избирательных бюллетеней, содержащихся в стационарных ящиках для голосования", "Число погашенных избирательных бюллетеней", "Число избирательных бюллетеней, выданных избирателям, проголосовавшим вне помещения для голосования", "Число избирательных бюллетеней, выданных избирателям в помещении для голосования в день голосования", "Число избирательных бюллетеней, полученных участковой избирательной комиссией", "Число избирателей, внесенных в список избирателей на момент окончания голосования", "Число утраченных избирательных бюллетеней", "Число избирательных бюллетеней, не учтенных при получении", "Процентов за Амосов Михаил Иванович", "Процентов за Беглов Александр Дмитриевич", "Процентов за Тихонова Надежда Геннадьевна", "Адрес УИК"], axis='columns', inplace=True)


#for item in range(6):
dopIdx = 0
for row in dataFr['Округ']:
  if (dopIdx + 1) == len(dataFr['Округ']): 
    break
  if row == dataFr['Округ'][dopIdx + 1]:
    dopdopIdx = dopIdx + 1
    while row == dataFr['Округ'][dopdopIdx]:
      if dopdopIdx == (len(dataFr['Округ']) - 1): 
        break
      for stolb in dataFr:
        if stolb != 'Округ':
          dataFr[stolb][dopIdx] = int(dataFr[stolb][dopIdx]) + int(dataFr[stolb][dopdopIdx])
          dataFr[stolb][dopdopIdx] = 0
      dopdopIdx += 1
    dopIdx += 1
    #print(dopdopIdx)

#print(dataFr)
#indexxxx = 0
#for row in dataFr[2]:
#  if row == 0
#    dataFr.drop([indexxxx], inplace=True)
#  indexxxx += 1

dataFr.to_csv(r'C:\Users\rybak\Desktop\OSPanel\domains\pyVOTE\temp_map111.csv', index=False)
