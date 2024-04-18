import pandas as pd
import openpyxl

class Save_to_excel:
    def __init__(self,list1:list,list2:list,list3:list,file_name:str):
        # Define the lists
        x = list1 # coordinates
        y1 = list2 # temperature
        y2 = list3 # viscosity

        # Create a DataFrame
        temperature_dataframe = pd.DataFrame({'X': x, 'Y': y1})
        viscosity_dataframe = pd.DataFrame({'X': x, 'Y': y2})


        # Create a new Excel file and add the DataFrame to it
        book = openpyxl.Workbook()
        writer = pd.ExcelWriter(book, engine='openpyxl')
        temperature_dataframe.to_excel(writer, sheet_name='temperature')
        viscosity_dataframe.to_excel(writer,sheet_name='viscosity')
        writer.save()

        # Create a chart in the Excel file
        # Plot temperature graph
        wb = openpyxl.load_workbook(f'{file_name}.xlsx')

        temperature_ws = wb['temperature']

        temperature_chart = openpyxl.chart.ScatterChart()
        temperature_chart.title = 'График изменения температуры по длине канала'
        temperature_chart.x_axis.title = 'Координаты по длине канала, м'
        temperature_chart.y_axis.title = 'Температура, '

        x_data = openpyxl.chart.Series(values=temperature_ws['X'])
        y_data = openpyxl.chart.Series(values=temperature_ws['Y'])

        temperature_chart.series.append(x_data)
        temperature_chart.series.append(y_data)

        temperature_ws.add_chart(chart, "E2")

        # Plot viscosity graph
        viscosity_ws = wb['viscosity']

        viscosity_chart = openpyxl.chart.ScatterChart()
        viscosity_chart.title = 'График изменения Вязкости по длине канала'
        viscosity_chart.x_axis.title = 'Координаты по длине канала, м'
        viscosity_chart.y_axis.title = 'Вязкость'

        x_data = openpyxl.chart.Series(values=viscosity_ws['X'])
        y_data = openpyxl.chart.Series(values=viscosity_ws['Y'])

        viscosity_chart.series.append(x_data)
        viscosity_chart.series.append(y_data)


        viscosity_ws.add_chart(chart, "E2")
        wb.save(f'{file_name}.xlsx')