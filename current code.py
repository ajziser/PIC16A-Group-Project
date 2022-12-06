url = "https://philchodrow.github.io/PIC16A/datasets/palmer_penguins.csv"
penguins = pd.read_csv(url)


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
        
    def plot_data(self, feature_variable): #compare species w other variable
        species = self.data['Species']
        fig,ax = plt.subplots(1, figsize=(8,8))
        ax.scatter(species, feature_variable)
        
        
        
        
    #3rd method
        # cluster 
    
        
        

        

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







