import numpy as np
import operator as op 

class KNearestNeighbor(object):

  def __init__(self):
    pass

  def train(self, X, y):
    
    self.X_train = X
    self.y_train = y
    
  def predict(self, X, k=1, num_loops=0):
    
    if num_loops == 0:
      dists = self.compute_distances_no_loops(X)
    elif num_loops == 1:
      dists = self.compute_distances_one_loop(X)
    elif num_loops == 2:
      dists = self.compute_distances_two_loops(X)
    else:
      raise ValueError('Invalid value %d for num_loops' % num_loops)

    return self.predict_labels(dists, k=k)

  def compute_distances_two_loops(self, X):
    
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
      for j in range(num_train):
        
        dists[i, j] = np.sqrt(np.sum((X[i] - self.X_train[j])**2))

        pass
        
    return dists

  def compute_distances_one_loop(self, X):
    
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
      
      dists[i] = np.sqrt(np.sum((X[i] - self.X_train)**2, axis=1))

      pass
      
    return dists

  def compute_distances_no_loops(self, X):
    
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train)) 
    
    dists = np.sum(self.X_train**2, axis=1) + np.sum(X**2, axis=1)[:, np.newaxis] - 2 * np.matmul(X, self.X_train.T)

    pass
    
    return dists

  def predict_labels(self, dists, k=1):
    
    num_test = dists.shape[0]
    y_pred = np.zeros(num_test)
    for i in range(num_test):
      
      closest_y = []
      
      indices = np.argsort(dists[i])
      ascending = list(op.itemgetter(*indices.tolist())(self.y_train))
      closest_y = ascending[:k]

      pass
    
      from scipy import stats
      y_pred[i] = stats.mode(closest_y)[0]

      pass
      

    return y_pred

