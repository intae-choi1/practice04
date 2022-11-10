from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8 row에 insert
ws.insert_rows(8, 5) # 8부터 5줄 추가

# ws.insert_cols(2) # B 열에 insert
ws.insert_cols(2, 3) # B부터 3줄 insert


wb.save("sample_insert_rows.xlsx")