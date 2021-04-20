import vtk


colors = vtk.vtkNamedColors()
# source
cube1 = vtk.vtkCubeSource()
cube1.SetXLength(30)
cube1.SetYLength(30)
cube1.SetZLength(30)
cube1.Update()

cube2 = vtk.vtkCubeSource()
cube2.SetXLength(10)
cube2.SetYLength(20)
cube2.SetZLength(3)
cube2.Update()

cube3 = vtk.vtkCubeSource()
cube3.SetXLength(2)
cube3.SetYLength(10)
cube3.SetZLength(20)
cube3.Update()

sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0.0, 0.0, 0.0)
sphereSource.SetRadius(1)

cono = vtk.vtkConeSource()
cono.SetCenter(0.0, 0.0, 0.0)
cono.SetResolution(51)
cono.SetRadius(25)
cono.SetHeight(30)
cono.SetDirection(0, 1, 0)

marcoVSource = vtk.vtkCubeSource()
marcoVSource.SetXLength(2.1)
marcoVSource.SetYLength(1)
marcoVSource.SetZLength(20)
marcoVSource.Update()

marcoHSource = vtk.vtkCubeSource()
marcoHSource.SetXLength(2.1)
marcoHSource.SetYLength(10)
marcoHSource.SetZLength(1)
marcoHSource.Update()


chimenea1Source = vtk.vtkCylinderSource()
chimenea1Source.SetCenter(0.0, 0.0, 0.0)
chimenea1Source.SetRadius(1.0)
chimenea1Source.SetHeight(20.0)
chimenea1Source.SetResolution(30)


chimenea2Source = vtk.vtkConeSource()
chimenea2Source.SetCenter(0.0, 0.0, 0.0)
chimenea2Source.SetResolution(51)
chimenea2Source.SetRadius(2)
chimenea2Source.SetHeight(3)
chimenea2Source.SetDirection(0, 1, 0)

ladrillo1Source = vtk.vtkCubeSource()
ladrillo1Source.SetXLength(2)
ladrillo1Source.SetYLength(0.5)
ladrillo1Source.SetZLength(1)
ladrillo1Source.Update()

ladrillo2Source = vtk.vtkCubeSource()
ladrillo2Source.SetXLength(1)
ladrillo2Source.SetYLength(0.5)
ladrillo2Source.SetZLength(2)
ladrillo2Source.Update()


# techo

points = vtk.vtkPoints()

p0 = [20.0, -30.0, 20.0]
p1 = [-20.0, -30.0, 20.0]
p2 = [-20.0, -30.0, -20.0]
p3 = [20.0, -30.0, -20.0]
p4 = [0.0, 0.0, 0.0]

points.InsertNextPoint(p0)
points.InsertNextPoint(p1)
points.InsertNextPoint(p2)
points.InsertNextPoint(p3)
points.InsertNextPoint(p4)

pyramid = vtk.vtkPyramid()
pyramid.GetPointIds().SetId(0, 0)
pyramid.GetPointIds().SetId(1, 1)
pyramid.GetPointIds().SetId(2, 2)
pyramid.GetPointIds().SetId(3, 3)
pyramid.GetPointIds().SetId(4, 4)

cells = vtk.vtkCellArray()
cells.InsertNextCell(pyramid)

ug = vtk.vtkUnstructuredGrid()
ug.SetPoints(points)
ug.InsertNextCell(pyramid.GetCellType(), pyramid.GetPointIds())

# end techo

troncoSource = vtk.vtkCylinderSource()
troncoSource.SetCenter(0.0, 0.0, 0.0)
troncoSource.SetRadius(3.0)
troncoSource.SetHeight(50.0)
troncoSource.SetResolution(100)

# ramitaSource=vtk.vtkCylinderSource()
#ramitaSource.SetCenter(0.0, 0.0, 0.0)
# ramitaSource.SetRadius(0.5)
# ramitaSource.SetHeight(4.0)
# ramitaSource.SetDirection(1,1,1)

hojasSource1 = vtk.vtkSphereSource()
hojasSource1.SetCenter(0.0, 0.0, 0.0)
hojasSource1.SetRadius(10)


hojasSource4 = vtk.vtkSphereSource()
hojasSource4.SetCenter(0.0, 0.0, 0.0)
hojasSource4.SetRadius(13)


hojasSource6 = vtk.vtkSphereSource()
hojasSource6.SetCenter(0.0, 0.0, 0.0)
hojasSource6.SetRadius(15)

hojaArbusto1 = vtk.vtkSphereSource()
hojaArbusto1.SetCenter(0.0, 0.0, 0.0)
hojaArbusto1.SetRadius(5)

