# Menambahkan kolom "kluster" dalam data frame ritel
dataset["cluster"] = kmeans.labels_
dataset.head()
