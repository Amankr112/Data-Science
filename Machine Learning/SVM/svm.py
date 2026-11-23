import numpy as np
class SVM_classifier():

    # Initiating the hyperparameters
    def __init__(self, learning_rate, no_of_iterations, lambda_parameter):
        
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations
        self.lambda_parameter = lambda_parameter

    # Fitting the dataset to svm classifier
    def fit(self, X, Y): 
        # No. of data points -> number of rows (m)
        # No. of input features -> number of columns (n)
        self.m, self.n = X.shape

        #Initiating the weight and bias value
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        # Implementing the Gradient Descent algorithm for optimization
        for i in range(self.no_of_iterations):
            self.update_weights()


    # Function for updating the weight and bais value
    def update_weights(self):
        
        # label encoding
        y_label = np.where(self.Y <= 0, -1, 1)

        # Gradients (dw, db)
        # We use enumerate function when we want to access both the index and the value of items in an iterable
        for index, x_i in enumerate(self.X):
            condition = y_label[index] * (np.dot(x_i, self.w) - self.b) >=1

            if (condition == True):
                dw = 2 * self.lambda_parameter * self.w
                db = 0
            else:
                dw = 2 * self.lambda_parameter * self.w - np.dot(x_i, y_label[index])
                db = y_label[index]
    
            self.w -= self.learning_rate * dw
            self.b -=  self.learning_rate * db
                                          
            


    # Predict the label for a given input value
    def predict(self, X):
        output = np.dot(X, self.w) - self.b
        predicted_labels = np.sign(output)
        y_cap = np.where(predicted_labels <= -1, 0, 1)
        
        return y_cap