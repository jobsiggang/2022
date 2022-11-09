3#1. 필요한 라이브러리 불러오기
 #1) 데이타를 차트나 플롯(Plot)으로 그려주는 라이브러리 불러오기
import matplotlib.pyplot as plt
 #2) csv 파일을 쉽게 다루도록 도와주는 라이브러리 불러오기
import csv
#2. 기온데이터 불러오기
 #1) csv 파일열기
f=open('ulsan_temp.csv')
 #2) 데이터를 컴마로 구분하여 저장하기
data=csv.reader(f)
next(data)
 #3) for 반복문으로 한줄씩 꺼내기
max_temp2018=[]
month2018=[]
max_temp2019=[]
month2019=[]
#3. 조건에 맞는 데이터만  순서대로 저장하기   
for row in data :
  if row[-1] !='' and row[0].split('-')[0]=='2019'and row[0].split('-')[2]=='01':
     max_temp2019.append(float(row[-1]))
     month2019.append(row[0].split('-')[1])
  elif row[-1] !='' and row[0].split('-')[0]=='2018'and row[0].split('-')[2]=='01':
     max_temp2018.append(float(row[-1]))
     month2018.append(row[0].split('-')[1])
#4.저장된 데이터를 다양한 그래프로 그리기
plt.rc('font',family='NanumGothic')
plt.figure(dpi=300)
plt.style.use('ggplot')
plt.subplot(2,2,1)
plt.title('2019최고기온 변화')
plt.plot(month2019,max_temp2019,label='max',color='red')
plt.subplot(2,2,2)
plt.plot(month2018,max_temp2018, label='max', color='blue')
plt.title('2018최고기온 변화')
#5.결과그래프 보여주기
plt.show()