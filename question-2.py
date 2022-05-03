from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from scipy import stats
classifiers

class StructuralPatternName:
	def __init__(self, classifiers) -> None:
		self.classifiers=classifiers
		"""
		Initialize a class item with a list of classificators
		"""
	def fit(self, classifiers):
		#scaler=[]
		for i in range(0,len(classifiers)):
			scaler.append(StandardScaler().fit(classifiers[i]))
		"""
		Fit classifiers from the initialization stage
		"""
		
	def predict(self, classifiers):
		classifiers = ExtraTreesClassifier(n_estimators=10, max_depth=None,
		min_samples_split=2, random_state=0)
		scores = cross_val_score(classifiers, X, y, cv=5)
		return stats.mode(scores)

		"""
		Get predicts from all the classifiers and return
		the most popular answers
		"""
	if __name__ == "__main__":
		iris = datasets.load_iris()
		X_train, y_train = iris.data[:, :2], iris.target 
		X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33) 
		classifiers=["ExtraTreesClassifier","RandomForestClassifier"]
		RandomForestClassifier(max_depth=2, random_state=0)
		"""
		1. Load iris dataset
		2. Shuffle data and divide into train / test.
		3. Prepare classifiers to initialize <StructuralPatternName> class.
		4. Train the ensemble
		"""
		
		
		clf1 = RandomForestClassifier(max_depth=2, random_state=0)
		clf2 = ExtraTreesClassifier(max_depth=2, random_state=0)
		print(clf1.predict([X_test]))
		print(clf2.predict([[X_test]]))
