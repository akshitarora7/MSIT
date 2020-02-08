#Akshit Arora LAb 11

fileName = '/Users/akshitarora/Downloads/Python IO/'
stock1FileName = '/Users/akshitarora/Downloads/Python IO/AAPL.csv'
#stock2FileName = '/Users/akshitarora/Downloads/Python IO/MSFT.csv'

import pandas as pd
stock1DF = pd.read_csv(stock1FileName, header = 0)
#stock2DF = pd.read_csv(stock2FileName, header = 0)

#cast columns to needed DataTypes - stock 1
#stock1DF['Volume'] = stock1DF['Volume'].astype(int)
stock1DF['Date'] = pd.to_datetime(stock1DF['Date'], format = '%Y-%m-%d')
#stock1DF = stock1DF.set_index(['Date'])
print(stock1DF)
##cast columns to needed DataTypes - stock 2
#stock2DF['Volume'] = stock2DF['Volume'].astype(int)
#stock2DF['Date'] = pd.to_datetime(stock2DF['Date'], format = '%Y-%m-%d')
#stock2DF = stock2DF.set_index(['Date'])
#
#combinedDF = stock1DF.join(stock2DF, how = 'outer', lsuffix = '_stock1', rsuffix = '_stock2')
#
#print(combinedDF.loc['2000-01-01':'2000-02-01'])
#
#combinedByYearDF = combinedDF.resample('Y').mean()
#
#print(combinedByYearDF)
#
#
#import matplotlib.pyplot as pp
#
#y1 = combinedByYearDF['Close_stock1'].values
#y2 = combinedByYearDF['Close_stock2'].values
#x = combinedByYearDF.index
#
#pp.plot(x, y1)
#pp.plot(x, y2)
#pp.show()













#import quandl
#quandl.ApiConfig.api_key = 'BNy_ZPWsiEbwMz_BT8sL'
#
##userInput = input('Please enter the ticker symbol:\n>>')
#userInput = 'AAPL'
#stockFound = 'n'
#while stockFound == 'n':
#    try:
#        stockData = quandl.get('WIKI/'+userInput)
#        stockFound = 'y'
#    except quandl.errors.quandl_error.NotFoundError:
#        userInput = input('Could not find that ticker symbol. Please enter another ticker symbol:\n>>')
#    except:
##        print('Could not connect to the data reader. Please check your internet connection.')
#        stockFound = 'y'
#        
##write to file
#fileName = fileName + userInput + '.csv'
#stockData.to_csv(fileName, header = True)

