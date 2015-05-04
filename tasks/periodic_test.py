from frontend.webapp import celery


@celery.task(name="periodic_test")
def add_test(a, b):
    print "I added things!", str(a + b)
    return a + b
