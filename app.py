from flask import Flask, render_template, session, request, redirect, flash 
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey 

app = Flask(__name__)
app.config['SECRET_KEY'] ='it_is_what_it_is'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.debug = True

Response_key = "responses"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_start():
    return render_template("start.html", survey = survey)

@app.route("/begin", methods=['POST'])
def survey_begin():
    session[Response_key] = []
    return redirect("/question/0")

@app.route("/answer", methods=['Post'])
def handle_question():

    #get the response choice
    choices = request.form["answer"]

    #add the repsonse to the session 
    responses = session[Response_key]
    responses.append(choices)
    session[Response_key] = responses

    #when all question are answer 
    if (len(responses) == len(survey.questions)):
        return redirect("/end")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/question/1," )
def show_question(qid):
    responses = session.get(Response_key)

    if (responses is None):
        #trying to access to fast!
        return redirect("/")
    
    if (len(responses) == len(survey.question)):
        return redirect("/question/2")
        
    if (len(responses) != qid):
        flash(f"invalid question id: {qid}")
        return redirect(f'/question/{len(responses)}')
    
    question = survey.questions[qid]
    return render_template("question0.html", qid = survey.questions, question = question)

@app.route("/question/2," )
def show_question(qid):
    responses = session.get(Response_key)

    if (responses is None):
        #trying to access to fast!
        return redirect("/")
    
    if (len(responses) == len(survey.question)):
        return redirect("/question/3")
        
    if (len(responses) != qid):
        flash(f"invalid question id: {qid}")
        return redirect(f'/question/{len(responses)}')
    
    question = survey.questions[qid]
    return render_template("question0.html", qid = survey.questions, question = question)

@app.route("/question/3," )
def show_question(qid):
    responses = session.get(Response_key)

    if (responses is None):
        #trying to access to fast!
        return redirect("/")
    
    if (len(responses) == len(survey.question)):
        return redirect("/end")
        
    if (len(responses) != qid):
        flash(f"invalid question id: {qid}")
        return redirect(f'/question/{len(responses)}')
    
    question = survey.questions[qid]
    return render_template("question0.html", qid = survey.questions, question = question)


@app.route("/end")
def show_end ():
    return render_template("end.html")
