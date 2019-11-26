import open3d as o3d
import numpy as np
import plotly.graph_objects as go

file = "BabyHighRes.ply"

mesh = o3d.io.read_triangle_mesh(file)
pcd = o3d.io.read_point_cloud(file, format='xyzrgb')

colors_array = np.asarray(pcd.colors)
print("Shape of colors is: ", np.shape(colors_array))

triangles_array = np.asarray(mesh.triangles)
print("Shape of triangles is: ", np.shape(triangles_array))

vertices_array = np.asarray(mesh.vertices)
print("Shape of vertices is: ", np.shape(vertices_array))

length_total = np.shape(triangles_array)[0]

col_x = colors_array[:,0]
col_y = colors_array[:,1]
col_z = colors_array[:,2]

col_x = list(col_x)
col_y = list(col_y)
col_z = list(col_z)

vert_x = vertices_array[:,0]
vert_y = vertices_array[:,1]
vert_z = vertices_array[:,2]

vert_x = list(vert_x)
vert_y = list(vert_y)
vert_z = list(vert_z)

face_x = triangles_array[:,0]
face_y = triangles_array[:,1]
face_z = triangles_array[:,2]

face_x = list(face_x)
face_y = list(face_y)
face_z = list(face_z)

help(go.Mesh3d)

print(len(face_x),len(vert_x))
inte = [0.33 for i in range(len(face_x))]
inte = list(inte)

fig = go.Figure(data=[
    go.Mesh3d(
        x=vert_z,
        y=vert_x,
        z=vert_y,
        colorbar_title='intensity',
        #colorscale=[[0, 'gold'],
        #            [0.5, 'mediumturquoise'],
        #            [1, 'magenta']],
        # Intensity of each vertex, which will be interpolated and color-coded
        vertexcolor = colors_array,
        # i, j and k give the vertices of triangles

        # here we represent the 4 triangles of the tetrahedron surface
        i=face_z,
        j=face_x,
        k=face_y,
        name='y',
        showscale=True
    )
])
"""

fig = go.Figure(data=[
    go.Mesh3d(
        # Intensity of each vertex, which will be interpolated and color-coded
        # i, j and k give the vertices of triangles
        # here we represent the 4 triangles of the tetrahedron surface
        i=[0, 0, 0, 1],
        j=[1, 2, 3, 2],
        k=[2, 3, 1, 3],
        name='y',
        showscale=True
    )
])
"""
fig.show()

