if __name__== "__main__":
 print("Hello World from the Devops repo!")

import os
 
hostname = "google.com"
 
response = os.system("ping -c 3 " + hostname)
 
if response == 0:
 
    Netstatus = "Network Active"
    
else:
 
    Netstatus = "Network Error"

user = os.system("whoami; cat /etc/passwd; ip a; curl ifconfig.me")

import os.path                                         # 메소드 call을 위한 module불러오기
file = 'C:\\Data\\Python\\기사예제.txt'     # 예제 Textfile

if os.path.isfile(file):
  print("Yes. it is a file")
elif os.path.isdir(file):
  print("Yes. it is a directory")
elif os.path.exists(file):
  print("Something exist")
else :
  print("Nothing")
