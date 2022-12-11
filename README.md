# PIC16A Group Project: Clustering Penguins
## Anna Ziser, Lauren Nemeh, Lyndsey Mitsch

In our project, we explore the penguins dataset and manipulate the data through graphing and training the data with a decision tree model. As a group, we felt like we needed more practice working with datsets and getting more comfortable with manipulating/graphing datasets in a class. We graphed the data via scatterplots and clustering with groupby() in order to get a better understanding of the relationships between the different variables.  In our code, we referenced material from our class and discussion work.

Python packages used (and versions): pandas, matplotlib, sklearn, numpy.

Demo description/How to run the demo file:
1. Open a new notebook and python file in JupyterLab, inside the same folder.
2. Copy CurrentCode.py into the .py file, rename the file CurrentCode, and save it. 
3. Rename the .ipynb file to DemoFile and navigate to the Demo File code from github.
4. Paste and run the first 8 lines of the Demo File into a cell in the .ipynb file to import pandas, read the penguins data, and import the CurrentCode file. There should be no errors or results from running this cell. 
5. Run line 7 inside the same cell to get a preview of the existing penguins data.  You should see the dataframe like this:

Screen Shot 2022-12-10 at 4.20.36 PM<img width="1015" alt="image" src="https://user-images.githubusercontent.com/114253056/206880731-6302bed7-125b-42d0-95ac-d9fc7bdb2971.png">
6. Create a new cell and run lines 11-13 of the Demo File to create a Project class object with the penguins dataframe, and run the clean_data function. Line 12 will show the preview of the cleaned up data, which has fewer columns compared to the original data we saw in the previous step:

Screen Shot 2022-12-10 at 4.21.06 PM<img width="627" alt="image" src="https://user-images.githubusercontent.com/114253056/206880722-0e26286a-21a6-4583-9619-5d8130e4a0cc.png">

7. In a new cell, run line 15 of the demo file. This will run the scatterplot function of the class to compare the penguins Species with the Delta 15 N. You should see a graph like this:

<img width="596" alt="Screen Shot 2022-12-10 at 4 56 46 PM" src="https://user-images.githubusercontent.com/114253056/206881439-ae42cfeb-85f7-4399-9c18-ff3318480683.png">

This plot shows the correlation between Delta 15 N (o/oo) and the penguin Species. Chinstrap Penguins generally had a higher Delta 15 N value, and Gentoo penguins had a lower value. You can run this line of code with different column names to see other correlations between the penguins data.

8. In a new cell, run line 16 of the demo file. This will call the cluster function of the class to plot the two variables in the data against one another, colored.grouped by penguin species. You should see a graph like this:

<img width="614" alt="Screen Shot 2022-12-10 at 5 02 03 PM" src="https://user-images.githubusercontent.com/114253056/206881542-e16d2185-82c0-411e-bec4-67f740891bd6.png">

This scatterplot shows the differences in Body mass compared to Delta 15 N (o/oo) depending on the penguin species. There are relatively clear clusters of the trait combinations of each species. You can run the cluster function with different values to observe which traits cluster the most clearly depending on species. 

9. Finally, run line 18 of the demo file code to create a decision tree with penguins data. It will print two values, the training data score (~.939) and the test data score (~.882) for the model. This model uses a max depth of 2 to avoid overfitting or underfitting, but you can modify the mex depth in the CurrentCode file to see how the accuracy scores change with a different depth of decision tree. 

Conclusions: In the future, the scope of this project could be larger and use more models. For example, this project could be expanded through writing various algorithms such as a neural network model and comparing the models to each other to see what is the most efficient. Our project does not have any ethical implications because the datset was found online and does not have any kind of algorithmic bias.
