import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
from math import pi


def mvp(nx,ny):
    res=np.array([[nx/2,0,0,(nx-1)/2],[0,ny/2,0,(ny-1)/2],[0,0,1,0],[0,0,0,1]])
    print("mvp",res)
    return res



def morth(l,b,n,r,t,f):
    res=np.array([
                    [2/(r-l),0,0,-((r+l)/(r-l))],
                    [0,2/(t-b),0,-((t+b)/(t-b))],
                    [0,0,2/(n-f),-((n+f)/(n-f))],
                    [0,0,0,1]])
    res2=np.array([
        [n,0,0,0],
        [0,n,0,0],
        [0,0,(n+f),-(f*n)],
        [0,0,1,0]])
    res=np.matmul(res,res2)
    print("morth",res)
    return res

def morth2(l,b,n,r,t,f,th,nx,ny):
    #t=np.tan(th/2)/abs(n)
    #b=-t
    #r=(nx/ny)*t
    #=-r
    res2=np.array([[n,0,0,0],[0,n,0,0],[0,0,n+f,-f*n],[0,0,1,0]])
    res=np.array([[2/(r-l),0,0,-(r+l)/(r-l)],[0,2/(t-b),0,-(t+b)/(t-b)],[0,0,2/(n-f),-(n+f)/(n-f)],[0,0,0,1]])
    res=res2*res
    print(res)
    #return res
    return np.array([[(2*n)/(r-l),0,(l+r)/(l-r),0],[0,(2*n)/(t-b),(b+t)/(b-t),0],[0,0,(f+n)/(n-f),(2*f*n)/(f-n)],[0,0,1,0]])

def cam(e,g,t):
    w=np.true_divide(-g,np.linalg.norm(g))
    u=np.true_divide(np.cross(t,w),np.linalg.norm(np.cross(t,w)))
    v=np.cross(w,u)
    #print(u)
    #print(v)
    #print(w)
    #print(e)
    res= np.concatenate((np.concatenate(([u],[v],[w],[[0,0,0]]),axis=0),np.array([[0,0,0,1]]).T),axis=1)
    res2=np.identity(4)
    res2[0][3]=-e[0]
    res2[1][3]=-e[1]
    res2[2][3]=-e[2]
    res=np.dot(res,res2)
    print("cam",res)
    #print(res2)
    return res

    #return np.concatenate([u,v,w,e],[0,0,0,1])

#print(mvp(100,80))

#print(morth(-2,0,-4,2,3,-8))

#cam(np.array([0,5,2]),np.array([0,-2,-5]),np.array([0,1,0]))
#print(cam(np.array([0,5,2]),np.array([0,-2,-5]),np.array([0,1,0])))

punto=np.array([[-1],[2],[-6],[1]])
matrizMVP=mvp(100,80)
matrizMORTH=morth(-2,0,-4,2,3,-8)
#matrizMORTH=morth2(-2,0,-4,2,3,-8,pi/3,100,80)
matrizCAM=cam(np.array([0,2,2]),np.array([0,-2,-5]),np.array([0,1,0]))

granMatriz=np.matmul(matrizMVP,matrizMORTH)
granMatriz=np.matmul(granMatriz,matrizCAM)
print("gran",granMatriz)




Puntos=np.array([
            [-1,1,1,-1],
            [2,2,0,0],
            [-6,-6,-6,-6],
            [1,1,1,1]
            ])
coor2D=np.matmul(granMatriz,Puntos)

Cm=np.array([
             [(coor2D[0][0]/coor2D[3][0]),(coor2D[0][1]/coor2D[3][1]),(coor2D[0][2]/coor2D[3][2]),(coor2D[0][3]/coor2D[3][3])],
             [(coor2D[1][0]/coor2D[3][0]),(coor2D[1][1]/coor2D[3][1]),(coor2D[1][2]/coor2D[3][2]),(coor2D[1][3]/coor2D[3][3])],
             [(coor2D[2][0]/coor2D[3][0]),(coor2D[2][1]/coor2D[3][1]),(coor2D[2][2]/coor2D[3][2]),(coor2D[2][3]/coor2D[3][3])],
             [(coor2D[3][0]/coor2D[3][0]),(coor2D[3][1]/coor2D[3][1]),(coor2D[3][2]/coor2D[3][2]),(coor2D[3][3]/coor2D[3][3])]
             ])


print("res",Cm)




verts = [
   (Cm[0][3],Cm[1][3]),  # right, bottom
   (Cm[0][0],Cm[1][0]),  # left, bottom
   (Cm[0][1],Cm[1][1]),  # left, top
   (Cm[0][2],Cm[1][2]),  # right, top
   
   (0., 0.),  # ignored
]

verts2 = [
   (0,0),  # left, bottom
   (0,80),  # left, top
   (100,80),  # right, top
   (100,0),  # right, bottom
   (0., 0.),  # ignored
]

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

path = Path(verts, codes)
path2 = Path(verts2, codes)

fig, ax = plt.subplots()
patch2 = patches.PathPatch(path2,facecolor='black',alpha=.1, lw=1)
patch = patches.PathPatch(path, facecolor='red', lw=2)
ax.add_patch(patch)
ax.add_patch(patch2)
ax.set_xlim(-50, 120)
ax.set_ylim(-50, 120)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

