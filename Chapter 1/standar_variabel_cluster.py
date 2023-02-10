# Menstandarkan ukuran variabel cluster, dengan rescaling
# MinMaxScaler() digunakan untuk membuat rentangan data 0-1
# np.array() untuk membuat array
# scaler.fit_transform digunakan untuk training data dan scaling parameter data

scaler = MinMaxScaler()
x_array = np.array(dataset_x)
x_scaled = scaler.fit_transform(x_array)
x_scaled
