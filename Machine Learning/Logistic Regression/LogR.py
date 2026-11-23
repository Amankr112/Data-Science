import numpy as np
class Logistic_Regression():

    # Declaring learning rate and number of iterations (HyperParamater)
    def __init__(self, learning_rate, no_of_iteration):
        self.learning_rate = learning_rate
        self.no_of_iteration = no_of_iteration

    # Fit function to train the model with dataset
    def fit(self, X, Y):

        # No. of data points in the dataset (no. of rows) - m
        # No. of input features in the dataset (no. of columns) - n
        self.m, self.n = X.shape 

        # Initiating weight & bias value 
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        # Implementing Gradient Descent for Optimization:
        for i in range(self.no_of_iteration):
            self.update_weights()

    def update_weights(self):

        # Y-cap formula (sigmod function)
        #Y_cap = 1/(1+np.exp(-z))
        Y_cap = 1/(1+np.exp(-(self.X.dot(self.w) + self.b)))   

        # Derivative
        dw = (1/self.m) * np.dot(self.X.T, (Y_cap - self.Y))     # X=[769*8] , Y=[769*1]  thats why to multiply we use transpose of X. 
        db = (1/self.m) * np.sum(Y_cap - self.Y)   

        # Updating the weights and bias using Gradient descent
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db
        
    # Sigmoid equation       
    def predict(self, X):
        Y_pred =  1/(1+np.exp(-(X.dot(self.w) + self.b)))
        Y_pred = np.where( Y_pred > 0.5, 1, 0)
        # if Y_pred > 0.5:
        #     return 1
        # else:
        #     return 0
        return Y_pred