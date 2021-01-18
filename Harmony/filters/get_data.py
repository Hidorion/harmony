# import psycopg2 
# import requests


# def get_data(DB):
#     source = psycopg2.connect(DB)
#     cursor = source.cursor()
# #     url = 'https://geo.api.gouv.fr/regions'
#     url = 'https://geo.api.gouv.fr/departements'
#     req = requests.get(url)
# #     regions = req.json()
#     depts = req.json()
#     # for region in regions:
#     for dept in depts:
# #         sql = """INSERT INTO Region (region_name, region_code, country_id) VALUES (%s,%s,%s)"""
# #         value = (region['nom'], region['code'], 2)
#         sql = """INSERT INTO Department (department_name, department_code, region_id) VALUES (%s,%s,%s)"""
#         value = (dept['nom'], dept['code'], dept['codeRegion'])
#         cursor.execute(sql,value)
#         source.commit()
# #         count = cur.rowcount
# #         print (count)
#     cursor.close()
#     source.close()
#     print("La connexion PostgreSQL est fermée")

# DB = ("dbname= postgres user= postgres password= AdminP3Harm host= ale-pyt-2006-pjt-p3-hamony-db.pythonrover.wilders.dev port = 15004")

# get_data(DB)

# This function was only used to automatically add the region informations into the database. It's still here with the only purpose of showing the process.
# But due to the security breach it would occur by letting the DB infos exposed. This file would be normally deleted.
