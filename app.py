from flask import Flask, render_template
from mixpanel import Mixpanel
import sys
import pymysql
import re
import datetime

mp = Mixpanel('070da64a2853ffff2ca9a4b1e77ffd0f')

mp.track('gyunseul9', 'Sent Message')
mp.track('gyunseul9', 'Plan Upgraded', {
    'Old Plan': 'Business',
    'New Plan': 'Premium'
})

app = Flask(__name__)

@app.route('/')
def main():
	
    host = 'localhost'
    user = 'gyunseul9'
    password = 'gyunseul9'
    db = 'gyunseul9'

    try:
        conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
    except Exception as e:
        with open('/workspace/gyunseul9/error.log', 'a') as file:
            file.write('{} YOU GOT AN ERROR: {}\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(e)))

    curs = conn.cursor()
    sql = 'select * from status_log'
    curs.execute(sql)
    data = curs.fetchall()
    conn.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
	app.run('0.0.0.0',80,debug=True)
