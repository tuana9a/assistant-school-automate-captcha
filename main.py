import services.AskMasterService as AskMasterService
import flaskr
import yaml
import threading
import json

with open('./config/server.yml') as f:
    config_server = yaml.load(f, Loader=yaml.FullLoader)


def set_interval(func, sec, delay=True):
    def func_wrapper():
        set_interval(func, sec)
        func()

    if(not delay):
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def askMaster():
    url = config_server['master-address'] + '/api/worker/ask/worker-address'
    data = json.dumps({
        'from':  {
            'name': 'assistant-school-automate-captcha',
            'address': config_server['address']
        },
        'asks': ['assistant-school-automate-captcha']
    })

    AskMasterService.askWorkerAddress(url, data)


print(' * thread: start ask master')
set_interval(askMaster, 10, False)

app = flaskr.create_app()
print(' * listen: ' + config_server['address'])
app.run(host='0.0.0.0', port=config_server['port'])
