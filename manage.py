from flask_script import Manager
from flipboard import create_app, db
from flask_migrate import Migrate, MigrateCommand

app = create_app('develop')

manage = Manager(app)
# 数据库迁移扩展
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
    import base64
    base64.b64encode()