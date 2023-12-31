from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/display', methods=['POST'])
def display():
    rollno=request.form['roll']
    roll=rollno.upper()
    url='https://dhondi.cmrithyderabad.edu.in/sharedfiles/e0d341de643812c29a19aac35b9e7d87/studentPhotos/'+roll+'.jpg'
    return render_template('home.html',photo=True,li=url)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
