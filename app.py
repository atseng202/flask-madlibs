from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story, stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/questions")
def show_story_form():
    """ Shows the Madlib story form  """

    story_category = request.args['story-templates']
    story = stories.get(story_category)

    return render_template("questions.html", story_category=story_category, prompts=story.prompts)

@app.route("/results")
def display_story():
    """ Diplay story on story.html """
    
    story_type = request.args.get('story-type')
    # can we do jquery here to get data-attributes?
    text = stories.get(story_type).generate(request.args)
    return render_template("story.html", text=text)

    
@app.route("/")
def index():
    """ Display home page with stories templates to select from """
   
    return render_template("index.html", templates=stories)


