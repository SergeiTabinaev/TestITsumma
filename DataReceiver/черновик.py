import  psutil
from decouple import config


# CPU
# тут будет блокировка потока
psutil.cpu_percent(interval=config('INTERVAL'))
# 2.0
# блокировки нет, цифра с момента последнего вызова
# psutil.cpu_percent(interval=None)
# 2.9


#memory
mem = psutil.virtual_memory()
#(total=8374149120L, available=1247768576L, percent=85.1, used=8246628352L, free=127520768L, active=3208777728, inactive=1133408256, buffers=342413312L, cached=777834496)
# total - общее количество физической памяти
# available - доступная память для процессов
# percent - процент использования памяти, (total - available) / total * 100.
# used - используемая память
# free - свободная память
# active - (UNIX), используемая память
# inactive - (UNIX), неиспользуемая память
# buffers - (Linux, BSD), кеш, метаданные файловой системы
# cached - (Linux, BSD): кеш для различных вещей
# wired - (BSD, OSX): память, не перемещаемая на диск
# shared - (BSD): память доступная одновременно для нескольких процессов

#disks
psutil.disk_partitions()
# [sdiskpart(device='/dev/sda3', mountpoint='/', fstype='ext4', opts='rw,errors=remount-ro'),
#  sdiskpart(device='/dev/sda7', mountpoint='/home', fstype='ext4', opts='rw')]
# Возвращает список именованных кортежей, информация по смонтированным разделам диска - устройство, точку монтирования, тип.
# psutil.disk_usage('/')
# sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
# Возвращает именованный кортеж, информация по использованию диска


#network
psutil.net_io_counters()
# snetio(bytes_sent=14508483, bytes_recv=62749361, packets_sent=84311, packets_recv=94888, errin=0, errout=0, dropin=0, dropout=0)
#bytes_sent - количество отправленных байтов
# bytes_recv - количество принятых байтов
# packets_sent - количество отправленных байтов
# packets_recv - количество принятых байтов
# errin - количество ошибок при приемке
# errout - количество ошибок при отправке
# dropin - количество пришедших пакетов, которые были отброшены
# dropout - количество отправленных пакетов, которые были отброшены(0 на OSX и BSD)














