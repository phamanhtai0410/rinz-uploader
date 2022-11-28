# -*- coding: utf-8 -*-
<<<<<<< HEAD
from flask_cors import CORS
=======
# from flask_cors import CORS
>>>>>>> 51f9606baafe2880c6bd024958d1450fab213b46

from gevent import monkey
monkey.patch_all()

from src import create_app
from flask_script import Manager

app = create_app()
<<<<<<< HEAD
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})
=======
# cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})
>>>>>>> 51f9606baafe2880c6bd024958d1450fab213b46
manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""

    app.run(host='0.0.0.0')


manager.add_option('-c', '--config',
                   dest="config",
                   required=False,
                   help="config file")

if __name__ == "__main__":
    manager.run()
