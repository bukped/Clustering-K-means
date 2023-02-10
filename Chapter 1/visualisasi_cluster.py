# Memvisualkan hasil kluster dengan matplotlib
plt.figure
sct = plt.scatter(x_scaled[:, 1], x_scaled[:, 0], s=100,
                  c=dataset.cluster, marker="o", alpha=0.5)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 1], centers[:, 0], c='blue', s=200, alpha=0.5)
plt.title("Hasil Klustering Kedisiplinan K-Means")
plt.xlabel("Rendah")
plt.ylabel("Tinggi")
plt.show()

# Boxplot untuk memvisualisasikan Cluster dan Izin dengan seaborn dan matplotlib
sns.boxplot(x='cluster', y='Izin/cuti', data=dataset)
