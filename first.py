import psutil

cpuCores = psutil.cpu_count()
cpuCores2 = cpuCores
maxClears = cpuCores/2
print(maxClears)

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
 
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
 
    listOfProcessObjects = []
 
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
 
    return listOfProcessObjects;

def setAffinity(processID):
    proc = psutil.Process(processID)
    proc.cpu_affinity(listik)

# Find PIDs od all the running instances of process by name
listOfProcessIds = findProcessIdByName('nostaleclientx')
 
if len(listOfProcessIds) > 0:
   print('Process Exists | PID and other details are')
   for elem in listOfProcessIds:
       processID = elem['pid']
       processName = elem['name']
       if cpuCores2 == 2:
           cpuCores2 = cpuCores
       listik = [cpuCores2-1, cpuCores2-2]
       print(processID ,processName, cpuCores2-1, cpuCores2-2)
       cpuCores2 -= 2
       setAffinity(processID)
else :
   print('No Running Process found with given text')


