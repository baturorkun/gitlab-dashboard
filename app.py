from pprint import pprint

from flask import Flask, render_template
from config import Config
from flask import request
from gitlab import Gitlab

app = Flask(__name__)


@app.route('/')
def index():
    config = Config()
    cfg = config.parseConfig()
    return render_template('main.html', projects=cfg["projects"])

#@app.route('/project/<id>', methods=('GET', 'POST'))
#def project1(id):
#    config = Config()
#    cfg = config.parseConfig()
#    mgl = MyGitlab(cfg["gitlab"]["url"], cfg["gitlab"]["token"])
#    if id == "":
#        id = request.args.get('id')
#
#    return render_template('project.html', project=mgl.projectsGet(id))


@app.route('/project', methods=('GET', 'POST'))
def project():
    gl = Gitlab()
    project_id = request.args.get('id')
    data = gl.getProject(project_id)
    return render_template('project.html', project=data)


@app.route('/projects/all', methods=('GET', 'POST'))
def projects():
    gl = Gitlab()
    data = gl.getAllProjects()
    return render_template('projects.html', projects=data)


@app.route('/pipelines', methods=('GET', 'POST'))
def pipelines():
    id = request.args.get('id')
    gl = Gitlab()
    data = gl.getPipelines(id)
    return render_template('pipeline.html', data=data)


@app.route('/pipelines/latest', methods=('GET', 'POST'))
def latestPipeline():
    project_id = request.args.get('id')
    gl = Gitlab()
    data = gl.getLatestPipeline(project_id)

    return render_template("pipeline.html", data=data)


@app.template_filter("test")
def test(num):
    return "batur"

@app.context_processor
def util_funtion():
    def gitUrl(path):
        config = Config()
        cfg = config.parseConfig()
        return cfg["gitlab"]["url"] + "/" + path
    return {"gitUrl": gitUrl}


# export FLASK_DEBUG=1
app.run(host='0.0.0.0', port=81, debug=True)
