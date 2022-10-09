import os

from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__)

    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)
 
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import trainer
    app.register_blueprint(trainer.bp)
    app.add_url_rule('/', endpoint='index')

    from . import client
    app.register_blueprint(client.bp)

    return app
