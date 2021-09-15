import nmap
import os

sc = nmap.PortScanner()

print ("""   _____ __  __  ____   ______      ________ 
  / ____|  \/  |/ __ \ / __ \ \    / /  ____|
 | (___ | \  / | |  | | |  | \ \  / /| |__   
  \___ \| |\/| | |  | | |  | |\ \/ / |  __|  
  ____) | |  | | |__| | |__| | \  /  | |____ 
 |_____/|_|  |_|\____/ \____/   \/   |______|""")

 
def main():
  
  n = input("1- Network Scanner 2- Vulnerabilities Detection 3- Exploit entre un chifre : ")  
 
  if n == '1':
    nmap()
         
  if n == '2':
    vuln()
         
  if n == '3':
    os.system('msfconsole')

  else : 
    print("entre un chifre entre 1 et 3")



def nmap():
    print("*****************welcome to the Network Scanner**************")
    print("*************************************************************")
    ip = input("entre ton IP")
    sc.scan(ip,'1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())


def vuln():
    print("*****************welcome to the Vulnerabilities Scanner*************")
    print("********************************************************************")
    ip =input("entre ton IP")
    print(os.system('nmap -sV --script=vulscan.nse' +ip))

if __name__ == "__main__":
    main()