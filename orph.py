from setup import create_app, db
from setup.models import User, Orphanage, Message, Donation

app = create_app()

# the decorator below registers the function as a shell context function
@app.shell_context_processor 
def make_shell_context():
    return {'db': db,'User': User, 'Orphanage': Orphanage, 'Message': Message, 'Donation': Donation}