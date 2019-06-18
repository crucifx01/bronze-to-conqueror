import psutil

print( "battery_info" )
print(psutil.sensors_battery())


#print(percent+'% | '+plugged)

print( "cpu_info" )
print(psutil.cpu_times())

print( "memory_usage" )
print(psutil.virtual_memory())

print( "swap_memory" )
print(psutil.swap_memory())

print ( "disk_partitions" )
print(psutil.disk_partitions())

print( "disk_usage" )
print(psutil.disk_usage('/'))
