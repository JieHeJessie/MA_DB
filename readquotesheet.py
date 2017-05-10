import openpyxl
import MySQLdb
from datetime import date, datetime
import decimal
from openpyxl.formula import Tokenizer
import MySQLdb as mdb

book = openpyxl.load_workbook("Quote Numbering.xlsx", data_only=True)
sheet = book.get_sheet_by_name('2016-17')

database = MySQLdb.connect(host="localhost", user="root", passwd="wang123Q", db="ma_newdb")
cursor = database.cursor()

for row in range(3, 39):
    quote_num = sheet['A' + str(row)].value
    quote_year = sheet['B' + str(row)].value
    version = sheet['C' + str(row)].value
    concatenate = sheet['D' + str(row)].value
    client = sheet['E' + str(row)].value
    company = sheet['F' + str(row)].value
    quote_staff = sheet['G' + str(row)].internal_value
    quote_date = sheet['H' + str(row)].value
    quote_value = sheet['I' + str(row)].value
    grant_not = sheet['J' + str(row)].value
    accept = sheet['K' + str(row)].value
    invoiced_not = sheet['L' + str(row)].value
    comment = sheet['M' + str(row)].value

    if isinstance(quote_date, date):
        quote_date = quote_date.isoformat()
    else:
        quote_date = date.today().isoformat()

    if quote_value is None:
        quote_value = "Null"
    if version is None:
        version = "Null"

    if grant_not is None:
        grant_not = "Null"
    if accept is None:
        accept = "Null"
    if invoiced_not is None:
        invoiced_not = "Null"
    if comment is None:
        comment="Null"

    query = """INSERT INTO migration_db_quote(quote_num,quote_year,version,concatenate,client,company,quote_staff,quote_date,quote_value,grant_not,accept, invoiced_not,comment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (quote_num,quote_year,version,concatenate,client,company,quote_staff,quote_date,quote_value,grant_not,accept, invoiced_not,comment)
    cursor.execute(query, values)
    database.commit()


cursor.close()

database.close()

print ("Importion Done.")



