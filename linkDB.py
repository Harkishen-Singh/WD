from main_part import Core_Base
from pymongo import MongoClient
import datetime
time = datetime.datetime.now()
objArr = []

url = 'mongodb+srv://harkishen:Bbsr131@cluster0-zmd3i.mongodb.net/Weather_record_tests?retryWrites=true'
#url = 'mongodb://127.0.0.1:27017'
client = MongoClient(url)
DBname = 'Weather_record_tests'
db = client[DBname]
previous_collections = []
collName = 'rec__'+ str(time)[:10]
collName = collName.replace('-','_')
coll = db[collName]


class Links_to_Database(Core_Base):

    def __init__(self):
        pass


    def object_creation_apending(self):
        object = {
            "place" : self.place,
            "state" : self.stateSp,
            "city" : self.citySp,
            "date" : str(time)[:10],
            "time_now" : str(time)[11:],
            "temperature_that_moment" : self.temperature,
            "max_temperature" : self.max_temp,
            "min_temperature" : self.min_temp,
            "avg_temperature" : self.avg_temp,
            "max_probability_rainfall" : self.max_rain_probability,
            "min_probability_rainfall" : self.min_rain_probability,
            "avg_rainfall" : self.avg_rain,
            "humidity": self.humidity,
            "feels_like_that_moment" : self.feel,
            "dew_point" : self.dew_point,
            "visibility" : self.visibility,
            "hourly_forecast" : self.var,
            "rain_array_starting_from_time_now" : self.rains,
            "temp_array_starting_from_time_now" : self.temps,
        }
        objArr.append(object)


cityObject_OD = ['Angul',
'Boudh',
'Bargarh',
'Balasore',
'balangir',
'Bhadrak',
'Cuttack',
'Debagarh',
'Dhenkanal',
'Ganjam',
'Gajapati',
'Jharsuguda',
'Jaipur',
'Jagatsinghpur',
'Khordha',
'Kendujhar',
'Kalahandi',
'Kandhamala',
'koraput',
'Kendrapara',
'Malkanagir',
'Mayurbhanj',
'Nabarangpur',
'Nuapada',
'Nayagarh',
'Puri',
'Rayagada',
'Sambalpur',
'Subarnapur',
'Sundergarh',
'Bhubaneswar',
'Jatni',
'Chilika',
]



cityObject_Puducherry =['Karaikal','Mahe','Pondicherry','Yanam']

cityObject_Punjab =['Amritsar','Chandigarh','Barnala','Bathinda','Firozpur','Faridkot','FatehgarhSahib','Fazilka','Gurdaspur','Hoshiarpur','Jalandhar','Kapurt','hala','Ludhiana','Mansa','Moga','SriMuktsarSahib','Pathankot','Patiala','Rupnagar','Ajitgarh','Mohali','Sangrur','Nawanshahr','TarnTaran']

cityObject_Rajasthan= ['Ajmer','Alwar','Bikaner','Barmer','Banswara','Bharatpur','Baran','Bundi','Bhilwara','Churu','Chittorgarh','Dausa','Dholpur','Dungapur','Ganganagar','Hanumangarh','Jhunjhunu','Jalore','Jodhpur','Jaipur','Jaisalmer','Jhalawar','Karauli','Kota','Nagaur','Pali','Pratapgarh','Rajsamand','Sikar','SawaiMadhopur','Sirohi','Tonk','Udaipur']
cityObject_Sikkim =['EastSikkim','NorthSikkim','SouthSikkim','WestSikkim']
cityObject_TamilNadu= ['Ariyalur','Chennai','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kanchipuram','Kanyakumari','Karur','Madurai','Nagapattinam','Nilgiris','Namakkal','Perambalur','Pudukkottai','Ramanathapuram','Salem','Sivaganga','Tirupur','Tiruchirappalli','Theni','Tirunelveli','Thanjavur','Thoothukudi','Tiruvallur','Tiruvarur','Tiruvannamalai','Vellore','Viluppuram','Virudhunagar']
cityObject_Tripura=['Dhalai','NorthTripura','SouthTripura','Khowai','WestTripura']
cityObject_Uttarakhand=['Almora','Bageshwar','Chamoli','Champawat','Dehradun','Haridwar','Nainital','PauriGarhwal','Pithoragarh','Rudraprayag','TehriGarhwal','UdhamSinghNagar','Uttarkashi']


