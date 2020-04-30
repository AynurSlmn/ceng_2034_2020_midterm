#!/usr/bin/python3
import os,sys,threading,requests
#1
print("PID is",os.getpid())
#2
if(sys.platform == "linux"):
         print("load average is ",os.getloadavg())
#4
arr=["https://api.github.com","http://bilgisayar.mu.edu.tr/","https://www.python.org/","http://akrepnalan.com/ceng2034","https://github.com/caesarsalad/wow"]
def request(url):
          res=requests.get(url)
          res_code =res.status_code

          if(200<=res_code<=300):
                   print(url +" URL is valid")
          else:
                   print(url +" URL is invalid")
for i in range(0,5):
        thread1 =threading.Thread(target=request,args=(arr[i],))
        thread1.start()
#3
load_avg=os.getloadavg()
print("Cpu count is ",os.cpu_count())
load_avg_5min =load_avg[1]
print("load_avg_5min is ",load_avg[1])
if(os.cpu_count()-load_avg[1]<1):
         
            sys.exit()
