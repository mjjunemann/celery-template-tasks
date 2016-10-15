from __future__ import absolute_import
from proj.tasks.os_task import invokeProgram
from proj.tasks.print_job import output_log
from proj.tasks.get_cursos import get_cursos,vacantes

if __name__ == '__main__':
    ## PROBAR ASYNTASK ..
    #get_cursos(['12390','12528'])
    b = ['12390','12442','12510','12528',
        '12669','14658','13739','12014','10028']
    #a = ['16923','14352','13573',
    #'15011','13245','13249']
    fix = ['14658','13739']
    courses1 = get_cursos(b,fix)
    print(courses1)
    #courses2 = get_cursos(a)
    for course in courses1:
        vacantes(course)
    #for course in courses2:
    #    vacantes(course)
