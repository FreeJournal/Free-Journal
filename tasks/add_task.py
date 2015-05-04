from frontend.webapp import celery


@celery.task()
def add_together(a, b):
    print "running add task!"
    return a + b
