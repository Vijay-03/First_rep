#
# program that allows a user to choose one of the time zones
# to display the date and time in a format suitable for the
# user of your program to understand

import pytz
import datetime

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Japan"}

print("please choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print("\t{} {}".format(place, available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print()

