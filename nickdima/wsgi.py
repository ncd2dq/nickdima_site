import sys
sys.path.insert(0, "/app/nickdima")


from __init__ import create_app, socker

app = create_app()
socker.run(app)