hojaArbusto2 = vtk.vtkSphereSource()
hojaArbusto2.SetCenter(0.0, 0.0, 0.0)
hojaArbusto2.SetRadius(5)

hojaArbusto3 = vtk.vtkSphereSource()
hojaArbusto3.SetCenter(0.0, 0.0, 0.0)
hojaArbusto3.SetRadius(5)

hojaArbusto4 = vtk.vtkSphereSource()
hojaArbusto4.SetCenter(0.0, 0.0, 0.0)
hojaArbusto4.SetRadius(5)

hojaArbusto5 = vtk.vtkSphereSource()
hojaArbusto5.SetCenter(0.0, 0.0, 0.0)
hojaArbusto5.SetRadius(5)

# luna
luna = vtk.vtkSphereSource()
luna.SetCenter(0.0, 0.0, 0.0)
luna.SetPhiResolution(20)
luna.SetThetaResolution(20)
# luna.Update()
luna.SetRadius(15)

# arbusto2
hoja2Arbusto1 = vtk.vtkSphereSource()
hoja2Arbusto1.SetCenter(0.0, 0.0, 0.0)
hoja2Arbusto1.SetRadius(5)

hoja2Arbusto2 = vtk.vtkSphereSource()
hoja2Arbusto2.SetCenter(0.0, 0.0, 0.0)
hoja2Arbusto2.SetRadius(5)

hoja2Arbusto3 = vtk.vtkSphereSource()
hoja2Arbusto3.SetCenter(0.0, 0.0, 0.0)
hoja2Arbusto3.SetRadius(5)

hoja2Arbusto4 = vtk.vtkSphereSource()
hoja2Arbusto4.SetCenter(0.0, 0.0, 0.0)
hoja2Arbusto4.SetRadius(5)

hoja2Arbusto5 = vtk.vtkSphereSource()
hoja2Arbusto5.SetCenter(0.0, 0.0, 0.0)
hoja2Arbusto5.SetRadius(5)


# arbusto3
hoja3Arbusto1 = vtk.vtkSphereSource()
hoja3Arbusto1.SetCenter(0.0, 0.0, 0.0)
hoja3Arbusto1.SetRadius(5)

hoja3Arbusto2 = vtk.vtkSphereSource()
hoja3Arbusto2.SetCenter(0.0, 0.0, 0.0)
hoja3Arbusto2.SetRadius(5)

hoja3Arbusto3 = vtk.vtkSphereSource()
hoja3Arbusto3.SetCenter(0.0, 0.0, 0.0)
hoja3Arbusto3.SetRadius(5)

hoja3Arbusto4 = vtk.vtkSphereSource()
hoja3Arbusto4.SetCenter(0.0, 0.0, 0.0)
hoja3Arbusto4.SetRadius(5)

hoja3Arbusto5 = vtk.vtkSphereSource()
hoja3Arbusto5.SetCenter(0.0, 0.0, 0.0)
hoja3Arbusto5.SetRadius(5)


# arbusto4
hoja4Arbusto1 = vtk.vtkSphereSource()
hoja4Arbusto1.SetCenter(0.0, 0.0, 0.0)
hoja4Arbusto1.SetRadius(5)

hoja4Arbusto2 = vtk.vtkSphereSource()
hoja4Arbusto2.SetCenter(0.0, 0.0, 0.0)
hoja4Arbusto2.SetRadius(5)

hoja4Arbusto3 = vtk.vtkSphereSource()
hoja4Arbusto3.SetCenter(0.0, 0.0, 0.0)
hoja4Arbusto3.SetRadius(5)

hoja4Arbusto4 = vtk.vtkSphereSource()
hoja4Arbusto4.SetCenter(0.0, 0.0, 0.0)
hoja4Arbusto4.SetRadius(5)

hoja4Arbusto5 = vtk.vtkSphereSource()
hoja4Arbusto5.SetCenter(0.0, 0.0, 0.0)
hoja4Arbusto5.SetRadius(5)

# arbusto5
hoja5Arbusto1 = vtk.vtkSphereSource()
hoja5Arbusto1.SetCenter(0.0, 0.0, 0.0)
hoja5Arbusto1.SetRadius(5)

hoja5Arbusto2 = vtk.vtkSphereSource()
hoja5Arbusto2.SetCenter(0.0, 0.0, 0.0)
hoja5Arbusto2.SetRadius(5)

hoja5Arbusto3 = vtk.vtkSphereSource()
hoja5Arbusto3.SetCenter(0.0, 0.0, 0.0)
hoja5Arbusto3.SetRadius(5)

