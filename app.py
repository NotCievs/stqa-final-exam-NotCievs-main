from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    data = request.form
    student = {
        "name": data['name'],
        "subject": data['subject'],
        "grade": int(data['grade']) 
    }
    students.append(student)
    return redirect(url_for('index'))

@app.route('/api/students')
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
