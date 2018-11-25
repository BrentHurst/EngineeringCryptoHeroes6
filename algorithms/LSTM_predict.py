from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from math import sqrt
from numpy import concatenate
from pandas import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
import sys 

# convert series to supervised learning: pushes column for variable to predict by 1 (since we are using t to predict t+1)
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

# convert data to flaot
values = values.astype('float32')

# normalize features using MinMax between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = format_output_column(scaled, 1, 1)

# drop columns we don't want to predict
reframed.drop(reframed.columns[[4,5,7]], axis=1, inplace=True)


# split into train and test sets
values = reframed.values
# leave last 30 days for testing
n_train_hours = 30; 
train = values[1:-30, :]
test = values[-30:-1, :]
# split into input and outputs
train_X = train[:,:-1];  
train_y = train[:,-1]; 
test_X  = test[:,:-1]; 
test_y = test[:,-1];
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

# design network
model = Sequential()
model.add(LSTM(300, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')

# fit network
history = model.fit(train_X, train_y, epochs=100, batch_size=50, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# plot history
#pyplot.plot(history.history['loss'], label='train')
#pyplot.plot(history.history['val_loss'], label='test')
#pyplot.legend()
#pyplot.title('RNN Fitting')
#pyplot.xlabel('Epochs', fontsize=16)
#pyplot.ylabel('Value Loss', fontsize=16)
#pyplot.show()
 
# make a prediction on the test data
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))

# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]

# calculate RMSE
#dates = itertools.islice(date_generator(), 30)
pyplot.plot(inv_y, marker='o', linestyle='-', color='b', label='Actual Price')
pyplot.plot(inv_yhat, marker='o', linestyle='-', color='r' , label='Forecasted Price using LSTM RNN')
pyplot.legend()
pyplot.title("Testing over past 30 days (Nov 1st)")
pyplot.xlabel('Days', fontsize=18)
pyplot.ylabel('Bitcoin Price ($)', fontsize=16)
pyplot.savefig('img/LSTM.png');
pyplot.show()

rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse) 
#print(train_y[-60:])  

# print out the actual price 
print(inv_y) 
# print out the forecast price  
print(inv_yhat) 

actual_price = inv_y 
forecast = inv_yhat 

# assume that you have 1000 dollars, 500 dollars for investing. 500 dollars to move around   

print("Investment $500, Saving $500, Total $1000\n");  
saving = 500 
invest_B = 500/actual_price[0] 
 
for i in range(0, actual_price.shape[0]): 
	if i > 0 and forecast[i-1] < forecast[i] and saving > 100: 
		invest_B = invest_B + saving * 0.2 /actual_price[i] 
		saving = saving * 0.8  
		print("day ", i, " Buy in, Bitcoin:", invest_B, "saving:", saving) 
        elif i > 0 and forecast[i-1] > forecast[i]: 
		saving = saving + invest_B * 0.2 * actual_price[i] 
		invest_B = invest_B * 0.8   
		print("day", i, " Buy out, Bitcoin: ", invest_B, "saving", saving) 
saving = saving + invest_B * actual_price[i]  

print("final total worth is ", saving) 	
