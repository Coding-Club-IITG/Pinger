# from ping3 import ping as PING
import platform
import subprocess
import pandas as pd
import os

df = pd.read_csv('C:/Users/CC/Desktop/Projects/pinger/ips.csv', index_col=0) #Absolute path for task scheduler

# df.at[91-51, 'Status']='Occupied'
# df.to_csv('ips.csv')

def ping(host):
    # res = PING(host)
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    res = subprocess.run(command, stdout=subprocess.PIPE)
    output = str(res.stdout).split('\\r\\n')
    if len(output[2]) > 18:
        newOutput = output[2].split(': ')
        if newOutput[1] == 'Destination host unreachable.':
            return False
        elif newOutput[1].split(' ')[0] == 'bytes=32':
            return True
    else:
        newOutput = output[2]
        if newOutput == 'Request timed out.':
            return True
    # if newOutput[1] == 'Destination host unreachable.':
    #     return False
    # elif newOutput:
    #     return True

# print(ping('172.16.101.88'))

for i in range(51, 97):
    res = ping(f'172.16.101.{i}')
    color = '\033[91m'
    emoji = '❌'
    if res == True:
        df.at[i-51, 'Status'] = 'Occupied'
        color = '\033[92m'
        emoji = '✔️ '
    
    print(f'{color}{emoji} IP 172.16.101.{i} occupied: ' + str(ping(f'172.16.101.{i}')))

df.to_csv('C:/Users/CC/Desktop/Projects/pinger/ips.csv')
print('\033[92m✔️ Done')

# IP Range
# 172.16.101.xx
# 51 - 96