hoja5Arbusto4 = vtk.vtkSphereSource()
hoja5Arbusto4.SetCenter(0.0, 0.0, 0.0)
hoja5Arbusto4.SetRadius(5)

hoja5Arbusto5 = vtk.vtkSphereSource()
hoja5Arbusto5.SetCenter(0.0, 0.0, 0.0)
hoja5Arbusto5.SetRadius(5)

# nube1
porcion0Nube1 = vtk.vtkSphereSource()
porcion0Nube1.SetCenter(0.0, 0.0, 0.0)
porcion0Nube1.SetRadius(7)

porcion1Nube1 = vtk.vtkSphereSource()
porcion1Nube1.SetCenter(0.0, 0.0, 0.0)
porcion1Nube1.SetRadius(7)

porcion2Nube1 = vtk.vtkSphereSource()
porcion2Nube1.SetCenter(0.0, 0.0, 0.0)
porcion2Nube1.SetRadius(7)

porcion3Nube1 = vtk.vtkSphereSource()
porcion3Nube1.SetCenter(0.0, 0.0, 0.0)
porcion3Nube1.SetRadius(7)

porcion4Nube1 = vtk.vtkSphereSource()
porcion4Nube1.SetCenter(0.0, 0.0, 0.0)
porcion4Nube1.SetRadius(7)

porcion5Nube1 = vtk.vtkSphereSource()
porcion5Nube1.SetCenter(0.0, 0.0, 0.0)
porcion5Nube1.SetRadius(7)

# suelo
suelo = vtk.vtkCubeSource()
suelo.SetXLength(150)
suelo.SetYLength(10)
suelo.SetZLength(150)
suelo.Update()

