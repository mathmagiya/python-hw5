from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import r_regression
from sklearn.linear_model import LinearRegression

class CreationalFactoryPattern:
	def __init__(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train


	def get_subsample(self, df_share):
		iris_copied = iris
		X_train, y_train = iris_copied.data[:, :2], iris_copied.target 
		X_train, y_train = shuffle(X_train, y_train, random_state= df_share)
		return df_share 
		
		"""
		1. Copy train dataset
		2. Shuffle data (don't miss the connection between X_train and y_train)
		3. Return df_share %-subsample of X_train and y_train
		"""



	if __name__ == "__main__":
		iris = datasets.load_iris()
		X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33) 
	"""
	1.	Load iris dataset
	2. Shuffle data and divide into train / test.
	"""
	
	pattern_item = CreationalPatternFactory()
	for df_share in range(10, 101, 10):
		curr_X_train, curr_y_train = pattern_item.get_subsample(X_train, y_train)
		curr_X_train = scaler.transform(X_train)
		curr_y_train = scaler.transform(X_test)
		print(r_regression(curr_X, curr_y, center=True))
	"""
	1.	Preprocess curr_X_train, curr_y_train in the way you want
	2.	Train Linear Regression on the subsample
	3.	Save or print the score to check how df_share affects the quality
	"""
	

