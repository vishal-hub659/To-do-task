from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Each task has: title, due_date, is_completed
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    due_date = request.form.get('due_date')

    if title and due_date:
        task = {
            'title': title,
            'due_date': due_date,
            'is_completed': False
        }
        tasks.append(task)
    return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
    if 0 <= index < len(tasks):
        tasks[index]['is_completed'] = not tasks[index]['is_completed']
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
