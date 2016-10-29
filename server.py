from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'ShhhSneaky'


#List of Activities

activitys = []

#Variable for Total Gold
# Do you need these variables? Is there a reason to not just use 0 ?
goldCount = 0
newGold = 0

@app.route('/')
def index():
    if not 'goldCount' in session:
        session['goldCount'] = 0
    # #spelling. I luv it.
    if not 'activitys' in session:
        session['activitys'] = []
        print session['activitys']
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    # this is all groovy, but if you are feeling about upping the ante, How could you go about refactoring this all down into <15 lines?
    # Notice how much of this code is repeated structure and just different responses based off the form value? is there a way to associate 
    # responses with form inputs?
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
        # mayhaps, you should return or flash an error message if you end up here?
        pass

def prepActivity(num, str):
    if num >0:
        style = 'gain'
    else:
        style = 'loss'
    session['activitys'].append({'style':style, 'activity':'Earned %d gold from the %s' % (num, str) })
    return None


app.run(debug=True)
