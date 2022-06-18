from flask import Flask,  redirect, url_for
app = Flask(__name__)

@app.route('/1')
def hello_world():
   return 'Server is running fine..'

@app.route('/getUserInfo/<id>', methods=['POST'])
#http://192.168.0.109:5001/getUserInfo/1
def getUserInfo(id):
    data = {"name": "ravi",          "email":"ravi@gmail.com"}
    print(id)
    return data

@app.route('/blog/<int:postID>') # it will accespt only int value
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/user/<name>',                   methods=['GET']) ## example runtime url creation and execute
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

#methods = ['POST', 'GET']


if __name__ == '__main__':
   app.run(host="0.0.0.0" ,port="5001", debug=True)
   ##app.add_url_rule(‘/’, ‘hello’, hello_world)


#######

"""
http://localhost:5000/   // deafult get
http://localhost:5000/getBooks // get
//http://127.0.0.1:5000
http://192.168.0.109:5001
"""