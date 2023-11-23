from flask import Flask , render_template, jsonify
app=Flask(__name__)

JOBS=[
{
  'id':1,
  'title':"Data Analyst",
  'location':'Benguluru,India',
  'salary':'Rs 10,00,000'
},
  {
    'id':2,
    'title':"Data Science",
    'location':'Delhi,India',
    'salary':'Rs 15,00,000'
  },
  {
    'id':3,
    'title':"Software Engineer",
    'location':'Remote',
    'salary':'Rs 18,00,000'
  },
{
  'id':4,
  'title':"Devops Engineer",
  'location':'Haryana,India',
  'salary':'Rs 22,00,000'
},
{
  'id':5,
  'title':"Frontend Engineer",
  'location':'San Francisco',
},
{
  'id':6,
  'title':"Backend Engineer",
  'location':'Disney Land',
  'salary':'$ 12,000'
}
]

@app.route("/")
def hello_world():
  return render_template('home.html', Jobs=JOBS , company_name="Jarvis")
 

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)




    

