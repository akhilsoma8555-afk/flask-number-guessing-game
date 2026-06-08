import random
from flask import Flask,render_template,request
app=Flask(__name__)
rnum=random.randint(1,10)
a=0
score="0❌"
name=""
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/start", methods=["POST"])
def start():
    global name

    name = request.form["name"]
    print("Start button clicked")
    return render_template(
        "index.html",
        name=name,
        score=score
    )
@app.route('/play',methods=['POST'])
def play():
    global rnum,a,score
    n=int(request.form['guess'])
    if n==rnum:
        if a==0:
            score=f'100🏆'
        elif a==1:
            score='75🥈'
        elif a==2:
            score='50🥉'
        result="🎉You guessed it right..."
        rnum=random.randint(1,10)
        a=0
        
    else:
        a+=1
        if a>=3 :
            result="💀Game Over... The number was "+str(rnum)
            score="0❌"
            rnum=random.randint(1,10)
            a=0
        elif n>rnum:
            result=f"📈TOO HIGH... Attempt {a}/3"
        elif n<rnum:
            result=f"📉TOO LOW... Attempt {a}/3"
    return render_template("index.html", result=result,score=score,name=name)

if __name__=='__main__':
    app.run(debug=True)








