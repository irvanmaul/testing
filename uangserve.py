from uang import getEjaanUang
from bottle import route, run, request
import json

@route('/uang')
def hello():
    value = request.GET.get('value', 20)

    if int(value) not in range(20, 1000 + 1):
        return 'error'
    else:
        return json.dumps({
            "value": value,
            "output": getEjaanUang(int(value))
        })

run(host='localhost', port=8888, debug=True)