cityObject_WB = ['Birbhum','Bankura','Bardhaman','Darjeeling','DakshinDinajpur',
'Hooghly','Howrah','Jalpaiguri','CoochBehar','Kolkata','Maldah','PaschimMedinipur',
'PurbaMedinipur','Murshidabad','Nadia','North24Parganas','South24Parganas',
'Purulia','UttarDinajpur' ]
cityObject_UP = ['Agra','Allahabad','Aligarh','AmbedkarNagar','Auraiya','Azamgarh','Barabanki','Budaun',
'Bagpat','Bahraich','Bijnor','Ballia','Banda','Balrampur','Bareilly','Basti','Bulandshahr','Chandauli',
'ChhatrapatiShahujiMaharajNagar','Chitrakoot','Deoria','Etah','KanshiRamNagar','Etawah','Firozabad','Farrukhabad',
'Fatehpur','Faizabad','GautamBuddhNagar','Gonda','Ghazipur','Gorakhpur','Ghaziabad','Hamirpur','Hardoi',
'MahamayaNagar','Jhansi','Jalaun','JyotibaPhuleNagar','Jaunpur','district','RamabaiNagar','KanpurDehat','Kannauj',
'Kanpur','Kaushambi','Kushinagar','Lalitpur','LakhimpurKheri','Lucknow','Mau','Meerut','Maharajganj','Mahoba','Mirzapur',
'Moradabad','Mainpuri','Mathura','Muzaffarnagar','PanchsheelNagar','Hapur','Pilibhit','Shamli',
'Pratapgarh','Rampur','Raebareli','Saharanpur','Sitapur','Shahjahanpur','SantKabirNagar','Siddharthnagar','Sonbhadra','SantRavidasNagar',
'Sultanpur','Shravasti','Unnao','Varanasi']

cityObject_AP =['Anantapur','Chittoor','Kakinada','Guntur','Hyderabad','Karimnagar','Khammam',
'Krishna','Kurnool','Mahbubnagar','Medak','Nalgonda','Nizamabad','Ongole','Hyderabad','Srikakulam','Nellore',
'Visakhapatnam','Vizianagaram','Warangal','Eluru','Kadapa']
cityObject_AruP = ['Anjaw','Changlang','EastSiang','KurungKumey','Lohit','LowerDibangValley','LowerSubansiri',
'PapumPare','Tawang','Tirap','DibangValley','UpperSiang','UpperSubansiri','WestKameng','WestSiang']




cityObject_Bihar=['Araria','Arwal','Aurangabad','Banka','Begusarai','Bhagalpur','Bhojpur','Buxar','Darbhanga','EastChamparan','Gaya','Gopalganj','Jamui','Jehanabad','Kaimur','Katihar','Khagaria','Kishanganj','Lakhisarai','Madhepura','Madhubani','Munger','Muzaffarpur','Nalanda','Nawada','Patna','Purnia','Rohtas','Saharsa','Samastipur','Saran','Sheikhpura','Sheohar','Sitamarhi','Siwan','Supaul','Vaishali','WestChamparan']

cityObject_Chatis=['Bastar','Bijapur','Bilaspur','Dantewada','Dhamtari','Durg','Jashpur','Janjgir-Champa','Korba','Koriya','Kanker',
'Kabirdham','Kawardha','Mahasamund','Narayanpur','Raigarh','Rajnandgaon','Raipur','Surguja']


cityObject_specifics = ['Delhi','Panaji','Margao','Chandigarh']


cityObject_Guj=['Ahmedabad','Amrelidistrict','Anand','Banaskantha','Bharuch','Bhavnagar','Dahod','TheDangs','Gandhinagar','Jamnagar','Junagadh','Kutch','Kheda','Mehsana','Narmada','Navsari','Patan','Panchmahal','Porbandar','Rajkot','Sabarkantha','Surendranagar','Surat','Vyara','Vadodara','Valsad']

cityObject_Haryn=['Ambala','Bhiwani','Faridabad','Fatehabad','Gurgaon','Hissar','Jhajjar','Jind','Karnal','Kaithal','Kurukshetra','Mahendragarh','Mewat','Palwal','Panchkula','Panipat','Rewari','Rohtak','Sirsa','Sonipat','YamunaNagar']

cityObject_HP =['Bilaspur','Chamba','Hamirpur','Kangra','Kinnaur','Kullu','Lahaul','Mandi','Shimla','Sirmaur','Solan','Una']

