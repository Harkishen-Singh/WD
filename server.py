from flask import Flask,request, render_template, url_for
import os
from linkDB import *

app = Flask(__name__)

from views import *
port = int(os.environ.get("PORT", 5000))

# home page
#app.add_url_rule('/', 'homePage', home)
@app.route('/')
def home():
	print('Home page request  ')
	return render_template('index.html', cities_OD=cityObject_OD,
	 cities_WB=cityObject_WB,
	 cities_UP=cityObject_UP)

# for starting the weather app
#app.add_url_rule('/startWeatherProcess', methods=['post'], 'startApp', startApp)

@app.route('/startWeatherProcess', methods=['GET','POST'])
def startApp():
	if request.method == 'POST' :
		user = request.form['name']
		key = request.form['password']
		if (user == 'harkishen' or user == 'harkishen singh' or user == 'pratik' or user=='pratik srichandan') and \
		key == 'socialyticsCompany' :

			print('User authunticated as ' + user)

			print('User '+user+' Requested to start the Application')
			obj = Links_to_Database()
			i = 'Odisha'
			for j in cityObject_OD :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'West_Bengal'
			for j in cityObject_WB :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			print('\n\n\n\nSuper array of all weathers...\n\n')
			print(objArr)
			print('\nperforming all checks...\n')
			
			i = 'Uttar_Pradesh'
			for j in cityObject_UP :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			print('\n\n\n\nSuper array of all weathers...\n\n')
			print(objArr)
			print('\nperforming all checks...\n')
			checks()

			return '<h3>Your Web Weather Application has been Completed Successfully. All Good.!<br/>Registered User : '+user+' </h3>'
		else :
			return '<h3 style="color:red;">User Authuntication Failed.! Inputed User : '+user+'</h3>'


if __name__ == '__main__' :
	app.debug = True
	app.run(host = '0.0.0.0', port = port)
