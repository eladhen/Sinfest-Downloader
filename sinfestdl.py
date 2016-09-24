import requests
from datetime import date, timedelta as td
print('This program will download all of the Sinfest comic strips between two given dates')
print('Enter the year of the starting date: yyyy')
yearD1 = int(input())
print('Enter the month of the starting date: mm')
monthD1 = int(input())
print('Enter the day of the starting date: dd')
dayD1 = int(input())
d1 = date(yearD1, monthD1, dayD1)

print('Enter the year of the ending date: yyyy')
yearD2 = int(input())
print('Enter the month of the ending date: mm')
monthD2 = int(input())
print('Enter the day of the ending date: dd')
dayD2 = int(input())
d2 = date(yearD2, monthD2, dayD2)

print('Downloading')

dateList = []
delta = d2 - d1
for i in range(delta.days + 1):
     dateList.append(str(d1 + td(days=i)))
    # print(d1 + td(days=i))

for j in dateList:
    res = requests.get('http://www.sinfest.net/btphp/comics/' + j + '.gif')
    res.raise_for_status()
    playFile = open(j + '.gif', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()

print('All done. Enjoy the comics')
