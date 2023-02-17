from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id" : 1,
    "title" : "Data Analyst",
    "location" : "San Francisco, USA",
    "salary" : "$ 100,000"
  },
  {
    "id" : 2,
    "title" : "Data Scientist",
    "location" : "San Diego, USA",
    "salary" : "$ 150,000"
  },
  {
    "id" : 3,
    "title" : "Data Engineer",
    "location" : "Remote",
    #"salary" : "$ 145,000"
  },
  {
    "id" : 4,
    "title" : "Frontend Engineer",
    "location" : "Lagos, Nigeria",
    "salary" : "$ 45,000"
  },
]


@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS, company_name="Joeyrocksbs")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
