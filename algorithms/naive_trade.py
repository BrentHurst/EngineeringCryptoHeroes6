from math import sqrt
from numpy import concatenate
import numpy as np
from pandas import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
import sys 

def format_output_column(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg


# load dataset
if len(sys.argv)==1: 
	dataset = read_csv('rev_bitcoinhistorical.csv', header=0, index_col=0)
elif sys.argv[1] == "eth": 
	dataset = read_csv('rev_etheriumhistorical.csv', header=0, index_col=0)
elif sys.argv[1] == "lit": 
	dataset = read_csv('rev_litecoinhistorical.csv', header=0, index_col=0)
else: 
	dataset = read_csv('rev_bitcoinhistorical.csv', header=0, index_col=0)

values = dataset.values

# convert data to float
values = values.astype('float32')

# frame as supervised learning
reframed = format_output_column(values, 1, 1)

# drop columns we don't want to predict
reframed.drop(reframed.columns[[4,5,7]], axis=1, inplace=True)

# split into train and test sets
values = reframed.values
# leave last 30 days for testing
n_train_hours = 30; 
train = values[1:-50, :]
test = values[-50:-1, :]
# split into input and outputs
train_X = train[:,:-1];  
train_y = train[:,-1]; 
test_X  = test[:,:-1]; 
test_y = test[:,-1];
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

output_x = test_y; 

print(test_y) 
print(test_y.shape) 

twenty_moving_average = []
ten_moving_average = [] 
for i in range(0,test_y.shape[0]-20): 
	twenty_moving_average.append(np.mean(test_y[i:i+20])) 
	ten_moving_average.append(np.mean(test_y[i+15:i+20]))
	print (np.mean(test_y[i:i+20]), np.mean(test_y[i+15:i+20])) 
	
print ten_moving_average
print twenty_moving_average

# plot history
#pyplot.plot(history.history['loss'], label='train')
#pyplot.plot(history.history['val_loss'], label='test')
#pyplot.legend()
#pyplot.title('RNN Fitting')
#pyplot.xlabel('Epochs', fontsize=16)
#pyplot.ylabel('Value Loss', fontsize=16)
#pyplot.show()
 
# calculate RMSE
#dates = itertools.islice(date_generator(), 30)

#pyplot.plot(ten_moving_average, marker='o', linestyle='-', color='b', label='5 day moving average')
#pyplot.plot(twenty_moving_average, marker='o', linestyle='-', color='r' , label='20 days moving average')
#pyplot.plot(test_y[-30:], marker='o', linestyle='-', color='g', label='Actual Price')

#pyplot.legend()
#pyplot.title("Testing over past 30 days (Nov 1st)")
#pyplot.xlabel('Days', fontsize=18)
#pyplot.ylabel('Bitcoin Price ($)', fontsize=16)
#pyplot.show()

# print out the actual price 
#print(inv_y) 
# print out the forecast price  
#print(inv_yhat) 


actual_price = test_y[-29:]  

print("Investment $500, Saving $500, Total $1000\n");  
saving = 500 
invest_B = 500/actual_price[0] 

saving = saving + invest_B * actual_price[-1]  

print("final total worth is ", saving) 	
