from flask.ext.script import Manager,Shell
from app import create_app


app=create_app()
manager=Manager(app)

def make_shell_context():
	return dict(app=app)

manager.add_command('sehll',Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()