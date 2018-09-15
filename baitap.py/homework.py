from flask import Flask
homework=Flask(__name__)
@homework.route("/")
def new():
    return "xin chao"
@homework.route("/bmi/<int:x>/<int:y>")
def news(x, y):   
    bmi=x/((y/100)*2)
    if bmi < 16 :
        return "thieu can nang"
    elif 16 <= bmi < 18.5:
        return "thieu can"
    elif 18.5 <= bmi < 25:
        return "binh thuong"
    elif 25 <= bmi < 30:
        return "thua can"
    elif bmi > 30:
        return "beo phi" 
if __name__=="__main__":
    homework.run(debug=True)