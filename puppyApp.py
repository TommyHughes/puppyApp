from puppyApp import create_app

app = create_app(config_class='DevConfig')

if __name__ == '__main__':
    app.run()