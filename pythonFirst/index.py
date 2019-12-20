import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets, linear_model


def get_data(url): # парсинг страницы с данными
  page = pd.read_html(url, encoding='CP1251')
  header = page[6].drop(12).T
  header = header.iloc[1]
  header[0]='Номер УИК'
  data=page[7].drop(12).T
  data.columns=header
  data.reset_index()
  return data


def to_numeric(data): #функция парсит все данные в числа, убирает символы
  data.iloc[:,0]=[int(i.split()[1][1:]) for i in data.iloc[:,0]]
  for i in range(1,12):
    data.iloc[:,i]=pd.to_numeric(data.iloc[:,i])
  for i in range(12,15):
    l=[]
    perc=[]
    for a in data.iloc[:,i]:
      a=a.split()
      l.append(int(a[0]))
      perc.append(float(a[1][:-2]))
    data.iloc[:,i]=l
    data['Процентов за ' + str(data.columns.values[i])] = perc
  return data

# Урлы 11 и 17 тика Калиниского района
url11 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217435&type=222'
url27 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217429&type=222'


data = get_data(url11)
data1 =get_data(url27)
data = to_numeric(data)
data1 = to_numeric(data1)
data = data.append(data1)
data.head()

def plot(x,y,label):
  x=np.array(x).reshape(-1,1)
  y=np.array(y).reshape(-1,1)
  l=LinearRegression().fit(x,y)
  c=l.coef_[0][0]
  xmin=min(data.iloc[:,1])
  xmax=max(data.iloc[:,1])
  ls=np.linspace(xmin,xmax)
  plt.plot(ls,ls*c,color='red')
  plt.scatter(x,y,linewidth=1)
  plt.legend(['МНК','Голоса за '+label])
  print('MSE =',mean_squared_error(y,x*c))
  print('R2 score = ',r2_score(y,x*c))
  plt.show()
  print()

plot(data.iloc[:,1],data.iloc[:,12], 'Амосова')
plot(data.iloc[:,1],data.iloc[:,13],'Беглова')
plot(data.iloc[:,1],data.iloc[:,14],'Тихонова')