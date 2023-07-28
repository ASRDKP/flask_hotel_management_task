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