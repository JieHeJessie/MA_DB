import openpyxl
import MySQLdb
from datetime import date, datetime
import decimal
from openpyxl.formula import Tokenizer
import MySQLdb as mdb
book = openpyxl.load_workbook("MA 16-17 1st Qtr TEST.xlsx", data_only=True)
sheet = book.get_sheet_by_name('Data 16-17')

database = MySQLdb.connect(host="localhost", user="root", passwd="wang123Q", db="ma_newdb")
cursor = database.cursor()

for row in range(2, 60):
    node = sheet['A' + str(row)].value
    pro_date = sheet['B' + str(row)].value
    project_name = sheet['C' + str(row)].value
    service = sheet['D' + str(row)].value
    instrument = sheet['E' + str(row)].value
    person = sheet['F' + str(row)].value
    organization = sheet['G' + str(row)].value
    num_sample = sheet['H' + str(row)].internal_value
    category = sheet['I' + str(row)].value
    int_ext = sheet['J' + str(row)].value
    state = sheet['K' + str(row)].value
    country = sheet['L' + str(row)].value
    user_define1 = sheet['M' + str(row)].value
    user_define2 = sheet['N' + str(row)].value
    subtotal = sheet['O' + str(row)].value
    cus_count = sheet['P' + str(row)].value

    # if pro_date=='Half year' or pro_date is 'Full year':
    # pro_date = date.today().isoformat()
    if isinstance(pro_date, date):
        pro_date = pro_date.isoformat()
    else:
        pro_date = date.today().isoformat()
    if project_name is None:
        project_name='null'
    if person is None:
        person = 'Null'
    if organization is None:
        organization = "Null"
    if cus_count is None:
        cus_count = "0"
    if user_define2 is not None:
        user_define2 = user_define2.upper()
    else:
        user_define2 = "NULL"
    if not isinstance(num_sample, int):
        num_sample = 0

    if subtotal is None:
        subtotal = 0.00
    else:
        subtotal = decimal.Decimal("%.2f" % subtotal)

    field_check = user_define2.split(';')
    if len(field_check) == 1:
        query = """INSERT INTO migration_db_project (node, pro_date,project_name,service,instrument,person,organization,num_sample,category,int_ext,state,country,user_define1,user_define2,subtotal,cus_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (
        node, pro_date, project_name, service, instrument, person, organization, num_sample, category, int_ext, state,
        country, user_define1, user_define2, subtotal, cus_count)
        cursor.execute(query, values)
        database.commit()
    else:
        for each in field_check:
            query = """INSERT INTO migration_db_project (node,pro_date,project_name,service,instrument,person,organization,num_sample,category,int_ext,state,country,user_define1,user_define2,subtotal,cus_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values = (
            node, pro_date, project_name, service, instrument, person, organization, num_sample, category, int_ext,
            state, country, user_define1, each, subtotal, cus_count)
            cursor.execute(query, values)
            # database.commit()

cursor.close()

database.close()

print ("Importion Done.")



