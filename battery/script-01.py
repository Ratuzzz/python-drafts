#!/usr/bin/python

import os
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

ALERT_TRESHOLDS = 0.80
SHUTDOWN_TRESHOLD = 0.10

def get_data_from_file(filePath):
    f = open(filePath, 'r')
    res = f.read()
    f.close()
    return res

energy_now = get_data_from_file('/sys/class/power_supply/BAT0/energy_now')
energy_full = get_data_from_file('/sys/class/power_supply/BAT0/energy_full')
energy_percent = int(energy_now) / int(energy_full)
battery_state = get_data_from_file('/sys/class/power_supply/BAT0/status').rstrip()

if (energy_percent < SHUTDOWN_TRESHOLD and battery_state == 'Discharging'):
    os.system('echo "done" > /home/tim/done')

if (energy_percent < ALERT_TRESHOLDS and battery_state == 'Discharging'):
    Notify.init("Battery low")
    battery_notif = Notify.Notification.new("Battery low", 
            "Low battery, the computer will shut down if not connected in time.", "dialog-information")
    battery_notif.show()


