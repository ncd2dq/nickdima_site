import sys
sys.path.insert(0, "/app/nickdima")


from __init__ import create_app, socker

app = create_app()
socker.run(app, host='0.0.0.0', port=5000, debug=True)