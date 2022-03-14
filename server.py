from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)   

app.secret_key = "hnvoaerv"

@app.route('/')          
def basic():
    return render_template('index.html')

#never use render template on a route that uses post
@app.route('/result', methods =['POST'])          
def processed():
    session['roche'] = request.form['Name']
    session['me'] = request.form['state']
    session['myself'] = request.form['language']
    session['andI'] = request.form['comments']
    return redirect('/result')

@app.route('/result')          
def meme():
    return render_template('secondpageerickmadememake.html',
    rochelle = session['roche'], place = session['me'], code = session['myself'], what_i_really_want_to_say = session['andI'])



if __name__=="__main__":  
    app.run(debug=True)    

