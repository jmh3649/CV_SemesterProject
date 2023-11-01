import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "semester_project/dataset/PointClouds"
    pcd = o3d.io.read_point_cloud(path+"/490.pcd")
    #pcd = np.asarray(target.points)
    xyz = np.asarray(pcd.points)
    print(xyz)
    o3d.visualization.draw_geometries([pcd])
    downpcd = pcd.voxel_down_sample(voxel_size=5)
    #o3d.visualization.draw_geometries([downpcd])
    #LiDAR is mounted at the intersection
    cl, ind = downpcd.remove_statistical_outlier(nb_neighbors=20, std_ratio= 1.2)
    o3d.visualization.draw_geometries([cl])
    

    """labels = np.array(pcd.cluster_dbscan(eps=0.005, min_points=50))
    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcd], zoom=0.455,
                                    front=[-0.4999, -0.1659, -0.8499],
                                    lookat=[2.1813, 2.0619, 2.0999],
                                    up=[0.1204, -0.9852, 0.1215])
    """
main()