import sys
sys.path.insert(0, "/app/nickdima")


from __init__ import create_app, socker

if __name__ == '__main__':
    app = create_app()
    socker.run(app)