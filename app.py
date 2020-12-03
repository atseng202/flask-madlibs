from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/questions")
def show_story_form():
    """ Shows the Madlib story form  """

    return render_template("questions.html", prompts=silly_story.prompts)


@app.route("/results")
def display_story():
    """ Diplay story on story.html """
    
    text = silly_story.generate(request.args)
    return render_template("story.html", text=text)

    

