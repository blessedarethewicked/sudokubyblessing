from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from solve_algorithm import solving_algorithm
import read_from_file
solve_flag = False
grid = read_from_file.read_game_file()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Num(db.Model):
	grid = []
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), unique=True, nullable=False)
	def __repr__(self):
		self.grid = grid
		return '<User %r>' % self.content
	
gridvalues = Num(content = '1',grid = grid)

@app.route('/', methods=["POST","GET"])
def index():
	global solve_flag
	if request.method == 'POST':
		task_content = request.form['content']
		array = [int(x) for x in task_content.split()] 
		
		#makes sure that we do not have to 
		if(len(array) == 3):
			print(array)
			gridvalues.grid[array[0]-1][array[1]-1] = array[2]
		try:
			return redirect('/')
		except:
			return 'error adding to database : tasks already there'
	
	else:
		try:
			num1 = gridvalues.grid
		except:
			return 'error adding to database : tasks already there'
		return render_template('index.html',num = num1)
	
@app.route('/solver')
def solver():
	gridvalues.grid = read_from_file.read_game_file()
	gridvalues.grid = solving_algorithm(gridvalues.grid)
	gridvalues.grid = solving_algorithm(gridvalues.grid)
	gridvalues.grid = solving_algorithm(gridvalues.grid)
	gridvalues.grid = solving_algorithm(gridvalues.grid)
	gridvalues.grid = solving_algorithm(gridvalues.grid)
	gridvalues.grid = solving_algorithm(gridvalues.grid)
	print(gridvalues.grid)
	global solve_flag
	solve_flag = True
	return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
	