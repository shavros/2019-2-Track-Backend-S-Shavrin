def handler(environ, start_response):
    age = 10
    if age < 18:
        data = b'You are very young yet'
    elif age >= 18:
        data = b'Oh, you are so adult'
    headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(data)))]
    start_response('200 OK', headers)
    return [data]

