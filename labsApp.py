from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route('/wsa2113')
def open():
	return render_template('adi_labs.html')

if __name__ == "__main__":
	app.run()