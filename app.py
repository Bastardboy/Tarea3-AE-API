from flask import Flask, request, jsonify
from Models import Admin, Company, Location, Sensor, SensorData, db
from init import create_app
import time

app= create_app()

@app.route('/admin', methods=['POST'])
def validate_admin():
    if request.method == 'POST':
        data= request.get_json()
        username= data['username']
        password= data['password']
        admin = Admin.query.filter_by(Username=username, Password=password).first()
        if admin is None:
            return jsonify({'message': 'Username not found'})
        if admin:
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Invalid password'})

@app.route('/api/addcompany', methods=['POST'])
def addcompany():
    data = request.get_json()
    company_name = data['company_name']
    company_api_key = data['company_api_key']
    user= data['username']
    password= data['password']

    admin= Admin.query.filter_by(Username=user, Password=password).first()
    
    if admin:
        company = Company.query.filter_by(company_name=company_name).first()
        if company:
            return jsonify({
                'status': 'fail',
                'message': 'Company already exists.'
            })
        else:   
            # console log
            print(company_name, company_api_key)
            company = Company(company_name=company_name, company_api_key=company_api_key)

            db.session.add(company)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Registered successfully.',
                'token': company.generate_token()
            })

@app.route('/api/addlocation', methods=['POST'])
def addlocation():
    data = request.get_json()
    company_id = data['company_id']
    location_name = data['location_name']
    location_country= data['location_country']
    location_city = data['location_city']
    location_meta = data['location_meta']
    user= data['user']
    password= data['password']
    
    admin= Admin.query.filter_by(Username=user, Password=password).first()
    
    if admin:
        location = Location.query.filter_by(location_name=location_name).first()
        if location:
            return jsonify({
                'status': 'fail',
                'message': 'Location already exists.'
            })
        else:   
            # console log
            print(company_id, location_name, location_country, location_city, location_meta)
            location = Location(company_id=company_id, location_name=location_name, location_country=location_country, location_city=location_city, location_meta=location_meta)
            location.save()
            return jsonify({
                'status': 'success',
                'message': 'Registered successfully.',
                'token': location.generate_token()
            })

@app.route('/api/addsensor', methods=['POST'])
def addsensor():
    data = request.get_json()
    location_id = data['location_id']
    sensor_name= data['sensor_name']
    sensor_category = data['sensor_category']
    sensor_meta = data['sensor_meta']
    sensor_api_key= data['sensor_api_key']
    user= data['user']
    password= data['password']
    
    admin= Admin.query.filter_by(Username=user, Password=password).first()    
    
    if admin: 
        # console log
        print(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
        sensor = Sensor(location_id=location_id, sensor_name=sensor_name, sensor_category=sensor_category, sensor_meta=sensor_meta, sensor_api_key=sensor_api_key)
        sensor.save()
        return jsonify({
            'status': 'success',
            'message': 'Registered successfully.',
            'token': sensor.generate_token()
        })

@app.route('/api/getlocations/<company_api_key>', methods=['GET'])
def getlocations(company_api_key):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        locations = Location.query.filter_by(company_id=company.ID).all()
        return jsonify({
            'status': 'success',
            'locations': [location.to_json() for location in locations]
        })
    else:
        return jsonify({
            'status': 'fail',
            'message': 'Company not found.'
        })

@app.route('/api/getlocation/<company_api_key>/<location_id>', methods=['GET'])
def getlocation(company_api_key, location_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    print(company_api_key, location_id)
    if company:
        location = Location.query.filter_by(ID=location_id).first()
        return jsonify({
            'status': 'success',
            'location': location.to_json()
        })
    else:
        return jsonify({
            'status': 'fail',
            'message': 'Company not found.'
        })



@app.route('/api/getsensors/<company_api_key>/<location_id>', methods=['GET'])
def getsensors(company_api_key, location_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensors = Sensor.query.filter_by(location_id=location_id).all()
        return jsonify({
            'status': 'success',
            'sensors': [sensor.to_json() for sensor in sensors]
        })
    else:
        return jsonify({
            'status': 'fail',
            'message': 'Company not found.'
        })


@app.route('/api/getsensor/<company_api_key>/<sensor_id>', methods=['GET'])
def getsensor(company_api_key, sensor_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        return jsonify({
            'status': 'success',
            'sensor': sensor.to_json()
        })
    else:
        return jsonify({
            'status': 'fail',
            'message': 'Company not found.'
        })


@app.route('/api/updatelocation', methods=['PUT'])
def updatelocation():
    data = request.get_json()
    location_id = data['location_id']
    company_api_key = data['company_api_key']
    location_name = data['location_name']
    location_country = data['location_country']
    location_city = data['location_city']
    location_meta = data['location_meta']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        location = Location.query.filter_by(ID=location_id).first()
        if location:
            location.location_name = location_name
            location.location_country = location_country
            location.location_city = location_city
            location.location_meta = location_meta
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Location updated successfully.'
            })
        else:
            return jsonify({
                'status': 'fail',
                'message': 'Location not found.'
            })
    else:
        return jsonify({
            'status': 'fail',
            'message': 'Company not found.'
        })

@app.route('/api/updatesensor', methods=['PUT'])
def updatesensor():
    data = request.get_json()
    sensor_id = data['sensor_id']
    company_api_key = data['company_api_key']
    sensor_name = data['sensor_name']
    sensor_category = data['sensor_category']
    sensor_meta = data['sensor_meta']
    sensor_api_key = data['sensor_api_key']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        if sensor:
            sensor.sensor_name = sensor_name
            sensor.sensor_category = sensor_category
            sensor.sensor_meta = sensor_meta
            sensor.sensor_api_key = sensor_api_key
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Sensor updated successfully.'
            })
        else:
            return jsonify({
                'status': 'fail',
                'message': 'Sensor not found.'
            })
    else:
        return jsonify({
            'status': 'fail',
            'message': 'Company not found.'
        })

