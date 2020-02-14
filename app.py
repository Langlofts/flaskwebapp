from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)
dogCount:int =0
catCount:int =0
@app.route('/')
def index():
   return render_template('welcome.html', count1=dogCount,count2 =catCount)
@app.route('/cat')
def addCat():
    global catCount
    catCount=catCount+1
    return redirect(url_for('index'))
@app.route('/dog')
def addDog():
    global dogCount
    dogCount = dogCount+1
    return redirect(url_for('index'))
if __name__ == '__main__':
   app.run()