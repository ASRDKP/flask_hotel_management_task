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