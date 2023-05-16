from django.shortcuts import render
import openpyxl

def list01(request):
    if request.method=='GET':
        return render(request, 'app_dashboard.html')
    raw_file = request.FILES['raw_file']

    wb = openpyxl.load_workbook(raw_file)
    sheet = wb['sheet1']

    excel_data = list()
    
    for row in sheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)

    return render(request, 'app_dashboard.html', {
        'excel_data': excel_data,
    })