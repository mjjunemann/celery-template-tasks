from __future__ import absolute_import
from proj.celery import app

import subprocess

@app.task
def invokeProgram(*args):
    res = subprocess.check_output(['java','-la']).decode('utf-8')

    return res

def invoke_program(program=None):
    if not(program):
        return
    #subprocess.check_output()

if __name__ == '__main__':
    pass
