import os
import sys

from app import create_app
from flask_script import Manager, Shell

from app import create_app

sys.path.insert(0, os.path.dirname(_file_))

application = create_app(os.getenv('FLASK_ENV') or 'config.ProductionConfig')
manager = Manager(application)

# these names will be available inside the shell without explicit import
def make_shell_context():
    return dict(app=application)

manager.add_command('shell', Shell(make_context=make_shell_context))

if _name_ == '_main_':
    manager.run()
