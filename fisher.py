from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', debug=app.config['DEBUG'], port=5001, threaded=True)
