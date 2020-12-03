from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story, stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/questions")
def show_story_form():
    """ Shows the Madlib story form  """

    story = stories.get(request.args['story-templates'])


    return render_template("questions.html", story_type=, prompts=story.prompts)


@app.route("/results")
def display_story():
    """ Diplay story on story.html """
    
    text = silly_story.generate(request.args)
    return render_template("story.html", text=text)

    
@app.route("/")
def index():
    """ Display home page with stories templates to select from """
    templates = [silly_story, excited_story]
    return render_template("index.html", templates=stories)


