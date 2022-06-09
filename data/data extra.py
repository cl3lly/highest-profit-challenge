import pandas as pd

df = pd.read_csv('data.csv')  # read csv to program
number_of_rows = len(df.axes[0])  # calculate the number of rows
print("Number of Rows: "+str(number_of_rows))  # print calculation

df.rename(columns={'Profit (in millions)': 'Profit'}, inplace=True)  # change name of profit column
conciseDF = df[df.Profit != "N.A."].copy()  # exclude all rows with NA and copy to new df
conciseDF['Profit'] = pd.to_numeric(conciseDF['Profit'])  # convert profit column to integer
number_of_rows_left = len(conciseDF.axes[0])  # calculate number of rows left
print("Number of Rows After Removing Non-Numeric Rows: "+str(number_of_rows_left))  # print number of rows left


conciseDF.to_json(r'data2.json')  # create json file


newdf = conciseDF.sort_values(by='Profit', ascending = False)  # sort profit column
newdf.rename(columns={'Profit': 'Profit (in millions)'}, inplace=True)  # change profit column name back to original
print(newdf.head(20))
