import numpy as np

class LinearRegression:
    def __init__(self):
        self.W=None
        self.b=None

    def fit(self,X,y):
        """
        learning func
        :param X: independent train(2d array)
        :param y: dependent label(2d array)
        :return:
        """
        X_mean=np.mean(X)
        y_mean=np.mean(y)

        denominator = np.sum(pow(X-X_mean,2))
        numerator=np.sum((X-X_mean)*(y-y_mean))

        self.slope=numerator/denominator
        self.intercept=y_mean-(self.slope*X_mean)

    def predict(self,X)->np.ndarray:
        """
        predict value for input
        :param X: new independent
        :return: predict value for input
        """
        return self.slope*np.array(X)+self.intercept