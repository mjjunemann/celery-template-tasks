BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_IMPORTS = (
                    'proj.tasks.os_task',
                    'proj.tasks.test_task',
                    'proj.tasks.get_cursos',
                    'proj.tasks.periodic_courses'
                )


# CELERY_ANNOTATIONS = {
#     'tasks.add': {'rate_limit': '10/m'}
# }