# mapper
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(cube1.GetOutput())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(cube2.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(cube3.GetOutput())

sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

conoMapper = vtk.vtkPolyDataMapper()
conoMapper.SetInputConnection(cono.GetOutputPort())

troncoMapper = vtk.vtkPolyDataMapper()
troncoMapper.SetInputConnection(troncoSource.GetOutputPort())


hojasMapper1 = vtk.vtkPolyDataMapper()
hojasMapper1.SetInputConnection(hojasSource1.GetOutputPort())


hojasMapper4 = vtk.vtkPolyDataMapper()
hojasMapper4.SetInputConnection(hojasSource4.GetOutputPort())


hojasMapper6 = vtk.vtkPolyDataMapper()
hojasMapper6.SetInputConnection(hojasSource6.GetOutputPort())

# arbusto

arbustMapper1 = vtk.vtkPolyDataMapper()
arbustMapper1.SetInputConnection(hojaArbusto1.GetOutputPort())

arbustMapper2 = vtk.vtkPolyDataMapper()
arbustMapper2.SetInputConnection(hojaArbusto2.GetOutputPort())

arbustMapper3 = vtk.vtkPolyDataMapper()
arbustMapper3.SetInputConnection(hojaArbusto3.GetOutputPort())

arbustMapper4 = vtk.vtkPolyDataMapper()
arbustMapper4.SetInputConnection(hojaArbusto4.GetOutputPort())

arbustMapper5 = vtk.vtkPolyDataMapper()
arbustMapper5.SetInputConnection(hojaArbusto5.GetOutputPort())

# luna
lunaMapper = vtk.vtkPolyDataMapper()
lunaMapper.SetInputConnection(luna.GetOutputPort())


# arbusto2
arbust2Mapper1 = vtk.vtkPolyDataMapper()
arbust2Mapper1.SetInputConnection(hoja2Arbusto1.GetOutputPort())

arbust2Mapper2 = vtk.vtkPolyDataMapper()
arbust2Mapper2.SetInputConnection(hoja2Arbusto2.GetOutputPort())

arbust2Mapper3 = vtk.vtkPolyDataMapper()
arbust2Mapper3.SetInputConnection(hoja2Arbusto3.GetOutputPort())

arbust2Mapper4 = vtk.vtkPolyDataMapper()
arbust2Mapper4.SetInputConnection(hoja2Arbusto4.GetOutputPort())

arbust2Mapper5 = vtk.vtkPolyDataMapper()
arbust2Mapper5.SetInputConnection(hoja2Arbusto5.GetOutputPort())

# arbusto3
arbust3Mapper1 = vtk.vtkPolyDataMapper()
arbust3Mapper1.SetInputConnection(hoja3Arbusto1.GetOutputPort())

arbust3Mapper2 = vtk.vtkPolyDataMapper()
arbust3Mapper2.SetInputConnection(hoja3Arbusto2.GetOutputPort())

arbust3Mapper3 = vtk.vtkPolyDataMapper()
arbust3Mapper3.SetInputConnection(hoja3Arbusto3.GetOutputPort())

arbust3Mapper4 = vtk.vtkPolyDataMapper()
arbust3Mapper4.SetInputConnection(hoja3Arbusto4.GetOutputPort())

arbust3Mapper5 = vtk.vtkPolyDataMapper()
arbust3Mapper5.SetInputConnection(hoja3Arbusto5.GetOutputPort())

# arbusto4
arbust4Mapper1 = vtk.vtkPolyDataMapper()
arbust4Mapper1.SetInputConnection(hoja4Arbusto1.GetOutputPort())

arbust4Mapper2 = vtk.vtkPolyDataMapper()
arbust4Mapper2.SetInputConnection(hoja4Arbusto2.GetOutputPort())

arbust4Mapper3 = vtk.vtkPolyDataMapper()
arbust4Mapper3.SetInputConnection(hoja4Arbusto3.GetOutputPort())

arbust4Mapper4 = vtk.vtkPolyDataMapper()
arbust4Mapper4.SetInputConnection(hoja4Arbusto4.GetOutputPort())

arbust4Mapper5 = vtk.vtkPolyDataMapper()
arbust4Mapper5.SetInputConnection(hoja4Arbusto5.GetOutputPort())

# arbusto5
arbust5Mapper1 = vtk.vtkPolyDataMapper()
arbust5Mapper1.SetInputConnection(hoja5Arbusto1.GetOutputPort())

arbust5Mapper2 = vtk.vtkPolyDataMapper()
arbust5Mapper2.SetInputConnection(hoja5Arbusto2.GetOutputPort())

arbust5Mapper3 = vtk.vtkPolyDataMapper()
arbust5Mapper3.SetInputConnection(hoja5Arbusto3.GetOutputPort())

arbust5Mapper4 = vtk.vtkPolyDataMapper()
arbust5Mapper4.SetInputConnection(hoja5Arbusto4.GetOutputPort())

arbust5Mapper5 = vtk.vtkPolyDataMapper()
arbust5Mapper5.SetInputConnection(hoja5Arbusto5.GetOutputPort())

# nube1
nube0Mapper1 = vtk.vtkPolyDataMapper()
nube0Mapper1.SetInputConnection(porcion0Nube1.GetOutputPort())

nube1Mapper1 = vtk.vtkPolyDataMapper()
nube1Mapper1.SetInputConnection(porcion1Nube1.GetOutputPort())

nube2Mapper1 = vtk.vtkPolyDataMapper()
nube2Mapper1.SetInputConnection(porcion2Nube1.GetOutputPort())

nube3Mapper1 = vtk.vtkPolyDataMapper()
nube3Mapper1.SetInputConnection(porcion3Nube1.GetOutputPort())

nube4Mapper1 = vtk.vtkPolyDataMapper()
nube4Mapper1.SetInputConnection(porcion4Nube1.GetOutputPort())

nube5Mapper1 = vtk.vtkPolyDataMapper()
nube5Mapper1.SetInputConnection(porcion5Nube1.GetOutputPort())

# suelo
sueloMaper = vtk.vtkPolyDataMapper()
sueloMaper.SetInputData(suelo.GetOutput())

# ramitaMapper=vtk.vtkPolyDataMapper()
# ramitaMapper=SetInputConnection(ramitaMapper.GetOutputPort())


techoMapper = vtk.vtkDataSetMapper()
techoMapper.SetInputData(ug)

marcoHMapper = vtk.vtkPolyDataMapper()
marcoHMapper.SetInputData(marcoHSource.GetOutput())

marcoVMapper = vtk.vtkPolyDataMapper()
marcoVMapper.SetInputData(marcoVSource.GetOutput())

chimenea1Mapper = vtk.vtkPolyDataMapper()
chimenea1Mapper.SetInputConnection(chimenea1Source.GetOutputPort())

chimenea2Mapper = vtk.vtkPolyDataMapper()
chimenea2Mapper.SetInputConnection(chimenea2Source.GetOutputPort())

ladrillo1Mapper = vtk.vtkPolyDataMapper()
ladrillo1Mapper.SetInputData(ladrillo1Source.GetOutput())

ladrillo2Mapper = vtk.vtkPolyDataMapper()
ladrillo2Mapper.SetInputData(ladrillo2Source.GetOutput())


# actor
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(211/255, 196/255, 103/255)
actor1.SetPosition(0, 15, 0)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(160/255, 100/255, 27/255)
actor2.SetPosition(0, 10, 15)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(200/255, 229/255, 235/255)
actor3.SetPosition(-15, 15, 0)

sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)
sphereActor.GetProperty().SetColor(7/255, 92/255, 187/255)
sphereActor.SetPosition(-3, 10, 16)

