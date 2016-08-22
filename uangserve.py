from uang import konversiAngkaToEjaan
from bottle import route, run, request
import json

@route('/uang')
def hello():
    value = request.GET.get('value', 20)

    if int(value) == 0:
        print 'nol'
    else:
        return json.dumps({
            "value": value,
            "output": konversiAngkaToEjaan(int(value))
        })

run(host='localhost', port=8888, debug=True)