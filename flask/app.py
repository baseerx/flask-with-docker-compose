from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database configuration
DATABASE = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

@app.route('/')
def get_data_from_db():
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()

    # Example query to fetch data from a table
    cur.execute("SELECT name FROM cities")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return data

@app.route('/cities')
def cities():
    #join cities and provices on province_id
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT cities.name as city_name, provinces.name as province_name FROM cities JOIN provinces ON cities.province_id = provinces.id")
    data = cur.fetchall()
    cur.close()
    return data

#get data from cities by passing province_id
@app.route('/cities/<int:province_id>')
def cities_by_province(province_id):
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT name FROM cities WHERE province_id = %s", (province_id,))
    data = cur.fetchall()
    cur.close()
    return data

#return all cities 
@app.route('/cities/all')
def cities_all():
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT name FROM cities")
    data = cur.fetchall()
    cur.close()
    return data

#return all provinces
@app.route('/provinces')
def provinces():
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT name FROM provinces")
    data = cur.fetchall()
    cur.close()
    return data

if __name__ == '__main__':
    app.run(debug=True)
