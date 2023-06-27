from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs.10,000'
  },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',

  },
  {
    'id': 3,
    'title': 'Frontend Guru',
    'location': 'Remote',
    'salary': '$120,000'
  },
  {
    'id': 4,
    'title': 'Analyst',
    'location': 'S. Francisco, USA',
    'salary': '$50,000'
  }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)