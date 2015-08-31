from openpyxl import load_workbook
import uuid

from database import Applicant, engine, DBSession, Base


def open_table(index):
    PATH = '/Users/liyanze/Documents/test.xlsx'
    wb = load_workbook(PATH)
    return wb.get_sheet_by_name('Sheet 1')


def insert_data(sheet):
    row_num = sheet.row
    session = DBSession()
    for row in range(2, row_num):
        row_val = table.row_values(row)
        print(row_val)
        # session.add(Applicant(
        #     id = uuid.uuid4(),
        #     name = row_val[1],
        #     major = row_val[2],
        #     contact = row_val[3],
        #     group = row_val[4],
        #     inter_time = row_val[5],
        #     inter_place = row_val[6],
        #     status = row_val[7]
        # ))
    #     session.commit()
    # session.close()

if __name__ == "__main__":
    table = open_table(0)
    insert_data(table)
