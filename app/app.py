from flask import Flask, render_template
import urllib.request, json
import sys

name="My Career App"
app = Flask(__name__)

@app.route("/")
def get_jobs():
  url = "http://api:5000/jobs"
  
  response = urllib.request.urlopen(url)
  data = response.read()
  list = json.loads(data)

  print(list, file=sys.stderr)

  return render_template("home.html", name=name, job_list=json.dumps(list))
  
@app.route("/job/<id>")
def jobs(id):
  return render_template("job.html", job_id=id)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)