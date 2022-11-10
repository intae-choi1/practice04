from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

ws.delete_rows(8) # 8번째 row 삭제
ws.delete_rows(8,3) # 8부터 3개 row 삭제

wb.save("sample_delete_rows.xlsx")