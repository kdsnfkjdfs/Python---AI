# -*- coding: utf-8 -*-
"""20613이정현_문자열.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XrvK3ks5Ufd8GuPKGYlNriYeldY6XsUr
"""

s= "python"
print(s[0])
print(s[-1])

s= "python"
print(s[10])

s1 = input("첫번째 문자열 : ")
s2 = input("두번째 문자열 : ")
s3 = input("세번째 문자열 : ")

if s1[-1] == s2[0] and s2[-1] == s3[0]:
    print("Good")
else:
  print("BAD")

s = "python"

for i in range(0,len(s)):
  print(s[i],end = ",")

number = input('하이픈(-)을 포함한 휴대번호를 입력하시오: ')

for i in number:
  if i != '-':
    print(i,end="")

s= "python"
print(len(s))
n = "여섯글자이다"
print(len(n))

sentence = input("문자열 입력:")
for i in range(0,len(sentence)):
  if sentence[i] == 't':
    print(i+1,end = ' ')

from os import set_inheritable
sentence = input("문자열 입력해주세요 : ")
i =len(sentence)-1

while i>=0:
  print(sentence[i], end ='')

  i-=1

data = input("문자열 : ")

for i in range(0,len(data)-1):
  print(data[i],data[i+1],sep = '')

s = 'python'
print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])
print(s[-2:])

s = "차종은: 코란드C,제조사:쌍용, 배기량: 1998"
print(s[14:16])

file = "20210505_104830.jpg"
print("촬영날짜:"+file[4:6]+"월"+file[6:8]+"일")
print("촬영시간:"+file[9:11]+"시"+file[11:13]+"분")
print("확장자"+file[15:19])

yoil = "월화수목금토일"
print(yoil[0:7:2])
print(yoil[::-1])

jumin = "901231-1914983"
year = int(jumin[0:2])
print(year,end = '')
print("년생입니다")

a = "10 20 30 40 50"

b = "나는 서울로봇고 2학년이야."

print(a.split(' '))
b.split((' '))

a = "a:b:c:d"

BTS = "정국, 진, 뷔, 슈가, 지민, RM, 제이홉"
BTS_member = BTS.split(",")

print("방탄 멤버:",BTS_member)

for i in range(0,7):
  print(BTS_member[i],"사랑해")

file_names = ["file.py", "file2.txt", "file3.pptx","file4.doc"]

for i in range(0,4):
  arr = file_names[i].split(".")
  print(file_names[i],"=> 파일명:",arr[0],", 확장자.",arr[1])

sentence = input("문자열 입력: ")
a = sentence.split()

for i in a:
  print(i[0],end = "")



print(",".join('abcd'))
print("::".join(["1","2","3","4","5"]))

s = "python programming"

print("문자열 s의 길이 =",len(s))
print()
print("문자열 s에서 o의 인덱스 = ",s.find('o'))
print("문자열 없는 인덱스 = ",s.find('P'))
print("o를 두이세부터 검색한 인덱스 = ",s.rfind('o'))
print()
print("문자열 s에서 r의 인덱스 = ",s.find('r'))
print("문자열s에서n의 개수 = ",s.count('n'))
print()
print("문자열 s에서 gram의 인덱스 = ",s.find('gram'))
print("문자열 s에서 gram의 인덱스 = ",s.index('gram'))
print("문자열 s에서 gram의 개수 = ",s.count('gram'))

name = "박보검"
if name.startswith("박"):
  print("박씨입니다.")
elif name.startswith("김"):
  print("김씨입니다.")

file = "HelloPython.jpg"
if file.split('.')[1] == 'jpg':
  print("그림파일입니다")

domain = "http://www.soen.kr"
if domain.endswith('r'):
  print("한국 도메인입니다.")

s = "python programming"
print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

s = input("영어 문장을 입력하시오 :")
i = 0
count = 0

print('모음 :',end='')
while i<len(s):
  if 'a' in s[i]:
    print("a", end = ' ')
    count+=1
  if 'e' in s[i]:
    print("e", end = ' ')
    count+=1
  if 'i' in s[i]:
    print("i", end = ' ')
    count+=1
  if 'o' in s[i]:
    print("o", end = ' ')
    count+=1
  if 'u' in s[i]:
    print("u", end = ' ')
    count+=1


  i+=1
print()
print("모음의 개수 : %d" %count)

height = input("키를 입력하시오:")
if height.isalnum==0:
  print("키 = ",height)
else:
  print("숫자만 입력하시오")

data = input("문자열:")

for i in range(0,len(data)):
  if data[i].islower() == True:
    print('X',end ='')
  else:
    print("O",end ='')

f = open("노래가사.txt",'r')
data = f.read()

data = data.lower

print(f'다음 가사에서 "rollin"이 등자하는 횟수는 {data.count("rollin")}번 입니다.')