# import bhtsne
# import numpy as np
# m1 = [[10,20,10,20],[20,30,10,20]]
# m2 = [[15,25,10,20],[25,35,10,20],[10,20,10,20],[20,30,10,20]]
# data = np.concatenate((m1,m2), axis=0)
# # embedding_array = bhtsne.run_bh_tsne(data, initial_dims=data.shape[1])
# embedding_array = bhtsne.tsne(data.astype(np.float64))
# print(embedding_array)
# print(embedding_array.shape)

from bhtsne import tsne
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data.shape)

Y = tsne(iris.data)

print(Y.shape)
print(Y.dtype)

