# info() digunakan untuk melihat jumlah kolom, tipe data, dsb
dataset.info()

# describe() digunakan untuk melihat data statistik pada file
dataset.describe()

# null digunakan untuk melihat ada data yang kosong atau tidak
dataset_null = round(100*(dataset.isnull().sum())/len(dataset), 2)
dataset_null
