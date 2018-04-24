import os
from flask_script import Manager, Server
from flask_script.commands import ShowUrls
from flask_migrate import Migrate, MigrateCommand
from mysite.extensions import db
from mysite import create_app

env = os.environ.get('APP_ENV', 'dev')
app = create_app('mysite.config.%sConfig' % env.capitalize())

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-url", ShowUrls())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db
    )


@manager.command
def setup_db():
    db.create_all()

if __name__ == "__main__":
    manager.run()
