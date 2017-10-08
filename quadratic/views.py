# -*- coding: utf-8 -*-
from math import sqrt
from django.shortcuts import render


def quadratic_results(request):
    a_err = ''
    a = request.GET.get('a', '')
    if not a:
        a_err = 'коэффициент не определен'
    else:
        try:
            a = int(a)
        except (TypeError, ValueError):
            a_err = 'коэффициент не целое число'

        if a == 0:
            a_err = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    b_err = ''
    b = request.GET.get('b', '')
    if not b:
        b_err = 'коэффициент не определен'
    else:
        try:
            b = int(b)
        except (TypeError, ValueError):
            b_err = 'коэффициент не целое число'

    c_err = ''
    c = request.GET.get('c', '')
    if not c:
        c_err = 'коэффициент не определен'
    else:
        try:
            c = int(c)
        except (TypeError, ValueError):
            c_err = 'коэффициент не целое число'
    if a and (b or b == 0) and (c or c == 0):
        disc = b * b - 4 * a * c
    else:
        disc = None
    if disc > 0:
        x1 = (-b + sqrt(disc)) / (2 * a)
        x2 = (-b - sqrt(disc)) / (2 * a)
    elif disc == 0:
        x1 = x2 = -b / (2 * a)
    else:
        x1 = x2 = None
    return render(request,
                  'quadratic/results.html',
                  {'a': a,
                   'b': b,
                   'c': c,
                   'disc': disc,
                   'x1': x1,
                   'x2': x2,
                   'a_err': a_err,
                   'b_err': b_err,
                   'c_err': c_err,
                   })