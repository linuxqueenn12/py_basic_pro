print('---------------------------------------------')
print('---------------------------------------------')
print('#### PYTHON basic ####')
print('[1]created by @linuxqueenn')
print('---------------------------------------------')
print('---------------------------------------------')
#القوائم
menu=['blackaht','whitehat','grayhat']

#طباعةعنصر محدد
menu[0]

#متغير
types="menuu"

#اضافة عنصر الى القائمة
menu.append('bluteam')
menu+=(['redteam'])
print(menu)

#اضافة عنصر 
menu.extend(['zero'])


#معرفة عدد عناصر في النص تحسب الحروف والقوائم تحسب الكلمات
len(types)
len(menu)

#يطبع من رقم الى رقم بالقائمة 
menu[0:3]
menu.reverse()
print(menu)

#يطبع من رقم الى رقم من القائمة 
menu[0:3]
menu.reverse()
print(menu)

#يطبع بالعكس 
menu[::-1]
types=[0-1]

type="\nchose\n"
type0="ur type"

type1= type + type0
print(type1)

#تبديل مكان كلمة 
url="youtube.com"
urll=url.replace("youtube.com" ,"facebook.com")
print(urll)

#التاكد من عنصر اذا كان موجود
'python' in menu

#تحويل متغير الى قائمة
list= url.split()

#تكبير اول حرف
url.capitalize()
url.lower()

#تكبير كل الحروف 
url2= url.upper()
print(url2)

#المجموعات
tuples=(1,2,3,4,'a')

#القواميس
users={'name':'salim','age':19}
print(users['name'])
print(users['age'])

#امر ادخال
names={'salim':100 ,'ahmed':89}
user=input('enter ur name\n')

#الجمل الشرطية
if user == 'salim':
  print(names['salim'])

elif names== 'la': 
 print('sorry')

#حساب القاموس 
len(names)

#تحديث القاموس
names.update({'sara': 92 , 'ayah':33})
print(names)

#حذف عنصر من القاموس
names.pop('ayah')
print(names)

#من النهاية
names.popitem()
print(names)

#حذف كل القاموس 
names.clear()
print(names)
del names
'cyber' in users 

#تحويل القاموس الى نص 
user=repr(users)
print(user)

user1=user.replace('name','unknown')
print(user1)


#فتح ملفات للكتابة فقطw
openn=open('kf.txt','w+')
openn.write('hello')

opern=open('kf.txt','r')
opern.read()
opern.close()

f11=open('kf.txt' , 'w')
f11.write('welcome\n to\n cyber\n world') 
f11.close()
#اضافة عناصر  append
#f1=open('kf.txt' , 'a')
#f1.write('welcome\n to\n cyber\n world')
#f1.close()
#قراءة وكتابة نفس الوقت 
f=open('kf.txt','w+')
f.read()
f.close()

print(openn.readline())
tt= print(openn.read(2))
print(tt)

with open('kf,txt', mode='w') as f:
 f.write('cyber world')
#جملة if الشرطية 
email='cyberg@gmail.com'
password='1234'
 
if email== 'cyberg@gmail.com' and password == '1234':
 print ('welcome')
 
elif email=='cyber@icloud.com':
  print('welcome back')

else :
 print('sorry')
  
name='ahmed'
password='12345'
if name == 'ahmed' or name == 'salim':
 print ('your password easy')

#الحلقات التكرارية loop
#aa=11
#while aa == 11 :
#print ('i love U')
#استمرار المحادثة 
#while True :
#data=input('enter your message')
#data2=input('enter your message')
 #استخدام قاعدة for
data=['cyber','security','offensive']
for new in data :
 print(new)
 
 #تحقق المستخدم من وجود 
name =input('enter your field\n')
dataa=['cyber','security','offensive']
for neww in dataa:
 if neww == name:
  print('found')
  
#تعريف الدوال input
def myinput():
 data3 = input('enter')
myinput()
 
