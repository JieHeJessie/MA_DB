import openpyxl
import MySQLdb
from datetime import date, datetime
import decimal
from openpyxl.formula import Tokenizer
import MySQLdb as mdb

book = openpyxl.load_workbook("BioScience MA Invoices.xlsx", data_only=True)
sheet = book.get_sheet_by_name('2016-2017')

database = MySQLdb.connect(host="localhost", user="root", passwd="wang123Q", db="ma_newdb")
cursor = database.cursor()

for row in range(10, 15):
    invoice_date = sheet['A' + str(row)].value
    invoice_num = sheet['B' + str(row)].value
    bad_debt = sheet['C' + str(row)].value
    quote = sheet['D' + str(row)].value
    paid = sheet['E' + str(row)].value
    ma_staff = sheet['F' + str(row)].value
    project_invoice = sheet['G' + str(row)].value
    service_type = sheet['H' + str(row)].value
    instrument = sheet['I' + str(row)].value
    person_invoice = sheet['J' + str(row)].value
    address = sheet['K' + str(row)].value
    no_sample_in = sheet['L' + str(row)].value
    category_in = sheet['M' + str(row)].value
    int_ext_in = sheet['N' + str(row)].value
    user_define1_in = sheet['O' + str(row)].value
    user_define2_in = sheet['P' + str(row)].value
    sub_total_in = sheet['q' + str(row)].value
    reconciliation = sheet['r' + str(row)].value
    running_total = sheet['s' + str(row)].value
    if isinstance(invoice_date, date):
        invoice_date = invoice_date.isoformat()
    else:
        invoice_date = date.today().isoformat()
    if bad_debt is None:
        bad_debt = "Null"
    if paid is None:
        paid = "Null"
    if reconciliation is None:
        reconciliation = "Null"
    if running_total is None:
        running_total = "Null"

    query = """INSERT INTO migration_db_invoice(invoice_date,invoice_num,bad_debt,quote,paid,ma_staff
                                                    ,project_invoice,service_type,instrument,person_invoice,address,no_sample_in,category_in,
                                                    int_ext_in, user_define1_in, user_define2_in, sub_total_in, reconciliation, running_total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    print query
    values = (invoice_date, invoice_num, bad_debt, quote, paid, ma_staff, project_invoice,service_type,
                  instrument, person_invoice, address, no_sample_in, category_in, int_ext_in, user_define1_in,
                  user_define2_in, sub_total_in,reconciliation, running_total)
    cursor.execute(query, values)

database.commit()
cursor.close()

database.close()
print ("Importion Done.")



