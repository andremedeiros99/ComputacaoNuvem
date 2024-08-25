from flask import Flask, render_template, redirect, url_for, request
from models import db, Client
from forms import ClientForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients', methods=['GET', 'POST'])
def manage_clients():
    form = ClientForm()
    if form.validate_on_submit():
        new_client = Client(
            name=form.name.data,
            cpf=form.cpf.data,
            birth_date=form.birth_date.data,
            email=form.email.data
        )
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('manage_clients'))
    clients = Client.query.all()
    return render_template('list_client.html', form=form, clients=clients)

@app.route('/clients/<int:id>/edit', methods=['GET', 'POST'])
def edit_client(id):
    client = Client.query.get_or_404(id)
    form = ClientForm(obj=client)
    if form.validate_on_submit():
        form.populate_obj(client)
        db.session.commit()
        return redirect(url_for('manage_clients'))
    return render_template('edit_client.html', form=form, client=client)

@app.route('/clients/<int:id>/delete', methods=['POST'])
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('manage_clients'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')
