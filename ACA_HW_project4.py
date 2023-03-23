from time import sleep
import logging
import datetime

from functools import wraps
logging.basicConfig(filename='performance.log',level=logging.INFO,encoding='utf-8', format='%(message)s',filemode='w')

def profile(func):
    def wrapper( *args,**kwargs):
        start = datetime.datetime.now()
        formatted_date = start.strftime("%Y-%m-%d %H:%M:%S.%f")
        result = func(*args)
        end = datetime.datetime.now()-start
        logging.info("%s - foo(%s) - %s", start, args,end)
        #logging.info("%s - foo(%d) - %s",logging.info(start),logging.info(args),logging.info(end))
        return result
    return wrapper

@profile
def foo(x):
    sleep(2)
    return x ** 2