conoActor = vtk.vtkActor()
conoActor.SetMapper(conoMapper)
conoActor.GetProperty().SetColor(168/255, 106/255, 29/255)
conoActor.SetPosition(0, 45, 0)

troncoActor = vtk.vtkActor()
troncoActor.SetMapper(troncoMapper)
troncoActor.GetProperty().SetColor(96/255, 50/255, 35/255)
troncoActor.SetPosition(30, 25, 0)

hojasActor1 = vtk.vtkActor()
hojasActor1.SetMapper(hojasMapper1)
hojasActor1.GetProperty().SetColor(12/255, 141/255, 119/255)
hojasActor1.SetPosition(30, 50, 5)

hojasActor2 = vtk.vtkActor()
hojasActor2.SetMapper(hojasMapper1)
hojasActor2.GetProperty().SetColor(110/255, 189/255, 131/255)
hojasActor2.SetPosition(30, 50, -5)

hojasActor3 = vtk.vtkActor()
hojasActor3.SetMapper(hojasMapper1)
hojasActor3.GetProperty().SetColor(12/255, 141/255, 119/255)
hojasActor3.SetPosition(35, 50, 0)

hojasActor4 = vtk.vtkActor()
hojasActor4.SetMapper(hojasMapper4)
hojasActor4.GetProperty().SetColor(11/255, 94/255, 86/255)
hojasActor4.SetPosition(35, 60, 5)

hojasActor5 = vtk.vtkActor()
hojasActor5.SetMapper(hojasMapper4)
hojasActor5.GetProperty().SetColor(103/255, 156/255, 138/255)
hojasActor5.SetPosition(35, 60, -5)

hojasActor6 = vtk.vtkActor()
hojasActor6.SetMapper(hojasMapper6)
hojasActor6.GetProperty().SetColor(110/255, 189/255, 131/255)
hojasActor6.SetPosition(25, 60, -5)

hojasActor7 = vtk.vtkActor()
hojasActor7.SetMapper(hojasMapper4)
hojasActor7.GetProperty().SetColor(12/255, 141/255, 119/255)
hojasActor7.SetPosition(30, 75, 0)

arbustoActor1 = vtk.vtkActor()
arbustoActor1.SetMapper(arbustMapper1)
arbustoActor1.GetProperty().SetColor(12/255, 141/255, 119/255)
arbustoActor1.SetPosition(-19, 0, 0)

arbustoActor2 = vtk.vtkActor()
arbustoActor2.SetMapper(arbustMapper2)
arbustoActor2.GetProperty().SetColor(12/255, 141/255, 119/255)
arbustoActor2.SetPosition(-21, 0, 0)

arbustoActor3 = vtk.vtkActor()
arbustoActor3.SetMapper(arbustMapper3)
arbustoActor3.GetProperty().SetColor(12/255, 141/255, 119/255)
arbustoActor3.SetPosition(-24, 3, 0)

arbustoActor4 = vtk.vtkActor()
arbustoActor4.SetMapper(arbustMapper4)
arbustoActor4.GetProperty().SetColor(12/255, 141/255, 119/255)
arbustoActor4.SetPosition(-26, 3, 0)

arbustoActor5 = vtk.vtkActor()
arbustoActor5.SetMapper(arbustMapper5)
arbustoActor5.GetProperty().SetColor(12/255, 141/255, 119/255)
arbustoActor5.SetPosition(-28, 0, 0)

# luna
lunaActor = vtk.vtkActor()
lunaActor.SetMapper(lunaMapper)
lunaActor.GetProperty().SetColor(169/255, 169/255, 169/255)
# lunaActor.GetProperty().SetDiffuseColor(colors.GetColor3d("DarkGreen"))
# lunaActor.GetProperty().SetOpacity(0.5)
lunaActor.SetPosition(0, 150, 0)

# lunaActor.SetMapper(lunaMapper)
# arbusto2
arbusto2Actor1 = vtk.vtkActor()
arbusto2Actor1.SetMapper(arbust2Mapper1)
arbusto2Actor1.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto2Actor1.SetPosition(-38, 0, 19)

arbusto2Actor2 = vtk.vtkActor()
arbusto2Actor2.SetMapper(arbust2Mapper2)
arbusto2Actor2.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto2Actor2.SetPosition(-40, 4, 29)

arbusto2Actor3 = vtk.vtkActor()
arbusto2Actor3.SetMapper(arbust2Mapper3)
arbusto2Actor3.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto2Actor3.SetPosition(-43, 4, 21)

