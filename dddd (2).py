#!/usr/bin/env python
import time
import datetime

name=['abc','bca','cbd','dcb','adc','bca','cda','dcb','bda']
locat=['New_York','Detroit','Louisville','Monticello','Indianapolis','Vincennes','Winamac','Indiana/Marengo','Petersburg','Vevay','Knox','Menominee','North_Dakota/Center','New_Salem','Los_Angeles','Anchorage','Juneau','Sitka','Yakutat']
status=['Intransmit','cancelled','Exception','Delivered']
statu=['Yes','No']
cargo="Container"
amount=[2334,2323,1412,1313,1334,5124,5234,5352,2524,2576,7683,3435,1341,3513,5124,4522,4245,3415]
import random
import sys

dt = datetime.datetime(2015, 05, 24)
end = datetime.datetime.today( ) + datetime.timedelta(days=1)
step = datetime.timedelta(minutes=1)

result = []

while dt < end:
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += step
    print "%s\t%s\t%s\t%d\t%d\t%s\t%s\t%s\t%s\t%s"%(dt,random.choice(name),cargo,random.choice(amount),random.choice(amount),random.choice(status),random.choice(locat),random.choice(locat),random.choice(statu),random.choice(statu))


