from boto3 import resource
import config



AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
REGION_NAME = config.REGION_NAME
 
 
 
resource = resource(
   'dynamodb',
   aws_access_key_id     = AWS_ACCESS_KEY_ID,
   aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
   region_name           = REGION_NAME
)



def create_table_reception_desk():   
   table = resource.create_table(
       TableName = 'Hotel_Management', # Name of the table
       KeySchema = [
           {
               'AttributeName': 'recept_id',
               'KeyType'      : 'HASH' #RANGE = sort key, HASH = partition key
           }
       ],
       AttributeDefinitions = [
           {
               'AttributeName': 'recept_id', # Name of the attribute
               'AttributeType': 'N'   # N = Number (B= Binary, S = String)
           }
       ],
       ProvisionedThroughput={
           'ReadCapacityUnits'  : 10,
           'WriteCapacityUnits': 10
       }
   )
   return table


Hotel_Management = resource.Table('Hotel_Management')




def write_to_record_table(recept_id, Date, Number_of_members, Name_of_members, Id_type, ID, Room_No, Check_in_time, Check_out_time, Total_amount, Payment_method, Payment_id):
    try:
        response = Hotel_Management.put_item(
            Item = {
                'recept_id'     : recept_id,
                'Date'  : Date,
                'Number_of_members' : Number_of_members,
                'Name_of_members'  : Name_of_members,
                'Id_type' : Id_type,
                'ID' : ID,
                'Room_No' : Room_No,
                'Check_in_time' :Check_in_time,
                'Check_out_time' : Check_out_time,
                'Total_amount' : Total_amount,
                'Payment_method' : Payment_method,
                'Payment_id' : Payment_id
            }
        )
        return response
    except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in controller.write_to_record_table()",
                "Error" : e.args[0]
            }
            return df

        
        
def read_from_record_table(recept_id):
    try:
        response = Hotel_Management.get_item(
            Key = {
                'recept_id'     : recept_id
            },
            AttributesToGet = [
                'recept_id', 'Date', 'Number_of_members', 'Name_of_members', 'Id_type', 'ID', 'Room_No', 'Check_in_time', 'Check_out_time', 'Total_amount', 'Payment_method', 'Payment_id'
        ])
        return response
    except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in controller.read_from_record_table()",
                "Error" : e.args[0]
            }
            return df
        
        

def delete_from_record_table(recept_id):
    response = Hotel_Management.delete_item(
        Key = {
            'recept_id': recept_id
        }
    )
    return response




def update_in_record_table(recept_id, data:dict):
    response = Hotel_Management.update_item(
        Key = {
            'recept_id': recept_id
        },
        AttributeUpdates={
            'Date': {
                'Value'  : data['Date'],
                'Action' : 'PUT' 
            },
            'Number_of_members': {
                'Value'  : data['Number_of_members'],
                'Action' : 'PUT'
            },
            'Name_of_members': {
                'Value'  : data['Name_of_members'],
                'Action' : 'PUT'
            },
            'Id_type': {
                'Value'  : data['Id_type'],
                'Action' : 'PUT'
            },
            'ID': {
                'Value'  : data['ID'],
                'Action' : 'PUT'
            },
            'Room_No': {
                'Value'  : data['Room_No'],
                'Action' : 'PUT'
            },
            'Check_in_time': {
                'Value'  : data['Check_in_time'],
                'Action' : 'PUT'
            },
            'Check_out_time': {
                'Value'  : data['Check_out_time'],
                'Action' : 'PUT'
            },
            'Total_amount': {
                'Value'  : data['Total_amount'],
                'Action' : 'PUT'
            },
            'Payment_method': {
                'Value'  : data['Payment_method'],
                'Action' : 'PUT'
            },
            'Payment_id': {
                'Value'  : data['Payment_id'],
                'Action' : 'PUT'
            }
        },
        ReturnValues = "UPDATED_NEW"  # returns the new updated values
    )    
    return response
