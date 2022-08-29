from flask import Flask, render_template
import urllib.request, json
import sys

name="My Career App"
app = Flask(__name__)

@app.route("/")
def get_jobs():
  return render_template("home.html", name=name)
  
@app.route("/job/<id>")
def jobs(id):
  return render_template("job.html", job_id=id)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)