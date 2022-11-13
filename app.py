from flask import Flask, render_template

app = Flask(__name__)

# create an index route to define the url
@app.route('/')

# define function for that route 
def index():
    return render_template('index.html') # no need to specify the folder, flask just knows

if __name__ == "__main__":
    app.run(debug=True)