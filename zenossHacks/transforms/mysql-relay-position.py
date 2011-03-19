import datetime

def get_maintenance_window(start_values, stop_values):
    results = {}
    delta = datetime.timedelta(days=1)

    now = datetime.datetime.now()
    start_time = datetime.time(start_values[0], start_values[1]) 
    stop_time = datetime.time(stop_values[0], stop_values[1]) 

    if start_time > stop_time:
        results['start'] = datetime.datetime.combine(now.date(), start_time) - delta
    else:
        results['start'] = datetime.datetime.combine(now.date(), start_time)
        
    results['stop'] = datetime.datetime.combine(now.date(), stop_time)

    return results
       
# Maintenance Variables (Hour, Min) astronomical time

START_TIME = (0, 45)
STOP_TIME = (1, 5)

now = datetime.datetime.now()
maintenance = get_maintenance_window(START_TIME, STOP_TIME)
###

repDelay = device.getRRDValue('check_mysql_slave_time')
if repDelay > 0:
    evt._action = "drop"

if now >= maintenance['start'] and now <= maintenance['stop']:
    evt.severity = 3
