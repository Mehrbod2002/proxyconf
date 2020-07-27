import os,requests,sys,time,json,urllib
os.system("clear")
def inputs():
  pathp=input(t()+bcolors.FAIL+(" Install ProxyChains Failed ... Enter Conf File :"))
def banner():
 print("""\033[93m ____                        ____             __ 
|  _ \ _ __ _____  ___   _  / ___|___  _ __  / _|
| |_) | '__/ _ \ \/ / | | || |   / _ \| '_ \| |_ 
|  __/| | | (_) >  <| |_| || |__| (_) | | | |  _|
|_|   |_|  \___/_/\_\\__, (_)____\___/|_| |_|_|  
                     |___/     
        v1.0.0-mehrbod2002/proxy.conf
                mehrbod.expo
""")
def t():
    current_time = time.localtime()
    ctime = time.strftime('%H:%M:%S', current_time)
    return '\033[94m[' + ctime + ']'
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'
def check_root():
 if os.getuid()!=0:
  sys.exit(t()+bcolors.FAIL+" Run As ROOT\n")
 else:
  print(t()+bcolors.GREEN+" Start Configuring...")
def reinstallit():
  s=os.system("apt-get reinstall proxychains")
def check_website():
  print(t()+bcolors.GREEN+" Check Last Proxy ... ")
  try:
   filep=urllib.request.urlretrieve("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all","p.txt") # you change proxy list website here
  except urllib.error.URLError:
   sys.exit(t()+bcolors.FAIL+"Network Problem  Retry ...")
  print(t()+bcolors.GREEN+" Done . Parsing ... ")
def count():
 with open('p.txt') as f:
    line_count = 0
    for line in f:
        line_count += 1
 return line_count
def otro():
  if os.path.isfile("/etc/proxychains.conf")==False:
   print(t()+bcolors.GREEN+" Check proxyChains installed or no ...\n")
   os.system("apt-get install proxychains")
  if os.path.isfile("/etc/proxychains.conf")==True:
   pathp="/etc/proxychains.conf"
  else:
   findproxyconf.pathp=input(t()+bcolors.FAIL+(" Install ProxyChains Failed ... Enter Conf File :"))
  if os.path.exists(pathp)==False:
   sys.exit(t()+bcolors.FAIL+"No Such File . Retry ...")
  else:
   print(t()+bcolors.GREEN+" Start Configuring...")
  fo=open("p.txt","r")
  li1=fo.readline()
  pr2=li1.split(":")
  pr3="socks4 "+pr2[0]+" "+pr2[1]
  fo1=open(pathp)
  fp2=fo1.read()
  if(pr3==fp2):
   sys.exit("Already Configure ... Try Later")
def parse():
  if os.path.isfile("/etc/proxychains.conf")==False:
   print(t()+bcolors.GREEN+" Check proxyChains installed or no ...\n")
   os.system("apt-get install proxychains")
  if os.path.isfile("/etc/proxychains.conf")==True:
   pathp="/etc/proxychains.conf"
  else:
   findproxyconf.pathp=input(t()+bcolors.FAIL+(" Install ProxyChains Failed ... Enter Conf File :"))
  if os.path.exists(pathp)==False:
   sys.exit(t()+bcolors.FAIL+"No Such File . Retry ...")
  else:
   print(t()+bcolors.GREEN+" Start Configuring...")
  f=open("p.txt","r")
  lines=f.readlines()
  i=1
  s=count()
  while i<s:
   pro=lines[i]
   prox=pro.split(":")
   prox1="socks4 "+prox[0]+" "+prox[1]
   f=open(pathp,"a")
   f.write(prox1)
   i+=1
  f.close()
  print(t()+bcolors.GREEN+" Done . Enjoy it")
def main():
 banner()
 check_root()
 reinstallit()
 check_website()
 otro()
 parse()
if __name__ == "__main__":
  main()
