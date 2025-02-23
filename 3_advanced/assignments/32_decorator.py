# *********************************************************************
# content   = decorator assignment
# version   = 0.1.0
# date      = 2025-02-18
#
# author   = Garvey Chi - garveychi@gmail.com
# *********************************************************************


"""
0. CONNECT the decorator "print_process" with all sleeping functions.
   Print START and END before and after.

   START *******
   main_function
   END *********


1. Print the processing time of all sleeping functions.
END - 00:00:00


2. PRINT the name of the sleeping function in the decorator.
   How can you get the information inside it?

START - long_sleeping

"""


import time


# *********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args, **kwargs):
        print('START - {0}'.format(func.__name__))
        start_time = time.time()

        func(*args)                  # main_function

        end_time = time.time()
        process_time = end_time - start_time
        formatted_time = time.strftime('%H:%M:%S', time.gmtime(process_time))

        print('END - {0}'.format(formatted_time))
    return wrapper


# *********************************************************************
# FUNC
@print_process
def short_sleeping(name):
    time.sleep(.1)
    print(name)


@print_process
def mid_sleeping(name):
    time.sleep(2)
    print(name)


@print_process
def long_sleeping(name):
    time.sleep(4)
    print(name)


short_sleeping('power nap')
mid_sleeping('nap')
long_sleeping('bedtime')
