from db.models import Record
import openpyxl
import logging
logger = logging.getLogger(__name__)


# for i in range(0,100):
#     o = Record()
#     o.ac_reg = "HVN"+str(i)
#     o.save()


# data = Record.objects.all()
# print(data.count())
# for it in data:
#     print(it.ac_reg)


from openpyxl import load_workbook
wb = load_workbook(filename = 'files/'+'01-07-22.xlsx')
worksheet = wb.worksheets[0]
header_list = []

for row in worksheet.iter_rows():
    # logger.debug(row)
    if not header_list:
        for cell in row:
            header_list.append(cell.value)
        print("header_list =", header_list)
        ac_reg_idx = header_list.index("A/C REG")
        type_idx = header_list.index("TYPE")
        arr_idx = header_list.index("ARR")
        dep_idx = header_list.index("DEP")
        route_idx = header_list.index("ROUTE")
        date_idx = header_list.index("DATE")
        eta_time_idx = header_list.index("ETA")
        etd_time_idx = header_list.index("ETD")

    else:
        logger.debug("============================================================")
        o = Record()
        o.ac_reg = str(row[ac_reg_idx].value)
        o.type = str(row[type_idx].value)
        o.arr = str(row[arr_idx].value)
        o.dep = str(row[dep_idx].value)
        # o.date = str(row[date_idx].value)
        o.route = str(row[route_idx].value)
        o.time_eta = str(row[eta_time_idx].value)
        o.time_etd = str(row[etd_time_idx].value)
        print("o.ac_reg = %s" %(o.ac_reg))
        print("o.type = %s" %(o.type))
        print("o.arr = %s" %(o.arr))
        print("o.date = %s" %(str(row[date_idx].value)))

        print("o.date = %s" %(worksheet["M2"].value))

        print("o.dep = %s" %(o.dep))
        print("o.route = %s" %(o.route))
        print("o.eta = %s" %(o.eta))
        print("o.etd = %s" %(o.etd))
        o.save()