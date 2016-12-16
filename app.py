from bottle import route, run, template, request
import parsing

gbl = dict()
gbl['data'] = []

@route('/')
def home():
    return gbl

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/bjork', method='POST')
def do_a_thing():
    data = request.body.read()

    form_data = parsing.parse_form_to_dict(data)

    gbl['data'].append(form_data)

run(host='0.0.0.0', port=8080)
