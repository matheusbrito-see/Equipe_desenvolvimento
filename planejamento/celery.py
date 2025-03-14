from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planejamento.settings')
app = Celery('planejamento')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')