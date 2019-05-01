#!/usr/bin/env python3

import wtforms
import flask
from flask import request
import linequations

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'devel'

class InputForm(wtforms.Form):
    """ Input form for number of equations and variables. """
    num_eq = wtforms.IntegerField('Number of equations: ')
    num_var = wtforms.IntegerField('Number of variables: ')

def get_result(coefficients, constants, variables):
    """ Generate latex representation of matrix. """
    matrix = '$$\\begin{pmatrix}'
    for i, k in enumerate(coefficients):
        for j in k:
            matrix += ' {} &'.format(j)
        matrix += ' {} \\\\'.format(constants[i])
    matrix += '\\end{pmatrix}$$'

    unknowns = '$$\\begin{cases}'
    for i, var in enumerate(variables):
        unknowns += 'x_{{{}}} = {};\\\\ '.format(i+1, var)
    unknowns += '\\end{cases}$$'

    return {
        "matrix": matrix,
        "unknowns": unknowns,
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    """ Index page. """
    form = InputForm(flask.request.form)
    matrix = request.cookies.get('matrix')
    unknowns = request.cookies.get('unknowns')
    if request.method == 'POST' and form.validate():
        result = get_result(*linequations.create_system(form.num_eq.data, form.num_var.data))
        resp = flask.make_response(flask.redirect(flask.url_for('index')))
        resp.set_cookie("matrix", result["matrix"])
        resp.set_cookie("unknowns", result["unknowns"])
        return resp
    return flask.render_template('index.html', form=form, matrix=matrix, unknowns=unknowns)

if __name__ == '__main__':
    app.run()
