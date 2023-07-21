if __name__== "__main__":
 print("Hello World from the Devops repo!")

import os
 
hostname = "google.com"
 
response = os.system("ping -c 3 " + hostname)
 
if response == 0:
 
    Netstatus = "Network Active"
    
else:
 
    Netstatus = "Network Error"
