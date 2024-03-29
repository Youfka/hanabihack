import random

from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Prof

app = Flask(__name__)
CORS(app)

engine = create_engine('sqlite:///data.db')
session = Session(bind=engine)


@app.route('/api/userToProf')
def profile():
    random_user = []
    labels = []

    sql_developer = []
    java_developer = []
    data_scientist = []
    data_engineer = []
    backend_developer = []
    frontend_developer = []
    qa_engineer = []
    databases_administrator = []
    devops = []
    javascript_developer = []

    for i in session.query(Prof).all():
        if i.language in ['R', 'F#', 'Other(s):', 'Erlang', 'nan', 'Dart', 'Rust', 'Objective-C', 'VBA', 'Clojure',
                          "Bash/Shell/PowerShell", "WebAssembly", "Assembly", "Elixir"
                          ]:
            continue
        random_user.append(round(random.random() / 5, 3))
        labels.append(i.language)
        sql_developer.append(i.sql_developer)
        java_developer.append(i.java_developer)
        data_scientist.append(i.data_scientist)
        data_engineer.append(i.data_engineer)
        backend_developer.append(i.backend_developer)
        frontend_developer.append(i.frontend_developer)
        qa_engineer.append(i.qa_engineer)
        databases_administrator.append(i.databases_administrator)
        devops.append(i.devops)
        javascript_developer.append(i.javascript_developer)

    datasets = [
        {'label': 'sql_developer', 'data': sql_developer},
        {'label': 'java_developer', 'data': java_developer},
        {'label': 'data_scientist', 'data': data_scientist},
        {'label': 'data_engineer', 'data': data_engineer},
        {'label': 'backend_developer', 'data': backend_developer},
        {'label': 'frontend_developer', 'data': frontend_developer},
        {'label': 'qa_engineer', 'data': qa_engineer},
        {'label': 'databases_administrator', 'data': databases_administrator},
        {'label': 'devops', 'data': devops},
        {'label': 'javascript_developer', 'data': javascript_developer},
    ]

    return jsonify({
        'labels': labels,
        'datasets': [
            {
                'label': 'Your skills',
                'data': random_user,
            },
            *datasets,
        ]
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
