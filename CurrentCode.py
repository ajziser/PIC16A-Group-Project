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
        
    
def cluster(self,first_var, second_var):
        #exception handling if variable is not a column we selected, still need to write
        X = penguins[[first_var, second_var, 'Species']].dropna()
        fig, ax = plt.subplots(1, figsize=(10,8))
        ax.set(xlabel = first_var,
        ylabel = second_var)
        for species, df_species in X.groupby('Species'):
            ax.scatter(df_species[first_var], df_species[second_var], label = species) #clusters the variables by species, 3 clusters
        ax.legend()
        
        

        
def decision_tree(data):
    penguins = data[["Species", "Flipper Length (mm)", "Body Mass (g)", "Sex"]]
    penguins.head()
    penguins = penguins.dropna()
    penguins.head()
    penguins = penguins[penguins["Sex"] != "."]
    penguins.shape
    np.random.seed(3354354524)
    le = preprocessing.LabelEncoder() # makes an instance of labelencoder
    penguins['Sex'] = le.fit_transform(penguins["Sex"]) # turn 'female' to 0 and 'male' to 1
    y = penguins["Species"]
    X = penguins.drop(["Species"], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    T = tree.DecisionTreeClassifier(max_depth=3)
    T.fit(X_train, y_train)
    print(T.score(X_test, y_test))
    print(T.score(X_train, y_train))
    fig, ax = plt.subplots(1, 1, figsize=(10,10))
    p = tree.plot_tree(T, filled=True, feature_names=X.columns)
    fig, ax = plt.subplots(1, figsize = (20, 20))
    p = tree.plot_tree(T, filled = True, feature_names = X.columns)







