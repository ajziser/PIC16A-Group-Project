class Project:
    def __init__(self, data):
        self.data = data
        
    
    # 2 examples of exception handling
    
    def clean_data(self):
        #saving the columns we want to work with
        self.data = penguins[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)', 'Species']] 
        self.data = penguins.dropna()  # removes all rows with NULL
        le = preprocessing.LabelEncoder() #make an instance of labelEncoder
        X = penguins[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']].copy() # X is the feature variable, subset  of the data
        X['Island'] = le.fit_transform(X['Island']) #turns the island names into numbers 0 - 2  
        #return something?
       
    def plot_data(self, first_variable, second_variable): #compare two variables using a scatterplot
        fig,ax = plt.subplots(1, figsize=(8,8))
        ax.scatter(first_variable, second_variable)
        
    def cluster(self, first_var, second_var):
        #exception handling if variable is not a column we selected, still need to write
        X = self.data[[first_var, second_var, 'Species']]
        fig, ax = plt.subplots(1, figsize=(10,8))
        for species, df_species in X.groupby('Species'):
            ax.scatter(df_species[first_var], df_species[second_var], label = species) #clusters the variables by species, 3 clusters
    
        
        

        

#outside function -  decision tree 
'''
np.random.seed(3354354524)
y = penguins["Species"]
X = penguins[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']].copy()

le = preprocessing.LabelEncoder()
X['Island'] = le.fit_transform(X['Island'])
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

T = tree.DecisionTreeClassifier(max_depth=3) 
T.fit(X_train, y_train)
print(T.score(X_train, y_train))
print(T.score(X_test, y_test))

'''







