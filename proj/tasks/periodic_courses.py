from __future__ import absolute_import
from proj.celery import app
from proj.tasks.get_cursos import get_cursos,vacantes

from celery.task import periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from datetime import timedelta,datetime
import os,json

logger = get_task_logger(__name__)

def vacantes(curso):
    return '{4}) {0: <7} - {1: <50} - {2}/{3}'.format(
                            curso['sigla'],
                            curso['curso'],curso['ocu'],
                            curso['ofr'],curso['NRC']
                            )

def save_output(data,file='entries.json'):
    with open(file,'a') as f:
        f.write("{}\n".format(json.dumps(data)))

def output_data(data):
    return {'timestamp':datetime.now().timestamp(),'data':data}

#@periodic_task(run_every=timedelta(minutes=15),ignore_result=True)
@periodic_task(run_every=crontab(minute="*/10" hour='8-22'))
def refresh_courses():
    fix = ['14658','13739']
    nrcs = ['12390','12442','12510','12528',
        '12669','14658','13739','12014']

    nrcs2 = ['16923','14352','13573',
     '15011','13245','13249']

    guille = ['13859', '11059', '12442' ,'16256','12528']

    courses = get_cursos(nrcs,fix)
    courses2= get_cursos(nrcs2)
    courses3= get_cursos(guille)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("{0:=^80}\n".format('MATIAS'))
    save_output(output_data(courses))
    i = 0
    for course in courses:
        print(vacantes(course))
        i+=1
    print('{0:=^80}\n'.format("ALVARO"))
    for course in courses2:
        print(vacantes(course))
    print("{0:=^80}\n".format('GUILLERMO'))
    for course in courses3:
        print(vacantes(course))
