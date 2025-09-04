import pickle
import gzip
with open("similarity.pkl","rb") as f:
    data=pickle.load(f)
with
gzip.open("similarity_copressed.pkl.gz","wb") as f:
    pickle.dump(data,f)
print("File compressed successfully! Upload similarity_compressed.pkl.gz to github")
