import config
from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html", tasks=tasks)

# Instead of a list of strings, we use a list of dictionaries
tasks = []

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("task")
    if task_text:
        tasks.append({"task": task_text, "done": False})
    return redirect(url_for("home"))

@app.route("/done/<int:task_id>", methods=["POST"])
def done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
    return redirect(url_for("home"))

    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=config.PORT,debug=config.DEBUG, host=config.HOST)