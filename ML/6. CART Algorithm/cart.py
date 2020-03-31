import pandas as pd
import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.paths = []
        self.children = []

    def add_child(self, path, child):
        self.paths.append(path)
        self.children.append(child)

    def get_node(self):
        return self.data.title()

    def build_tree(self, tabs):
        if len(self.children) == 0:
            return self.data
        else:
            print(' ' * tabs + '*', self.data.title())
            tabs += 4
            for i, child in enumerate(self.children):
                print(' ' * tabs + '|', self.paths[i].title())
                data = child.build_tree(tabs)
                if data:
                    print(' ' * tabs + '->', data.title())

class CART:
    def __init__(self):
        self.tree = None
        self.target_values = None

    def calculate_gini(self, value_counts, col):
        Total_G = 0
        for row in np.unique(col):
            value = value_counts.loc[row, 'value_counts'] / value_counts.loc[row, 'value_counts'].sum()
            G_val = 1
            for _t in self.target_values:
                try:
                    # print(value.loc[_t])
                    G_val -= value.loc[_t] ** 2
                except:
                    pass
            Total_G += (col.value_counts().loc[row] / len(col)) * G_val
        return Total_G


    def calculate_root(self, X, y):
        GINI = {}
        for col in X.columns:
            value_counts = X.groupby([col, y]).size().to_frame(name = 'value_counts')
            GINI[col] = [self.calculate_gini(value_counts, X[col])]
        GINI = pd.DataFrame.from_dict(GINI, orient='index')
        min_val = GINI.min().values
        separate_on = GINI.idxmin().values
        return separate_on[0]

    def break_down(self, root, path, X, y):
        newX = X.loc[X[root] == path]
        options = newX.groupby([root, y]).size().to_frame(name = 'value_counts')
        newX = newX.drop([root], axis=1)
        if len(options.values) == 1:
            new_root = Node(options.index[0][1])
            return options.index[0][0], new_root
        else:
            new_root = self.calculate_root(newX, y)
            new_node = Node(new_root)
            for r in np.unique(newX.loc[:, new_root]):
                new_path, child = self.break_down(new_root, r, newX, y)
                new_node.add_child(new_path, child)
            return path, new_node

    def fit(self, X, y):
        self.target_values = np.unique(y)
        root = self.calculate_root(X, y)
        self.tree = Node(root)
        for r in np.unique(X.loc[:, root]):
            path, child = self.break_down(root, r, X, y)
            self.tree.add_child(path, child)
        self.tree.build_tree(0)
        

df = pd.read_csv('cartclass1.csv')
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
print('[INFO] * - Decision Node, | - Path, -> Leaf Node\n')
cart = CART()
cart.fit(X, y)