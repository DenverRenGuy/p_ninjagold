from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'ShhhSneaky'


#List of Activities

activitys = []

#Variable for Total Gold
goldCount = 0
newGold = 0

@app.route('/')
def index():
    if not 'goldCount' in session:
        session['goldCount'] = 0
    if not 'activitys' in session:
        session['activitys'] = []
        print session['activitys']
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        newGold = random.randrange(10,21)
        session['goldCount'] = session['goldCount'] + newGold
        prepActivity(newGold, request.form['building'])
        print session['activitys']
        return redirect('/')
    elif request.form['building'] == 'cave':
        newGold = random.randrange(5,11)
        session['goldCount'] = session['goldCount'] + newGold
        prepActivity(newGold, request.form['building'])
        return redirect('/')
    elif request.form['building'] == 'house':
        newGold = random.randrange(2,6)
        session['goldCount'] = session['goldCount'] + newGold
        prepActivity(newGold, request.form['building'])
        return redirect('/')
    elif request.form['building'] == 'casino':
        newGold = random.randrange(-50,51)
        session['goldCount'] = session['goldCount'] + newGold
        prepActivity(newGold, request.form['building'])
        return redirect('/')
    elif request.form['building'] == 'clear':
        session.clear()
        return redirect('/')
    else:
        pass

def prepActivity(num, str):
    if num >0:
        style = 'gain'
    else:
        style = 'loss'
    session['activitys'].append({'style':style, 'activity':'Earned %d gold from the %s' % (num, str) })
    return None


app.run(debug=True)