arbusto2Actor4 = vtk.vtkActor()
arbusto2Actor4.SetMapper(arbust2Mapper4)
arbusto2Actor4.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto2Actor4.SetPosition(-46, 0, 23)

arbusto2Actor5 = vtk.vtkActor()
arbusto2Actor5.SetMapper(arbust2Mapper5)
arbusto2Actor5.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto2Actor5.SetPosition(-48, 0, 26)

# arbusto3
arbusto3Actor1 = vtk.vtkActor()
arbusto3Actor1.SetMapper(arbust2Mapper1)
arbusto3Actor1.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto3Actor1.SetPosition(38, 0, 19)

arbusto3Actor2 = vtk.vtkActor()
arbusto3Actor2.SetMapper(arbust2Mapper2)
arbusto3Actor2.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto3Actor2.SetPosition(40, 4, 29)

arbusto3Actor3 = vtk.vtkActor()
arbusto3Actor3.SetMapper(arbust2Mapper3)
arbusto3Actor3.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto3Actor3.SetPosition(43, 4, 21)

arbusto3Actor4 = vtk.vtkActor()
arbusto3Actor4.SetMapper(arbust2Mapper4)
arbusto3Actor4.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto3Actor4.SetPosition(46, 0, 23)

arbusto3Actor5 = vtk.vtkActor()
arbusto3Actor5.SetMapper(arbust2Mapper5)
arbusto3Actor5.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto3Actor5.SetPosition(48, 0, 26)

# arbusto4
arbusto4Actor1 = vtk.vtkActor()
arbusto4Actor1.SetMapper(arbust2Mapper1)
arbusto4Actor1.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto4Actor1.SetPosition(-38, 0, -19)

arbusto4Actor2 = vtk.vtkActor()
arbusto4Actor2.SetMapper(arbust2Mapper2)
arbusto4Actor2.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto4Actor2.SetPosition(-40, 4, -29)

arbusto4Actor3 = vtk.vtkActor()
arbusto4Actor3.SetMapper(arbust2Mapper3)
arbusto4Actor3.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto4Actor3.SetPosition(-43, 4, -21)

arbusto4Actor4 = vtk.vtkActor()
arbusto4Actor4.SetMapper(arbust2Mapper4)
arbusto4Actor4.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto4Actor4.SetPosition(-46, 0, -23)

arbusto4Actor5 = vtk.vtkActor()
arbusto4Actor5.SetMapper(arbust2Mapper5)
arbusto4Actor5.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto4Actor5.SetPosition(-48, 0, -26)

# arbusto5
arbusto5Actor1 = vtk.vtkActor()
arbusto5Actor1.SetMapper(arbust2Mapper1)
arbusto5Actor1.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto5Actor1.SetPosition(19, 0, 38)

arbusto5Actor2 = vtk.vtkActor()
arbusto5Actor2.SetMapper(arbust2Mapper2)
arbusto5Actor2.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto5Actor2.SetPosition(29, 4, 40)

arbusto5Actor3 = vtk.vtkActor()
arbusto5Actor3.SetMapper(arbust2Mapper3)
arbusto5Actor3.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto5Actor3.SetPosition(21, 4, 43)

arbusto5Actor4 = vtk.vtkActor()
arbusto5Actor4.SetMapper(arbust2Mapper4)
arbusto5Actor4.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto5Actor4.SetPosition(23, 0, 46)

arbusto5Actor5 = vtk.vtkActor()
arbusto5Actor5.SetMapper(arbust2Mapper5)
arbusto5Actor5.GetProperty().SetColor(12/255, 141/255, 119/255)
arbusto5Actor5.SetPosition(26, 0, 48)

# nubes 0  255  255
nube0Actor1 = vtk.vtkActor()
nube0Actor1.SetMapper(nube0Mapper1)
nube0Actor1.GetProperty().SetColor(0/255, 225/255, 255/255)
nube0Actor1.GetProperty().SetOpacity(0.1)
nube0Actor1.SetPosition(-30, 80, 15)

nube1Actor1 = vtk.vtkActor()
nube1Actor1.SetMapper(nube1Mapper1)
nube1Actor1.GetProperty().SetColor(0/255, 225/255, 255/255)
nube1Actor1.GetProperty().SetOpacity(0.1)
nube1Actor1.SetPosition(-32, 82, 15)

nube2Actor1 = vtk.vtkActor()
nube2Actor1.SetMapper(nube2Mapper1)
nube2Actor1.GetProperty().SetColor(0/255, 225/255, 255/255)
nube2Actor1.GetProperty().SetOpacity(0.1)
nube2Actor1.SetPosition(-35, 82, 15)

