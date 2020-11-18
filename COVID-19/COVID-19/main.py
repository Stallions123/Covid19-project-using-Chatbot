from flask import Flask,render_template, request
app = Flask(__name__)
import pickle


#Open a file where you store the pickle data
file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()


@app.route('/',methods=["GET","POST"])
def hello_world():
   
    if request.method == "POST":
       myDict = request.form
       Fever= int(myDict['Fever'])
       Age = int(myDict['Age'])
       Pain = int(myDict['Pain'])
       runnynose = int(myDict['runnynose'])
       breathingdifficulty = int(myDict['breathingdifficulty'])
       #Code For Inference
       inputfeatures = [Fever, Pain, Age, runnynose, breathingdifficulty]
       infProb = clf.predict_proba([inputfeatures])[0][1]
       print(infProb)
       return render_template('show.html',inf=round(infProb*100))
    return render_template('index.html')
    # return 'Hello,World'+str(infProb)

if __name__== "__main__":
    app.run(debug=True)