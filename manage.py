#!/usr/bin/env python
import os
from flask_script import Manager

from app import app
import config

#app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(config.DevelopmentConfig)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

