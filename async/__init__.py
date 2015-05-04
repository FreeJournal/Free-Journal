from threading import Thread, Event
from functools import wraps
from time import sleep


def run_as_thread(func):
    """
    Decorator for making a function run as a new thread
    :param func: the function to run
    :return: the resulting thread object
    """
    @wraps(func)
    def thread_func(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    return thread_func


def repeat_periodic(interval):
    def decorator(func):
        def wrapper(*args, **kwargs):
            stop_event = Event()

            @run_as_thread
            def loop():
                while not stop_event.wait(interval):
                    try:
                        func(*args, **kwargs)
                    except Exception as e:
                        print "Repeated job error'd with message:", e.message
            loop()
            return stop_event
        return wrapper
    return decorator


def wait_for_interrupt(func, stop_event, args=[]):
    while True:
        try:
            sleep(10)
        except (KeyboardInterrupt, SystemExit):
            stop_event.set()
            func(*args)
            exit(0)
