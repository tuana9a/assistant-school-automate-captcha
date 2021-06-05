import requests


def askWorkerAddress(url, data):
    try:
        response = requests.post(url, data)
        return response
    except:
        print(' * thread: ask master failed')
        return 'Err: ask master failed'
