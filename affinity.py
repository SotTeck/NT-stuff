import psutil

cpuCores = psutil.cpu_count()
cpuCores2 = cpuCores
maxClears = cpuCores/2
print(maxClears)

def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
 
    return listOfProcessObjects;

def setAffinity(processID):
    proc = psutil.Process(processID)
    proc.cpu_affinity(listik)

listOfProcessIds = findProcessIdByName('nostaleclientx')
 
if len(listOfProcessIds) > 0:
   print('Process Exists | PID and other details are')
   for elem in listOfProcessIds:
       processID = elem['pid']
       processName = elem['name']
       if cpuCores2 == 0:
           cpuCores2 = cpuCores
       listik = [cpuCores2-1, cpuCores2-2]
       print(processID ,processName, cpuCores2-1, cpuCores2-2)
       cpuCores2 -= 2
       setAffinity(processID)
else :
   print('No Running Process found with given text')
