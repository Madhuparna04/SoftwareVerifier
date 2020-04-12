from flask import * 
import re

app = Flask(__name__)  

def parse_py(name):
	txt = []
	exp = "def "
	with open(name) as f:
		lines = [line.rstrip() for line in f]
	for line in lines:
		x = re.search(exp, line)
		if not (x == None):
			txt.append(line)
			txt.append(line)
	return txt

def parse_file(name, extension):
	if extension == "c":
		return parse_c(name)
	elif extension == "py":
		return parse_py(name)

def process_file(fname):
	x = fname.split(".")
	if len(x) >=2:
		if x[1] == "c" or x[1]=="cpp" or x[1]=="py":
			res = parse_file(fname, x[1])
			return res
		else:
			return x[1]
	else:
		return ""
 
@app.route('/')  
def upload():  
    return render_template("upload.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)
        res = process_file(f.filename)
        re = {"result":res}
        return render_template("all.html", res = re)  
  
if __name__ == '__main__':  
    app.run(debug = True)
