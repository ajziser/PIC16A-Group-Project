from matplotlib import pyplot as plt
from sklearn import tree, preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class Project:
    '''Project class: Class object contains with penguins data and includes methods to clean up data, and visualize the data.
    
    Input: data-penguins pandas dataframe, saved as self.data
    Methods: clean_data-Cleans the penguins data (self.data) into a smaller subset of 5 columns.
            plot_data-Compares variables from two columns in the dataframe using a scatterplot.
            cluster-Clusters data
    
    '''
    
    
    def __init__(self, data): 
        if type(data) == pd.core.frame.DataFrame:
            self.data = data #saves data input (penguins data) to class variable self.data
        else:
            raise TypeError("Data entered must be a pandas dataframe.") #if input data is not a dataframe, TypeError is raised.

    def clean_data(self):
        '''Cleans the penguins data (self.data) into a smaller subset of columns, removes rows with NULL values, and changes the island names into numbers 0-2'''
        #saving the columns we want to work with:
        self.data = self.data[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)', 'Species']] 
        self.data = self.data.dropna()  # removes all rows with NULL
        le = preprocessing.LabelEncoder() #make an instance of labelEncoder
        X = self.data[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']].copy() # X is the feature variable, subset  of the data
        X['Island'] = le.fit_transform(X['Island']) #turns the island names into numbers 0 - 2  
        
    def plot_data(self, first_variable, second_variable):
        '''Compares variables from two columns in the dataframe using a scatterplot.
        Arguments: first_variable and second_variable: columns of self.data that will be plotted.
        Output: scatter plot with first_variable values on x axis and second_variable values on y axis.
        '''
        fig,ax = plt.subplots(1, figsize=(8,8))
        ax.scatter(self.data[first_variable], self.data[second_variable])
        ax.set(xlabel=first_variable,ylabel=second_variable)
        
    def cluster(self, first_var, second_var):
        '''Clusters data according to input.
        Arguments: first_var and second_var: names of columns in self.data to be clustered
        Output: scatter plot of clustered data
        '''
        fig, ax = plt.subplots(1, figsize=(10,8)) #creates one plot of size width 10, and height 8
        
        try:
            X = self.data[[first_var, second_var, 'Species']].dropna() #?
            ax.set(xlabel = first_var,
            ylabel = second_var)
            for species, df_species in X.groupby('Species'): 
                ax.scatter(df_species[first_var], df_species[second_var], label = species) #plots the variables by species, 3 clusters
            ax.legend()   
        except KeyError:
            print("Variable input name not found in dataframe") #If KeyError is raised by the try block of code because the input is not in the data, this message is printed.
        finally:
            return fig, ax #return the plot created, even if there was a KeyError and nothing was plotted
        
        

def decision_tree(data):
    '''Docstring'''
    penguins = data[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)', 'Species']]
    penguins = penguins.dropna()
    np.random.seed(3354354524)
    le = preprocessing.LabelEncoder() # makes an instance of labelencoder
    penguins['Island'] = le.fit_transform(penguins["Island"]) # turn 'female' to 0 and 'male' to 1
    y = penguins["Species"]
    X = penguins.drop(["Species"], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8)
    T = tree.DecisionTreeClassifier(max_depth=2)
    T.fit(X_train, y_train)
    print(T.score(X_test, y_test))
    print(T.score(X_train, y_train))







