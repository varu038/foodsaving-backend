from celery import shared_task

"""
@shared_task.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
    """


@shared_task
def test(arg):
    print(arg)
