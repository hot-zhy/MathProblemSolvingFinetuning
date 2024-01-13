"""
Using K-Means algorithm to classify math word problems
"""
import json
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from umap import UMAP
import re

data_path = '../../dataset/AAAI/TAL-SAQ6K-EN.jsonl'

# 1. data preparing
with open(data_path, 'r', encoding='utf-8') as file:
    data = [json.loads(line) for line in file]

patterns = r"Overseas Competition->Knowledge Point->|\['|'\]"


texts = [re.sub(patterns, '', str(item['knowledge_point_routes']))+item['problem']
         for item in data]

# 2. extract characteristics
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(texts)

# 3. apply K-Means
num_clusters = 14
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)
labels = kmeans.labels_

# 4. save results to different jsonl file
clustered_data = [[] for _ in range(num_clusters)]
for text, label in zip(data, labels):
    clustered_data[label].append(text)

for i, cluster in enumerate(clustered_data):
    with open(f'../classification/KMeans/KMeanscluster_{i}.jsonl', 'w', encoding='utf-8') as file:
        for item in cluster:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')

# 5. 使用UMAP进行降维，并绘制聚类结果
umap = UMAP(n_neighbors=8, min_dist=1, n_components=2, random_state=42)
reduced_X = umap.fit_transform(X.toarray())

plt.figure(figsize=(10, 8))
for i in range(num_clusters):
    points = reduced_X[labels == i]
    plt.scatter(points[:, 0], points[:, 1], label=f'Cluster {i}')

plt.title('K-Means Clustering of Math Questions with UMAP')
plt.xlabel('UMAP Feature 1')
plt.ylabel('UMAP Feature 2')
plt.legend()
plt.show()

# # 5. Using PCA to downscale to 2D and plotting clustering results
# pca = PCA(n_components=2)
# reduced_X = pca.fit_transform(X.toarray())

# plt.figure(figsize=(10, 8))
# for i in range(num_clusters):
#     points = reduced_X[labels == i]
#     plt.scatter(points[:, 0], points[:, 1], label=f'Cluster {i}')

# plt.title('K-Means Clustering of Math Questions')
# plt.xlabel('PCA Feature 1')
# plt.ylabel('PCA Feature 2')
# plt.legend()
# plt.show()
