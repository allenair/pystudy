#-*- coding: utf-8 -*-

import psutil

print(psutil.cpu_percent(interval=1,percpu=False))
print(psutil.cpu_percent(interval=1,percpu=True))
