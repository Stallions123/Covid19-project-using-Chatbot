from chatbot import chatbot
from covid_india import states
from flask import Flask,render_template, request
from bs4 import BeautifulSoup as BS 
import requests
app = Flask(__name__)
import pickle


#Open a file where you store the pickle data
file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()


@app.route('/')
def real():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)

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

#linking the home page with others
@app.route('/contact')
def home():
	
	return render_template('contact.html')
	
@app.route('/services')
def services():
	
	return render_template('services.html')
	
@app.route('/FAQ')	
def blog():
	
	return render_template('FAQ.html')
	
@app.route('/')	
def homeself():
	
	return render_template('index.html')
	
@app.route('/About/Team')	
def home_team():
	
	return render_template('team.html')
	
@app.route('/About/Aims')	
def aboutus():
	
	return render_template('about.html')
	
	

	

	
#Linking the service page with another:
@app.route('/services/contact')
def services_contact():
	
	return render_template('contact.html')

app.route('/services/')
def services():
	
	return render_template('services.html')	
	
@app.route('/services/FAQ')	
def services_blog():
	
	return render_template('FAQ.html')
	
@app.route('/services/home')	
def service_home():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/Services/About/Team')	
def services_team():
	
	return render_template('team.html')
	
@app.route('/Services/About/Aims')	
def aim():
	
	return render_template('about.html')
	

	
#Linking the FAQ page with another:
@app.route('/FAQ/contact')
def blog_contact():
	
	return render_template('contact.html')

@app.route('/FAQ/')
def bloging():
	
	return render_template('FAQ.html')	
	
@app.route('/FAQ/services')	
def blog_service():
	
	return render_template('services.html')
	
@app.route('/FAQ/home')	
def blog_home():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/FAQ/About/Team')	
def blog_team():
	
	return render_template('team.html')
	
@app.route('/FAQ/About/Aims')	
def aim_faq():
	
	return render_template('about.html')
	

	
	
#Linking the contact page with another:
@app.route('/contact/')
def contact_self():
	
	return render_template('contact.html')

app.route('/contact/FAQ')
def contact_FAQ():
	
	return render_template('FAQ.html')
	
	
@app.route('/contact/FAQ')	
def contactf():
	
	return render_template('FAQ.html')
	
@app.route('/contact/home')	
def con_home():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/contact/services')	
def con_ser():
	
	return render_template('services.html')
	
@app.route('/contact/About/Team')	
def contact_team():
	
	return render_template('team.html')
	
@app.route('/contact/About/Aims')	
def contact_aim():
	
	return render_template('about.html')
	


	
	
@app.route('/contact/Send Message')	
def contactphp():
	 
	 return render_template('contact_submit.html')
	


#linking serenity with index	
@app.route('/Serenity')	
def ser_home():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/contact/Serenity')	
def ser_contact():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)

@app.route('/blog/Serenity')	
def ser_blog():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)

@app.route('/services/Serenity')	
def ser_services():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/About/Team/Covid-19 Project')	
def topic_link():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)	
	
@app.route('/About/Team/Aims/Covid-19 Project')	
def topic_linkaim():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)

	
#linking the team page with others
@app.route('/About/Team/')
def homet():
	
	return render_template('team.html')
	
@app.route('/About/Team/Home')
def servicest():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/About/Team/FAQ')	
def blogt():
	
	return render_template('FAQ.html')
	
@app.route('/About/Team/Services')	
def homeselft():
	
	return render_template('services.html')
	
@app.route('/About/Team/Contact')	
def home_teamt():
	
	return render_template('contact.html')
	
@app.route('/About/Team/Aims')	
def aim_teamt():
	
	return render_template('about.html')
	

	
#Linking the FAQ page with another:
@app.route('/FAQ/')
def FAQ():
	
	return render_template('FAQ.html')

app.route('/FAQ/contact')
def FAQc():
	
	return render_template('contact.html')
	
	
@app.route('/FAQ/services')	
def FAQs():
	
	return render_template('services.html')
	
@app.route('/FAQ/home')	
def FAQh():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/FAQ/About/Team')	
def FAQt():
	
	return render_template('team.html')

@app.route('/FAQ/About/Aims')	
def FAQaim():
	
	return render_template('about.html')		
	



#Linking chatbot with website
@app.route("/FAQ/Send")
def index():
    return render_template("FAQ.html")
	
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
	
#Linking Aims path with others
@app.route('/About/Aims/')
def aim_self():
	
	return render_template('about.html')
	
@app.route('/About/Aims/Home')
def aim_servicest():
	url = "https://www.worldometers.info/coronavirus/"
	data = requests.get(url) 
	soup = BS(data.text, 'html.parser') 
	total = soup.find("div", class_ = "maincounter-number").text
	total = total[1 : len(total) - 2]
	other = soup.find_all("span", class_ = "number-table")
	recovered = other[2].text 
	deaths = other[3].text 
	deaths = deaths[1:] 
	critical = other[1].text
	return render_template("index.html",total=total, recovered=recovered, deaths=deaths, critical=critical)
	
@app.route('/About/Aims/FAQ')	
def aim_blogt():
	
	return render_template('FAQ.html')
	
@app.route('/About/Aims/Services')	
def aim_homeselft():
	
	return render_template('services.html')
	
@app.route('/About/Aims/Contact')	
def aim_home_teamt():
	
	return render_template('contact.html')
	
@app.route('/About/Aims/team')	
def aim_team():
	
	return render_template('team.html')
	


		
	









	
if __name__== "__main__":
	app.run(debug=True)
 

 