nube3Actor1 = vtk.vtkActor()
nube3Actor1.SetMapper(nube3Mapper1)
nube3Actor1.GetProperty().SetColor(0/255, 225/255, 255/255)
nube3Actor1.GetProperty().SetOpacity(0.1)
nube3Actor1.SetPosition(-37, 80, 15)

nube4Actor1 = vtk.vtkActor()
nube4Actor1.SetMapper(nube4Mapper1)
nube4Actor1.GetProperty().SetColor(0/255, 225/255, 255/255)
nube4Actor1.GetProperty().SetOpacity(0.1)
nube4Actor1.SetPosition(-37, 82, 17)

nube5Actor1 = vtk.vtkActor()
nube5Actor1.SetMapper(nube5Mapper1)
nube5Actor1.GetProperty().SetColor(0/255, 225/255, 255/255)
nube5Actor1.GetProperty().SetOpacity(0.1)
nube5Actor1.SetPosition(-39, 82, 17)
# suelo
sueloActor = vtk.vtkActor()
sueloActor.SetMapper(sueloMaper)
sueloActor.GetProperty().SetColor(46/255, 139/255, 87/255)
sueloActor.SetPosition(0, -7, 0)

# ramitaActor1=vtk.vtkActor()
# ramitaActor1.SetMapper(ramitaMapper)
#ramitaActor1.GetProperty().SetColor(110/255, 189/255, 131/255)
# hojasActor7.SetPosition(30,75,0)

techoActor = vtk.vtkActor()
techoActor.SetMapper(techoMapper)
techoActor.GetProperty().SetColor(168/255, 106/255, 29/255)
techoActor.SetPosition(0, 60, 0)

marcoH1Actor = vtk.vtkActor()
marcoH1Actor.SetMapper(marcoHMapper)
marcoH1Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoH1Actor.SetPosition(-15, 15, 10)

marcoH2Actor = vtk.vtkActor()
marcoH2Actor.SetMapper(marcoHMapper)
marcoH2Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoH2Actor.SetPosition(-15, 15, -10)

marcoH3Actor = vtk.vtkActor()
marcoH3Actor.SetMapper(marcoHMapper)
marcoH3Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoH3Actor.SetPosition(-15, 15, 0)


marcoH1Actor = vtk.vtkActor()
marcoH1Actor.SetMapper(marcoHMapper)
marcoH1Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoH1Actor.SetPosition(-15, 15, 10)

marcoH2Actor = vtk.vtkActor()
marcoH2Actor.SetMapper(marcoHMapper)
marcoH2Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoH2Actor.SetPosition(-15, 15, -10)

marcoV1Actor = vtk.vtkActor()
marcoV1Actor.SetMapper(marcoVMapper)
marcoV1Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoV1Actor.SetPosition(-15, 15, 0)

marcoV2Actor = vtk.vtkActor()
marcoV2Actor.SetMapper(marcoVMapper)
marcoV2Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoV2Actor.SetPosition(-15, 20, 0)

marcoV3Actor = vtk.vtkActor()
marcoV3Actor.SetMapper(marcoVMapper)
marcoV3Actor.GetProperty().SetColor(96/255, 50/255, 35/255)
marcoV3Actor.SetPosition(-15, 10, 0)

chimenea1Actor = vtk.vtkActor()
chimenea1Actor.SetMapper(chimenea1Mapper)
chimenea1Actor.GetProperty().SetColor(165/255, 165/255, 165/255)
chimenea1Actor.SetPosition(-13, 40, -6)

chimenea2Actor = vtk.vtkActor()
chimenea2Actor.SetMapper(chimenea2Mapper)
chimenea2Actor.GetProperty().SetColor(165/255, 165/255, 165/255)
chimenea2Actor.SetPosition(-13, 52, -6)


ladrillo1Actor = vtk.vtkActor()
ladrillo1Actor.SetMapper(ladrillo1Mapper)
ladrillo1Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo1Actor.SetPosition(14.0001, 10, 14.501)

ladrillo2Actor = vtk.vtkActor()
ladrillo2Actor.SetMapper(ladrillo2Mapper)
ladrillo2Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo2Actor.SetPosition(14.5001, 10.8, 14.001)

ladrillo3Actor = vtk.vtkActor()
ladrillo3Actor.SetMapper(ladrillo2Mapper)
ladrillo3Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo3Actor.SetPosition(14.5001, 9.2, 14.001)

ladrillo4Actor = vtk.vtkActor()
ladrillo4Actor.SetMapper(ladrillo2Mapper)
ladrillo4Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo4Actor.SetPosition(14.5001, 10, 12.201)

ladrillo5Actor = vtk.vtkActor()
ladrillo5Actor.SetMapper(ladrillo1Mapper)
ladrillo5Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo5Actor.SetPosition(12.2001, 9.2, 14.501)

