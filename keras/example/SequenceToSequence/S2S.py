from keras.models import Sequential
import numpy as np
from keras.layers.recurrent import SimpleRNN, GRU, LSTM
from keras.layers.core import Dense, Activation

n_in_out = 1
n_in = 1
n_out = 1
n_hidden = 100
n_samples = 2297
n_timesteps = 400

model = Sequential()
# `return_sequences` controls whether to copy the input automatically
model.add(GRU( n_hidden, input_dim = n_in_out, return_sequences=True))
model.add(Dense(n_in_out, input_dim = n_hidden))
model.compile(loss='mse', optimizer='rmsprop')

X = np.random.random((n_samples, n_timesteps, n_in))
Y = np.random.random((n_samples, n_timesteps, n_out))

# learning the hidden states from source sentences

Xp = model.predict(X)
print(Xp.shape)
print(Y.shape)

model.fit(X, Y, nb_epoch=10)