from __future__ import absolute_import
from proj.celery import app

import requests
import json
from lxml import html

URL = "http://buscacursos.uc.cl/"
URL2 = "http://buscacursos.uc.cl/informacionVacReserva.ajax.php"

def make_request2(semester="2016-2",nrc=None):
    params = {}

    params['termcode'] = semester
    params['nrc'] = nrc
    print(params)
    res = requests.get(URL2,params)
    print(res.url)
    return res


def get_curso2(nrc):
    response = make_request2(nrc=nrc)
    text = response.text
    tree = html.fromstring(text)
    a = tree.xpath('//tr[@class="resultadosRowPar"]//text()|//tr[@class="resultadosRowImpar"]//text()')
    a = map(lambda x: x.strip(),a)
    a = list(filter(lambda x: x != '' , a))
    print(a)

    i = 0
    tmp = []
    for j in range(1, len(a) + 1):
        if j == len(a) or a[j].isnumeric() and len(a[j]) >= 4:
            tmp.append(get_info(a[i:j]))
            i = j
    print(tmp)
def get_info2(datos_curso):
    data = dict()
    #print(datos_curso)

    cat = ['curso', 'NRC', 'semester', 'sigla', 'sec', 'apr', 'curso',
           'profesor', 'campus', 'cred', 'ofr', 'ocu', 'disp']
    print("==============="*5)
    print(datos_curso)
    print("==============="*5)
    data.update(dict(zip(cat, map(clean, datos_curso))))
    return data

def vacantes(curso):
    print('{4}) {0: <7} - {1: <50} - {2}/{3}'.format(curso['sigla'],curso['curso'],curso['ocu'],curso['ofr'],curso['NRC']))

def make_request(semester="2016-2",nrc=None,sigla=None):
    params = {}

    params['cxml_nrc'] = nrc
    params['cxml_semestre'] = semester
    params['cxml_sigla'] = sigla

    res = requests.get(URL,params)
    return res

def clean(val):
    if isinstance(val, list):
        return val
    if val.isnumeric():
        return int(val)
    return val.strip()

def get_info(datos_curso,fix=False):
    data = dict()
    cat = ['NRC', 'sigla', 'retiro', 'eng', 'sec', 'apr', 'curso',
           'profesor', 'campus', 'cred', 'ofr', 'ocu', 'disp']
    if len(datos_curso) >= 19 or fix:
        cat.insert(8,'profesor2')
    data.update(dict(zip(cat, map(clean, datos_curso))))
    return data

def get_curso(nrc,fix=None):
    response = make_request(nrc=nrc)
    response.encoding = 'utf-8'
    text = response.text
    tree = html.fromstring(text)
    a = tree.xpath('//tr[@class="resultadosRowPar"]//text()|//tr[@class="resultadosRowImpar"]//text()')
    a = map(lambda x: x.strip(), a)
    a = list(filter(lambda x: x != '' and x != ",", a))
    i = 0

    return get_info(a,fix)

def get_cursos(cursos,fix=None):
    courses = []
    fix = [] if fix == None else fix
    for curso in cursos:
        if curso in fix:
            courses.append(get_curso(curso,True))
        else:
            courses.append(get_curso(curso))
    return courses
