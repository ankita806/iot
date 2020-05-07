from flask import Flask,redirect,url_for,request
from influxdb import InfluxDBClient
app= Flask(__name__)

@app.route('/weatherstation', methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		wind_count = request.get_json()["wind_count"]
		bucket_count = request.get_json()["bucket_count"]
		direction = request.get_json()["direction"]
		print(wind_count,"\t",bucket_count,"\t",direction)
		client= InfluxDBClient( host = 'localhost', port = 8086)
		client.create_database( "weatherstation1" )
		#json_body = [{ "measurement": "cpu","fields": {"wind_count":wind_count}}]
		json_body = [{ "measurement": "cpu","tags":{"direction":direction,},"fields": {"wind_count":wind_count,"bucket_count":bucket_count}}]
		client.write_points(json_body, database='weatherstation1')
		return ("POST successful") 
	elif request.method == 'GET':
		user = request.args.get('nm') 
		print(user)
		
if __name__ == '__main__': 
        app.run(host='0.0.0.0',debug = True) 
