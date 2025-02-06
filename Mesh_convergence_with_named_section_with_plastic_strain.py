from time import clock, time
Model.Mesh.ElementOrder = ElementOrder.Quadratic
solution = Model.Analyses[0].Solution #define solution data
setting2d = Ansys.Mechanical.Graphics.GraphicsImageExportSettings()

CAMERA=Graphics.Camera

#selection
SlMn = ExtAPI.SelectionManager
SlMn.ClearSelection()
Sel = SlMn.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)

#Model
model = ExtAPI.DataModel.Project.Model

# Get parts
Parts = model.Geometry.GetChildren(DataModelObjectCategory.Part,True)
location =[]
n=0
print("Listing properties of Items:")
with Transaction():             # Suppress GUI update until finish to improve speed
    for Part in Parts:
        location.append(str('named_section_%d') %(n))
        # print("Part name: ",PName)
        tmp_ls = []
        for Body in Part.Children:
            BName = Body.Name
            BId = Body.GetGeoBody().Id
            #print("Body name: "+BName+" ,BId: "+str(BId))
            tmp_ls.append(BId)      # Collect all body Ids in temporary list

        Sel.Ids = tmp_ls
        print("Sel.Ids: ",Sel.Ids)
        # Create named selection
        NSn = model.NamedSelections
        MyNS = NSn.AddNamedSelection()
        MyNS.Name = Part.Name
        MyNS.Location = Sel
        location[n] = solution.AddEquivalentPlasticStrain()
        location[n].Location = Sel
        n+=1
        
        

maximum_equivalent_plastic_strain = 0 # defines maximum equivalent plastic strain
total_equivalent_plastic_strain = solution.AddEquivalentPlasticStrainRST() # defines total equivalent stress
total_deformation = solution.AddTotalDeformation() # defines total deformation
total_equivalent_stress = solution.AddEquivalentStress()

convergence = 0 # defines convergence
n = 0 # steps
m = 3
plastic_strain = []
mesh_size_list = []
convergence_list = []
# starts while loop
while n < 7: # defines convergence criterias for while loop

    
    maximum_equivalent_plastic_strain_pre = maximum_equivalent_plastic_strain #defines the previous equivalent stress
    m = m *0.8
    #region Details View Action
    Model.Mesh.ElementSize = Quantity(m, "mm") # iterates on mesh
    

    #region Context Menu Action
    t1 = time() # notes time

    Model.Mesh.GenerateMesh() # generates mesh


    solution.Solve(True) #solves analysis
    total_deformation.Activate()
    CAMERA.SetFit()
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Iso)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d0069.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    total_equivalent_stress.Activate()
    CAMERA.SetFit()
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Front)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d001.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Back)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d002.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Right)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d003.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Left)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d004.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Top)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d005.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Bottom)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d006.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Iso)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d007.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    location[0].Activate()
    CAMERA.SetFit()
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Front)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d101.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Back)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d102.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Right)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d103.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Left)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d104.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Top)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d105.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Bottom)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d106.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Iso)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d107.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    
    
    location[1].Activate()
    CAMERA.SetFit()
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Front)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d201.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Back)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d202.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Right)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d203.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Left)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d204.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Top)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d205.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Bottom)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d206.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Iso)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d207.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    '''
    location[2].Activate()
    CAMERA.SetFit()
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Front)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d301.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Back)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d302.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Right)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d303.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Left)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d304.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Top)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d305.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Bottom)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d306.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    CAMERA.SetSpecificViewOrientation(ViewOrientationType.Iso)
    Graphics.ExportImage("C:\Users\prustad\OneDrive - Digicorner\Downloads\\image%d307.png" % (n), GraphicsImageExportFormat.PNG, setting2d)
    
    
    maximum_equivalent_plastic_strain = total_equivalent_plastic_strain.Maximum
    minimum_equivalent_plastic_strain = total_equivalent_plastic_strain.Minimum
    
    convergence = maximum_equivalent_plastic_strain_pre / maximum_equivalent_plastic_strain
    '''
    t2 = time() # notes time
    
    plastic_strain.append(maximum_equivalent_plastic_strain)
    mesh_size_list.append(m)
    convergence_list.append(convergence)
    print maximum_equivalent_plastic_strain, maximum_equivalent_plastic_strain_pre
    print "convergence is equal to ", convergence
    print "Stats for mesh %d, elapsed time=%d" % (n, t2-t1)
    print Model.Mesh.Nodes
    print "mesh size = ", m
    n += 1
else:
    print "finished."
    print plastic_strain
    print mesh_size_list
    print convergence_list
#region Details View Action