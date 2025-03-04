import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class MeanImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None) -> None:
        self.variables = variables
    
    def fit(self, X, y=None):
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col] = X[col].fillna(self.mean_dict[col])
        return X


class ModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None) -> None:
        self.variables = variables
    
    def fit(self, X, y=None):
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col] = X[col].fillna(self.mode_dict[col])
        return X


class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None) -> None:
        self.variables_to_drop = variables_to_drop
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X = X.drop(columns = self.variables_to_drop)
        return X


class DomainProcessing(BaseEstimator, TransformerMixin):
    def __init__(self, variable_to_modify=None, varibale_to_add=None) -> None:
        self.varibale_to_modify = variable_to_modify
        self.varibale_to_add = varibale_to_add

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.varibale_to_modify:
            X[feature] = X[feature] + X[self.varibale_to_add]
        return X


class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None) -> None:
        self.varibales = variables

    def fit(self, X, y=None):
        self.label_dict = {}
        for variable in self.varibales:
            encode = X[variable].value_counts().sort_values(ascending=True).index
            self.label_dict[variable] = {k: i for i, k in enumerate(encode, 0)}
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.varibales:
            X[feature] = X[feature].map(self.label_dict[feature])
        return X
    

class LogTransform(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None) -> None:
        self.variables = variables

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.log(X[feature])
        return X