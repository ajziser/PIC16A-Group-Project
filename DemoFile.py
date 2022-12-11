#Demo with instructions for running this code found in README.md.

import pandas as pd
from CurrentCode import Project, decision_tree

url = "https://philchodrow.github.io/PIC16A/datasets/palmer_penguins.csv"
penguins = pd.read_csv(url)
penguins.head()

project = Project(penguins)
project.clean_data()
project.data.head()

project.scatterplot('Species', 'Delta 15 N (o/oo)')
project.cluster('Body Mass (g)', 'Delta 15 N (o/oo)')

decision_tree(penguins)
