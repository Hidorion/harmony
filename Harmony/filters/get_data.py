
import requests
import psycopg2

    

def get_data(DB):
    source = psycopg2.connect(DB)
    cur = source.cursor()
    url = 'https://geo.api.gouv.fr/regions' 
    r = requests.get(url)
    regions = r.json()
    for region in regions:
        sql = """INSERT INTO Region (region_name, region_code, country_id) VALUES (%s,%s,%s)"""
        value = (region['nom'], region['code'], 2)
        cur.execute(sql,value)
        source.commit()
        count = cur.rowcount
        print (count)
    cur.close()
    source.close()
    print("La connexion PostgreSQL est fermée")

DB = ("dbname= postgres user= postgres password= AdminP3Harm host= ale-pyt-2006-pjt-p3-hamony-db.pythonrover.wilders.dev port = 15004")

get_data(DB)

