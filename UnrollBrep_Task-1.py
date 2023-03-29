import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th


unrolledSurfaces = []
unrolledPoints = []

for i, a, b, c, d in zip(brep, pointA, pointB, pointC, pointD):
    
    # INITIALIZE UNFOLDING
    unroll = rg.Unroller(i)
    
    # ADD CENTROIDS
    tempCentroids = []
    for face in i.Faces:
        centroid = rg.AreaMassProperties.Compute(face).Centroid
        tempCentroids.append(centroid)
        unroll.AddFollowingGeometry(centroid)
    
    # ADD POINTS
    unroll.AddFollowingGeometry(a)
    unroll.AddFollowingGeometry(b)
    unroll.AddFollowingGeometry(c)
    unroll.AddFollowingGeometry(d)
    
    # UNFOLD GEOMETRY
    unrolled = unroll.PerformUnroll()
    unrolledSurfaces.append(unrolled[0])
    unrolledPoints.append(unrolled[2])


unrolledSurfaces = th.list_to_tree(unrolledSurfaces)
unrolledPoints = th.list_to_tree(unrolledPoints)
