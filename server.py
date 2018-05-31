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
	 cities_UP=cityObject_UP,
	 cities_AP=cityObject_AP,
	 cities_Bihar=cityObject_Bihar,
	 cities_Chatis=cityObject_Chatis,
	 cities_Guj=cityObject_Guj,
	 cities_Haryn=cityObject_Haryn,
	 cities_HP=cityObject_HP,
	 cities_Karnataka=cityObject_Karnataka,
	 cities_JK=cityObject_JK,
	 cities_Kerela=cityObject_Kerela,
	 cities_AruP=cityObject_AruP,
	 cities_Maharashtra=cityObject_Maharashtra,
	 cities_Manipur=cityObject_Manipur,
	 cities_Punjab=cityObject_Punjab,
	 cities_Rajasthan=cityObject_Rajasthan,
	 cities_Sikkim=cityObject_Sikkim,
	 cities_Nagaland=cityObject_Nagaland,
	 cities_Tripura=cityObject_Tripura,
	 cities_Uttarakhand=cityObject_Uttarakhand,
	 cities_TamilNadu=cityObject_TamilNadu,
	 cities_Puducherry=cityObject_Puducherry,
	 cities_JHK=cityObject_JHK,
	 cities_MadhyaPradesh=cityObject_MadhyaPradesh,
	 cities_Meghalaya=cityObject_Meghalaya,cities_Mizoram=cityObject_Mizoram,
	 cities_specifics = cityObject_specifics,
	 )

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

			i = 'WestBengal'
			for j in cityObject_WB :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'UttarPradesh'
			for j in cityObject_UP :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'AndhraPradesh'
			for j in cityObject_AP :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'ArunachalPradesh'
			for j in cityObject_AruP :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Bihar'
			for j in cityObject_Bihar :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Chattisgrah'
			for j in cityObject_Chatis :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Gujarat'
			for j in cityObject_Guj :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Haryana'
			for j in cityObject_Haryn :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()


			i = 'HimachalPradesh'
			for j in cityObject_HP :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'JammuKashmir'
			for j in cityObject_JK :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Karnataka'
			for j in cityObject_Karnataka :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Kerela'
			for j in cityObject_Kerela :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'MadhyaPradesh'
			for j in cityObject_MadhyaPradesh :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Maharashtra'
			for j in cityObject_Maharashtra :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Manipur'
			for j in cityObject_Manipur :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Meghalaya'
			for j in cityObject_Meghalaya :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Mizoram'
			for j in cityObject_Mizoram :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()


			i = 'Nagaland'
			for j in cityObject_Nagaland :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Punjab'
			for j in cityObject_Punjab :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Rajasthan'
			for j in cityObject_Rajasthan :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Sikkim'
			for j in cityObject_Sikkim :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Tripura'
			for j in cityObject_Tripura :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Uttarakhand'
			for j in cityObject_Uttarakhand :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'TamilNadu'
			for j in cityObject_TamilNadu :

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()
			i = 'Puducherry'
			for j in cityObject_Puducherry:

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = 'Jharkhand'
			for j in cityObject_JHK:

			    obj.asking(j,i)
			    obj.further_info()
			    obj.displaying()
			    obj.object_creation_apending()

			i = ''
			for j in cityObject_specifics:

				if j =='Panaji' or j == 'Margao':
					i = 'GA'
				else :
					i=''
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
