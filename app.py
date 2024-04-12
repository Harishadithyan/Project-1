from flask import Flask , render_template,jsonify
app=Flask(__name__)
JOBS = [
    {
        'id':'1',
        'title':'Fundamental Maths',
        'Duration': '1 month'
         
    },
    {
        'id':'2',
        'title':'Tamil reading',
        'Duration': '1 month'
    },
    {
        'id':'3',
        'title':'Tamil writing',
        'Duration': '1 month'
    },
    {
        'id':'4',
        'title':'Hindi reading and writing',
        'Duration': '1 month'
    }
]
@app.route('/')
def index():
  return render_template('home.html',jobs=JOBS, company_name='Sai')
@app.route('/api/class')
def classes():
  return jsonify(JOBS)
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)