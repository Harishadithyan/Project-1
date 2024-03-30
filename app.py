from flask import Flask , render_template,jsonify
app=Flask(__name__)
JOBS = [
    {
        'id':'1',
        'title':'class 9',
        'Duration':' 1 Year course',
        'Fees': '1000 per month '
    },
    {
        'id':'2',
        'title':'class 10',
        'Duration':' 1 Year course',
        'Fees': '2000 per month '
    },
    {
        'id':'3',
        'title':'class 11',
        'Duration':' 1 Year course',
        'Fees': '3000 per month '
    },
    {
        'id':'4',
        'title':'class 12',
        'Duration':' 1 Year course',
        'Fees': '4000 per month'
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