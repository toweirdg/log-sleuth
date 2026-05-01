from celery import Celery

celery_app = Celery(
    "worker", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)

celery_app.autodiscover_tasks(["app.workers"])

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serilizer="json",
    timezone="UTC",
    enable_utc=True,
)
