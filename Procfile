web: gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker -w 1 --log-file=- --chdir nickdima wsgi:app
