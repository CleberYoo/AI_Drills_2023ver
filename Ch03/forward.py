import numpy as np   # numerical python

def sigmoid(x):   # define the sigmoid function
    return 1 / (1 + np.exp(-x))

def identity_function(x):   # just call myself
    return x

def myNetwork():
    network = {}    # empty dictionary
                    # it will be appended key : value pairs later
    network['W1'] = np.array([[0.1,0.3,0.5],   # input layer's Weight
                              [0.2,0.4,0.6]])   # size : 2 X 3
    network['b1'] = np.array([0.1,0.2,0.3])   # input layer's Bias   # size : 1 X 3
    network['W2'] = np.array([[0.1,0.4],   # 1st hidden layer's Weight
                              [0.2,0.5],   # size : 3 X 2
                              [0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])   # 1st hidden layer's Bias   # size : 1 X 2
    network['W3'] = np.array([[0.1,0.3],   # output layer's Weight
                              [0.2,0.4]])   # size : 2 X 2
    network['b3'] = np.array([0.1,0.2])   # output layer's Bias   # size : 1 X 2
    print(network)
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x,W1)+b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2)+b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3)+b3
    y = identity_function(a3)
    
    return y

network = myNetwork()
x = np.array([1.0,0.5])
y = forward(network, x)
print(y)