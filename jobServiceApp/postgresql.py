import psycopg2

#CURRENT CONNECTION : APP-QUART-THESIS
HOST='ec2-18-209-153-180.compute-1.amazonaws.com'
DBNAME='d7g3gjmh2qj1n9'
USER='nvnxtxwgcechxk'
PASSWORD='80b6ad7fe020da46a66ff63b15148cfa3f1719f7ab1ab42050d7c58a862488eb'
PORT='5432'


def getQuery(query):
    
    conn = psycopg2.connect(host=HOST,dbname=DBNAME, user=USER, password=PASSWORD,sslmode='require')
    cursor = conn.cursor()
    cursor.execute(query)
    lsResult = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return lsResult

def executeNonQuery(query):
    conn = psycopg2.connect(host=HOST,dbname=DBNAME, user=USER, password=PASSWORD,sslmode='require')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return True
   





