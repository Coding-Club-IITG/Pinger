import csv

header = ['IP', 'Status']
with open('./ips.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(51, 97):
        writer.writerow([f'172.16.101.{i}', '-'])
f.close()