cityObject_JK=[
'Anantnag','Badgam','Baramula','Doda','Ganderbal','Jammu','Kathua','Kishtwar','Kupwara','Kulgam',
'Poonch','Pulwama','Rajauri','Ramban','Reasi','Samba','Shopian','Srinagar','Udhampur'
]
cityObject_JHK=[
'Bokaro','Chatra','Deoghar','Dhanbad','Dumka','EastSinghbhum','Garhwa','Giridih','Godda','Gumla','Hazaribag','Jamtara',
'Khunti','Koderma','Latehar','Lohardaga','Pakur','Palamu','Ramgarh','Ranchi','Sahibganj','SeraikelaKharsawan','Simdega'
'WestSinghbhum'
]
cityObject_Karnataka=[
'Bagalkot','Bangalore','Belgaum','Bellary','Bidar','Bijapur','Chamarajnagar','Chikkamagaluru',
'Chikkaballapur','Chitradur','ga','Davanagere','Dharwad','DakshinaKannada','Gadag','Gulbarga','Hassan','Haveridistrict',
'Kodagu','Kolar','Koppal','Mandya','Mysore','Raichur','Shimoga','Tumkur','Udupi','UttaraKannada','Ramanagara','Yadgir'
]
cityObject_Kerela=[
'Alappuzha','Ernakulam','Idukki','Kannur','Kasaragod','Kollam','Kottayam','Kozhikode','Malappuram','Palakkad','Pathanamthitta',
'Thrissur','Thiruvananthapuram','Wayanad'
]
cityObject_MadhyaPradesh = [
'Alirajpur','Anuppur','AshokNagar','Balaghat','Barwani','Betul','Bhind','Bhopal','Burhanpur','Chhatarpur','Chhindwara',
'Damoh','Datia','Dewas','Dhar','Dindori','Guna','Gwalior','Harda','Hoshangabad','Indore','Jabalpur','Jhabua','Katni','Khandwa',
'Mandla','Mandsaur','Morena','Narsinghpur','Neemuch','Panna','Rewa','Rajgarh','Ratlam','Raisen','Sagar','Satna','Sehore','Seoni',
'Shahdol','Shajapur','Sheopur','Shivpuri','Sidhi','Singrauli','Tikamgarh','Ujjain','Umaria','Vidisha'
]
cityObject_Maharashtra =[
'Ahmednagar','Akola','Amravati','Aurangabad','Bhandara','Beed','Buldhana','Chandrapur','Dhule','Gadchiroli',
'Gondia','Hingoli','Jalgaon','Jalna','Kolhapur','Latur','Mumbai','Nandurbar','Nanded','Nagpur','Nashik','Osmanabad',
'Parbhani','Pune','Raigad','Ratnagiri','Sindhudurg','Sangli','Solapur','Satara','Thane','Wardha','Washim','Yavatmal'
]
cityObject_Manipur=[
'Bishnupur','Churachandpur','Chandel','ImphalEast','Senapati','Tamenglong','Thoubal','Ukhrul','ImphalWest'
]
cityObject_Meghalaya=[
'EastGaroHills','EastKhasiHills','JaintiaHills','RiBhoi','SouthGaroHills','WestGaroHills','WestKhasiHills'
]
cityObject_Mizoram=[
'Aizawl','Champhai','Kolasib','Lawngtlai','Lunglei','Mamit','Saiha','Serchhip'
]
cityObject_Nagaland=[
'Dimapur','Kohima','Mokokchung','Mon','Phek','Tuensang','Wokha','Zunheboto'
]



state = ['Odisha']

def checks():

        previous_collections = db.collection_names(include_system_collections=False)

        collectionAlreadyAvailable = False
        for jj in previous_collections :

            if collName == jj :
                collectionAlreadyAvailable = True
                print(previous_collections)
                db.drop_collection(jj)

                print('Previous Similar collection found. Deleting it to avoid conflicts. Time : '+str(time))

                print('\n')
        if collectionAlreadyAvailable == False :
            print(previous_collections)
            print('No previous collections found. All Good!')

        x = coll.insert_many(objArr)
        print('\nAdded to database. Name : '+collName)
        print('\ncollections available \n')
        print(previous_collections)


# mongo "mongodb+srv://cluster0-zmd3i.mongodb.net/test" --username harkishen
