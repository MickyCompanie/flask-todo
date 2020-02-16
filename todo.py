from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

tasks = [
    {
        'title': 'First Task',
        'text': 'this is obviously the text of the first task'
    },
    {
        'title': 'Second Task',
        'text': 'this is obviously the text of the second task'
    },
    {
        'title': 'Third Task',
        'text': 'this is obviously the text of the third task'
    }
]

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    text = db.Column(db.String(200))


@app.route('/')
@app.route('/home')
def index():
    todos = Todo.query.all()
    return render_template('index.html', title="Home", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    # todo = Todo(request.form)
    
@app.route('/delete', methods=['POST'])
def delete():
    todo = Todo.querry.filter_by(id=int(id)).first()
    todo.delete()
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)