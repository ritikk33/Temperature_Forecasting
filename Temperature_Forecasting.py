import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.layers import Dropout

NUM_OF_PREV_ITEMS = 5


# construct an array of values into a matrix of features
# that are the previous time series values in the past
def reconstruct_data(data_set, n=1):
    x, y = [], []

    for i in range(len(data_set) - n - 1):
        a = data_set[i:(i + n), 0]
        x.append(a)
        y.append(data_set[i + n, 0])

    return numpy.array(x), numpy.array(y)


# Random numbers generation
numpy.random.seed(1)
data_frame = read_csv('daily_min_temperatures.csv', usecols=[1])

data = data_frame.values
data = data.astype('float32')

scaler = MinMaxScaler(feature_range=(0, 1))
data = scaler.fit_transform(data)
# split it in 70% train and 30% test
train, test = data[0:int(len(data) * 0.7), :], data[int(len(data) * 0.7):len(data), :]
# create the training data and test data matrix
train_x, train_y = reconstruct_data(train, NUM_OF_PREV_ITEMS)
test_x, test_y = reconstruct_data(test, NUM_OF_PREV_ITEMS)

# reshape input to be [numOfSamples, time steps, numOfFeatures]
# time steps is 1 because we want to predict tomorrow's temp
train_x = numpy.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
test_x = numpy.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

model = Sequential()
model.add(LSTM(units=100, return_sequences=True, input_shape=(1, NUM_OF_PREV_ITEMS)))
model.add(Dropout(0.5))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(units=50))
model.add(Dropout(0.3))
model.add(Dense(units=1))
# optimize with ADAM
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(train_x, train_y, epochs=10, batch_size=16, verbose=2)

test_predict = model.predict(test_x)
test_predict = scaler.inverse_transform(test_predict)
test_labels = scaler.inverse_transform([test_y])

test_score = mean_squared_error(test_labels[0], test_predict[:, 0])
print('Score on test set: %.2f MSE' % test_score)

test_predict_plot = numpy.empty_like(data)
test_predict_plot[:, :] = numpy.nan
test_predict_plot[len(train_x)+2*NUM_OF_PREV_ITEMS+1:len(data)-1, :] = test_predict
plt.plot(scaler.inverse_transform(data))
plt.plot(test_predict_plot, color='green')
plt.show()
