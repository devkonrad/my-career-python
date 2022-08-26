from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")
  
@app.route("/job/<id>")
def jobs(id):
  return render_template("job.html", job_id=id)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)