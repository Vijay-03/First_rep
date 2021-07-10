# import time
#
# print(time.gmtime(0))
#
# print(time.localtime())
#
# # using tuple
# time_here = time.localtime()
# print(time_here)
# # printing result using tuple
# print(time_here[0])
# print(time_here[1])
# print(time_here[2])
# # using method
# print(time_here.tm_year)
# print(time_here.tm_mon)
# print(time_here.tm_day)


# import time
# from time import time as my_timer   # three other function we can use in place of time r
# import random                       # perf_counter, monotonic, process_time
#
# input("press enter to start")
#
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("press enter to stop")
#
# end_time = my_timer()
#
# print("Started at " + time.strftime("%X", time.localtime(start_time)))
# print("Ended at " + time.strftime("%X", time.localtime(end_time)))
#
# print("Your reaction time was {} seconds".format(end_time - start_time))

# challenge
# write a small program to display the info on the four clocks using the four time functions
# i.e - time, perf_counter, monotonic, process_time.

import time

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_time():\t", time.get_clock_info('time'))
print("monotonic():\t", time.get_clock_info('time'))
print("process_time():\t", time.get_clock_info('time'))


