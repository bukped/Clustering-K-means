# Menentukan dan mengkonfigurasi fungsi kmeans, dan berapa cluster yang dinginkan
# n_clusters jumlah cluster yang diinginkan
kmeans = KMeans(n_clusters=3, random_state=123)

# Menentukan kluster dari data
kmeans.fit(x_scaled)

# Menampilkan pusat cluster
print(kmeans.cluster_centers_)

# Menampilkan hasil kluster
print(kmeans.labels_)