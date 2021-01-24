# import psycopg2 
# import requests
# import json
# from settings import get_secret

# def get_data(DB):
#     source = psycopg2.connect(DB)
#     cursor = source.cursor()
#     url = 'https://geo.api.gouv.fr/departements'
#     req = requests.get(url)
#     depts = req.json()
#     # for region in regions:
#     for dept in depts:
#         sql = """INSERT INTO Department (department_name, department_code, region_id) VALUES (%s,%s,%s)"""
#         value = (dept['nom'], dept['code'], dept['codeRegion'])
#         cursor.execute(sql,value)
#         source.commit()
#     cursor.close()
#     source.close()
#     print("La connexion PostgreSQL est fermée")

# DB = ("dbname= postgres user= postgres,
#        password= get_secret('DB_PASSWORD'),
#        host= ale-pyt-2006-pjt-p3-hamony-db.pythonrover.wilders.dev ,
#        port = 15004")

# get_data(DB)

# This function was only used to automatically add the department informations into the database.
# It's still here with the only purpose of showing the process.
# But due to the security breach it would occur by letting the DB infos exposed. This file would be normally deleted.
