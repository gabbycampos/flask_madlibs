from flask import Flask, request, render_template, redirect
from stories import story

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home_page():
#   return render_template('base.html')

# @app.route('/form')
# def form():
#   return render_template('form.html')

# @app.route('/story')
# def show_story():
#   place = request.args['place']
#   noun = request.args['noun']
#   verb = request.args['verb']
#   adjective = request.args['adjective']
#   # nouns = request.args['nouns']
#   return render_template('story.html', place=place, noun=noun, verb=verb, adjective=adjective)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
