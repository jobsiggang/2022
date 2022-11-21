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
max_temp=[]
min_temp=[]
year=[]
#3. 조건에 맞는 데이터만  순서대로 저장하기   
for row in data :
  if row[-1] !='' :
     max_temp.append(float(row[-1]))
     year.append(row[0].split('-')[0])
#4.저장된 데이터를 다양한 그래프로 그리기
plt.rc('font',family='NanumGothic')

plt.title('기온 변화')
# plt.plot(year,max_temp)#5.결과그래프 보여주기
plt.plot(year,max_temp,color='red')
plt.xticks(rotation=45)
plt.show()