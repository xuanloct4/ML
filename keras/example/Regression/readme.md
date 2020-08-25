http://danielhnyk.cz/predicting-sequences-vectors-keras-using-rnn-lstm/
Update (24. 03. 2017): My dear friend Tomas Trnka rewrote the code below for Keras 2.0! Check it on his github repo (https://github.com/trnkatomas/Keras_2_examples/blob/master/Simple_LSTM_keras_2.0.ipynb)!

Update (28.11.2015): This article become quite popular, probably because it's just one of few on the internet (even thought it's getting better). Please read the comments where some readers highlights potential problems of my approach. Furthermore I am afraid I can't help you with your specific cases, since I don't work with LSTM any more. And, to be honest, I don't really feel very confident about my understanding to LSTM to give advices. This is just what worked for me.

My task was to predict sequences of real numbers vectors based on the previous ones. This task is made for RNN. As you can read in my other post Choosing framework for building Neural Networks (mainly RRN - LSTM), I decided to use Keras framework for this job.

Coding LSTM in Keras

CAUTION! This code doesn't work with the version of Keras higher then 0.1.3 probably because of some changes in syntax here and here. For that reason you need to install older version 0.1.3. To do that you can use pip install keras==0.1.3 (probably in new virtualenv). For this tutorial you also need pandas. Please let me know if you make it work with new syntax so I can update the post.

Example code for this article can be found in this gist. This is tested on keras 0.1.3. It is edited a bit so it's bearable to run it on common CPU in minutes (~10 minutes on my laptop with i5). When you plot the results from resulted .csv files you should get something like this: 
Predicted up, testing down where predicted points are up and true data down.

Quick hands-on

To run the script just use python keras.py. It will create two csv files (predicted.csv and test_data.csv) which should be almost same.

Step-by-step solution

Keras have pretty simple syntax and you just stack layers and their tuning parameters together.Let's build our first LSTM.

The code is as follows:

from keras.models import Sequential  
from keras.layers.core import Dense, Activation  
from keras.layers.recurrent import LSTM

in_out_neurons = 2  
hidden_neurons = 300

model = Sequential()  
model.add(LSTM(in_out_neurons, hidden_neurons, return_sequences=False))  
model.add(Dense(hidden_neurons, in_out_neurons))  
model.add(Activation("linear"))  
model.compile(loss="mean_squared_error", optimizer="rmsprop")  
and that's it! We just created LSTM NN which expects vector of length 2 and NN has 1 leayer with 300 hidden neurons. It returns vector of length 2 (this doesn't have to be the same in your case, but for my purposes it is).

Data preparation

Now we need to prepare data. Let's generate some randomly (you need pandas library for this example). Imagine that we have two stocks and we have prices for every minute.

import pandas as pd  
from random import random

flow = (list(range(1,10,1)) + list(range(10,1,-1)))*1000  
pdata = pd.DataFrame({"a":flow, "b":flow})  
pdata.b = pdata.b.shift(9)  
data = pdata.iloc[10:] * random()  # some noise  
this will create the saw-like columns shifted to each other.