ladrillo6Actor = vtk.vtkActor()
ladrillo6Actor.SetMapper(ladrillo1Mapper)
ladrillo6Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo6Actor.SetPosition(14.0001, 8.4, 14.501)

ladrillo7Actor = vtk.vtkActor()
ladrillo7Actor.SetMapper(ladrillo2Mapper)
ladrillo7Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo7Actor.SetPosition(14.5001, 7.6, 14.001)

ladrillo8Actor = vtk.vtkActor()
ladrillo8Actor.SetMapper(ladrillo2Mapper)
ladrillo8Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo8Actor.SetPosition(14.5001, 8.4, 12.201)

ladrillo9Actor = vtk.vtkActor()
ladrillo9Actor.SetMapper(ladrillo1Mapper)
ladrillo9Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo9Actor.SetPosition(12.2001, 7.6, 14.501)

ladrillo10Actor = vtk.vtkActor()
ladrillo10Actor.SetMapper(ladrillo1Mapper)
ladrillo10Actor.GetProperty().SetColor(201/255, 60/255, 32/255)
ladrillo10Actor.SetPosition(14.0001, 6.8, 14.501)


# axes
transform = vtk.vtkTransform()
transform.Translate(0.0, 0.0, 0.0)
axes = vtk.vtkAxesActor()
axes.SetTotalLength(50, 50, 50)
axes.SetUserTransform(transform)

# renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(axes)
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(sphereActor)
# renderer.AddActor(conoActor)
renderer.AddActor(troncoActor)
renderer.AddActor(hojasActor1)
renderer.AddActor(hojasActor2)
renderer.AddActor(hojasActor3)
renderer.AddActor(hojasActor4)
renderer.AddActor(hojasActor5)
renderer.AddActor(hojasActor6)
renderer.AddActor(hojasActor7)
# arbusto1
renderer.AddActor(arbustoActor1)
renderer.AddActor(arbustoActor2)
renderer.AddActor(arbustoActor3)
renderer.AddActor(arbustoActor4)
renderer.AddActor(arbustoActor5)
# luna
renderer.AddActor(lunaActor)

# arbusto2
renderer.AddActor(arbusto2Actor1)
renderer.AddActor(arbusto2Actor2)
renderer.AddActor(arbusto2Actor3)
renderer.AddActor(arbusto2Actor4)
renderer.AddActor(arbusto2Actor5)

# arbusto3
renderer.AddActor(arbusto3Actor1)
renderer.AddActor(arbusto3Actor2)
renderer.AddActor(arbusto3Actor3)
renderer.AddActor(arbusto3Actor4)
renderer.AddActor(arbusto3Actor5)
# arbusto4
renderer.AddActor(arbusto4Actor1)
renderer.AddActor(arbusto4Actor2)
renderer.AddActor(arbusto4Actor3)
renderer.AddActor(arbusto4Actor4)
renderer.AddActor(arbusto4Actor5)
# arbusto5
renderer.AddActor(arbusto5Actor1)
renderer.AddActor(arbusto5Actor2)
renderer.AddActor(arbusto5Actor3)
renderer.AddActor(arbusto5Actor4)
renderer.AddActor(arbusto5Actor5)
# nube1
renderer.AddActor(nube0Actor1)
renderer.AddActor(nube1Actor1)
renderer.AddActor(nube2Actor1)
renderer.AddActor(nube3Actor1)
renderer.AddActor(nube4Actor1)
renderer.AddActor(nube5Actor1)

# suelo
renderer.AddActor(sueloActor)
# renderer.AddActor(ramitaActor1)
renderer.AddActor(techoActor)
renderer.AddActor(marcoH1Actor)
renderer.AddActor(marcoH2Actor)
# renderer.AddActor(marcoH3Actor)
# renderer.AddActor(marcoV1Actor)
renderer.AddActor(marcoV2Actor)
renderer.AddActor(marcoV3Actor)
renderer.AddActor(chimenea1Actor)
renderer.AddActor(chimenea2Actor)
renderer.AddActor(ladrillo1Actor)
renderer.AddActor(ladrillo2Actor)
renderer.AddActor(ladrillo3Actor)
renderer.AddActor(ladrillo4Actor)
renderer.AddActor(ladrillo5Actor)
renderer.AddActor(ladrillo6Actor)
renderer.AddActor(ladrillo7Actor)
renderer.AddActor(ladrillo8Actor)
renderer.AddActor(ladrillo9Actor)
renderer.AddActor(ladrillo10Actor)

# renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(400, 400)
render_window.AddRenderer(renderer)

# interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