@app.route('/api/deletelocation', methods=['DELETE'])
def deletelocation():
    data = request.get_json()
    location_id = data['location_id']
    company_api_key = data['company_api_key']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        location = Location.query.filter_by(ID=location_id).first()
        if location:
            db.session.delete(location)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Location deleted successfully.'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Location not found.'
            })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Company not found.'
        })

@app.route('/api/deletesensor', methods=['DELETE'])
def deletesensor():
    data = request.get_json()
    sensor_id = data['sensor_id']
    company_api_key = data['company_api_key']

    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
        if sensor:
            db.session.delete(sensor)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Sensor deleted successfully.'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Sensor not found.'
            })

@app.route('/api/sensordata', methods=['POST'])
def sensordata():
    data = request.get_json()
    sensor_api_key = data['sensor_api_key']
    sensor_data = data['sensor_data']

    sensor = Sensor.query.filter_by(sensor_api_key=sensor_api_key).first()
    if sensor:
        date=time.time()
        date= int(date)
        sensor_data = SensorData(sensor_id=sensor.sensor_id, data=sensor_data, date=date)
        sensor_data.save()
        return jsonify({
            'status': 'success',
            'message': 'Sensor data inserted successfully.'
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Sensor not found.'
        })

@app.route('/api/getsensordata/<company_api_key>/from/<time1>/to/<time2>/<sensor_id>/', methods=['GET'])
def getsensordata(company_api_key, time1, time2, sensor_id):
    company = Company.query.filter_by(company_api_key=company_api_key).first()
    if company:
        data=[]
        for sensor in sensor_id.split(','):
            sensor = Sensor.query.filter_by(sensor_id=sensor).first()
            if sensor:
                sensordata = SensorData.query.filter_by(sensor_id=sensor.sensor_id).all()
                for i in sensordata:
                    if i.date>=int(time1) and i.date<=int(time2):
                        data.append(i.to_json())
        return jsonify({
            'status': 'success',
            'data': data
        })

    else:
        return jsonify({
            'status': 'error',
            'message': 'Company not found.'
        })

@app.route('/api/updatesensordata', methods=['PUT'])
def updatesensordata():
    data = request.get_json()
    sensor_api_key = data['sensor_api_key']
    sensor_data = data['sensor_data']
    sensor_data_id = data['sensor_data_id']

    sensor = Sensor.query.filter_by(sensor_api_key=sensor_api_key).first()
    if sensor:
        sensordata = SensorData.query.filter_by(sensor_data_id=sensor_data_id).first()
        if sensordata:
            sensordata.data = sensor_data
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Sensor data updated successfully.'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Sensor data not found.'
            })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Sensor not found.'
        })

@app.route('/api/deletesensordata', methods=['DELETE'])
def deletesensordata():
    data = request.get_json()
    sensor_api_key = data['sensor_api_key']
    sensor_data_id = data['sensor_data_id']

    sensor = Sensor.query.filter_by(sensor_api_key=sensor_api_key).first()
    if sensor:
        sensordata = SensorData.query.filter_by(sensor_data_id=sensor_data_id).first()
        if sensordata:
            db.session.delete(sensordata)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Sensor data deleted successfully.'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Sensor data not found.'
            })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Sensor not found.'
        })

        
app.run()