# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

@app.route('/api/get_data', methods=['GET'])
def get_example():
    try:
        # You can create or fetch data here
        data = {
            "message": "Hello, GET!",
            "status": "success"
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"})
    
#post api
@app.route('/api/post/data', methods=['POST'])
def post_data():
    try:
        #post data
        data = {
            
        }
        return jsonify({"status": True,
                        "message": "Done"
                        })
    except Exception as e:
        return jsonify({"status": False,
                        "message": "not done",
                        "err":str(e)
                        })
            
if __name__ == '__main__':
    app.run(debug=True)