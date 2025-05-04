from flask import Flask,render_template,redirect,request,url_for,session,g


app=Flask(__name__)
app.secret_key='LibaTaneem'

class User:
    def __init__(self,userid,username,password):
        self.id=userid
        self.username=username
        self.password=password

@app.before_request
def before_request():
    g.user=None
    if 'user_id' in session:
        user=next((x for x in users if x.id==session['user_id']),None)
        g.user=user

users=[]
users.append(User(1,'farhan','2307'))
users.append(User(2,'sharath','2508'))
users.append(User(3,'tharun','212'))


@app.route("/")
def index():
    return redirect(url_for('login'))


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        session.pop('user_id',None)
        username=request.form["username"]
        password=request.form["password"]

        user=next((x for x in users if x.username==username),None)
        if user and user.password==password:
            session['user_id']=user.id
            return redirect(url_for('profile'))
        return redirect(url_for('login'))

    return render_template("login.html")



@app.route('/register', methods=["GET","POST"])
def register():
    if request.method=='POST':
        username=request.form["username"]
        userid=request.form["userid"]
        password=request.form['password']
        if username and userid and password:
            users.append(User(userid,username,password))
        return redirect(url_for('login'))
    return render_template('registration.html')



@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template("profile.html")

for i in users:
    print(i.username)


if __name__=="__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)