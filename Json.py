import pymysql
from db_config import mysql
from app import app
from flask import jsonify


@app.route('/states')
def users():
    result={}
    try:
        conn=mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM location")
        rows = cursor.fetchall()
        #dict_val={}
        for row in rows:
            state = row['state']

            state_data={
                'Id':row['id'],
                'District':row['district'],
                'Pincode':row['pincode']
            }


            if(state not in result):
                list = []
            else:
                list = result[state]

            list.append(state_data)
            result[state] = list

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


    res_list = []

    for key in result:
        state_data = { 
            'state' : key,
            'districts' : result[key]
        }
        res_list.append(state_data)
    
    result_data = {'data' : res_list}

    return jsonify(result_data)

if __name__ == "__main__":
    app.run()







