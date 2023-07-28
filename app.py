from flask import Flask, request
import controller as dynamodb



app = Flask(__name__)



@app.route('/')
def root_route():
    try:
        dynamodb.create_table_reception_desk()
        return 'Table created'
    except Exception as e:
        df = {
            "Error_Message" : "Something went wrong while creating the Table by root_route()",
            "Error" : e.args[0]
        }
        return df
        

@app.route('/room_booking', methods=['POST'])
def add_receipt():
    try:
        data = request.get_json()
        response = dynamodb.write_to_record_table(data['recept_id'], data['Date'], data['Number_of_members'], data['Name_of_members'], data['Id_type'], data['ID'], data['Room_No'], data['Check_in_time'], data['Check_out_time'], data['Total_amount'], data['Payment_method'], data['Payment_id'])   
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            return {
                'msg': 'Room Booked successfully',
            }
    except Exception as e:
        df = {
            "Error_Message" : "Something went wrong while Booking a Room in add_receipt()",
            "Error" : e.args[0]
        }
        return df
    
        


@app.route('/get_detail_by_recept_id/<int:recept_id>', methods=['GET'])
def get_details_from_record_table(recept_id):
    try:
        response = dynamodb.read_from_record_table(recept_id)
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            if ('Item' in response):
                return { 'Item': response['Item'] }
            return { 'msg' : 'Item not found!' }
    except Exception as e:
        df = {
            "Error_Message" : "Something went wrong while fetching information by receipt_id from the record_table",
            "Error" : e.args[0]
        }
        return df
    
    


@app.route('/delete_record/<int:recept_id>', methods=['DELETE'])
def delete_from_record_table(recept_id):
    try:
        response = dynamodb.delete_from_record_table(recept_id)
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            return {
                'msg': 'Delete successful',
            }
    except Exception as e:
        df = {
            "Error_Message" : "Something went wrong while deleting record by delete_from_record_table()",
            "Error" : e.args[0]
        }
        return df    
    
    
    

@app.route('/update_record/<int:recept_id>', methods=['PUT'])
def update_record(recept_id):
    try:
        data = request.get_json()
        response = dynamodb.update_in_record_table(recept_id, data)
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            return {
                'msg'                : 'update successful',
                'response'           : response['ResponseMetadata'],
                'ModifiedAttributes' : response['Attributes']
            }
    except Exception as e:
        df = {
            "Error_Message" : "Something went wrong while updating record by update_record()",
            "Error" : e.args[0]
        }
        return df 