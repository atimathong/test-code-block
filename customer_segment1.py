import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.metrics import silhouette_samples, silhouette_score
import warnings


def customer_segmentation(data):
    for col in data.select_dtypes(include=[object]):
        print(col, ":", data[col].unique())

    h = "Sex"
    pal = None
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))
    sns.scatterplot(x="Credit amount", y="Duration",
                    hue=h, palette=pal, data=data, ax=ax1)
    sns.scatterplot(x="Age", y="Credit amount", hue=h,
                    palette=pal, data=data, ax=ax2)
    sns.scatterplot(x="Age", y="Duration", hue=h,
                    palette=pal, data=data, ax=ax3)
    plt.tight_layout()

    # Selecting columns for clusterisation with k-means
    selected_cols = ["Age", "Credit amount", "Duration"]
    cluster_data = data.loc[:, selected_cols]
    cluster_log = np.log(cluster_data)
    scaler = StandardScaler()
    cluster_scaled = scaler.fit_transform(cluster_log)

    clusters_range = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    inertias = []

    for c in clusters_range:
        kmeans = KMeans(n_clusters=c, random_state=0).fit(cluster_scaled)
        inertias.append(kmeans.inertia_)

    plt.figure()
    plt.plot(clusters_range, inertias, marker='o')

    clusters_range = range(2,15)
    random_range = range(0,20)
    results =[]
    for c in clusters_range:
        for r in random_range:
            clusterer = KMeans(n_clusters=c, random_state=r)
            cluster_labels = clusterer.fit_predict(cluster_scaled)
            silhouette_avg = silhouette_score(cluster_scaled, cluster_labels)
            results.append([c,r,silhouette_avg])

    result = pd.DataFrame(results, columns=["n_clusters","seed","silhouette_score"])
    pivot_km = pd.pivot_table(result, index="n_clusters", columns="seed",values="silhouette_score")

    kmeans_sel = KMeans(n_clusters=3, random_state=1).fit(cluster_scaled)
    labels = pd.DataFrame(kmeans_sel.labels_)
    clustered_data = cluster_data.assign(Cluster=labels)

    data.groupby(by='loan_status')['loan_amnt'].describe()

