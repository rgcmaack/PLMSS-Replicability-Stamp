# state file generated using paraview version 5.10.1-2-g4354bf2d

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1153, 817]
renderView1.InteractionMode = 'Selection'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, 0.0, 0.0301545187830925]
renderView1.UseToneMapping = 1
renderView1.Exposure = 2.0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.0, 0.0, 2.0642214904940137]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.0301545187830925]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.7339276300654552
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.EnableRayTracing = 1
renderView1.BackEnd = 'OSPRay pathtracer'
renderView1.AmbientSamples = 5
renderView1.SamplesPerPixel = 8
renderView1.LightScale = 0.3
renderView1.Backgroundmode = 'Backplate'
renderView1.EnvironmentalBG = [1.0, 1.0, 1.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1153, 817)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
noisyTerrainvtu = XMLUnstructuredGridReader(registrationName='noisyTerrain.vtu', FileName=['/home/noisyTerrain.vtu'])
noisyTerrainvtu.PointArrayStatus = ['TextureCoordinates', 'RandomPointScalars', 'Sine', 'DistanceField', 'Blend']
noisyTerrainvtu.TimeArray = 'None'

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=noisyTerrainvtu)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'Blend']
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.07

# create a new 'TTK MorseSmaleSegmentationPL'
tTKMorseSmaleSegmentationPL1 = TTKMorseSmaleSegmentationPL(registrationName='TTKMorseSmaleSegmentationPL1', Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleSegmentationPL1.InputArray = ['POINTS', 'Blend']
tTKMorseSmaleSegmentationPL1.ComputeSaddles = 1

# find source
tTKMorseSmaleSegmentationPL1_1 = FindSource('TTKMorseSmaleSegmentationPL1')

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=OutputPort(tTKMorseSmaleSegmentationPL1_1,3))

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals1', Input=extractSurface1)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKMorseSmaleSegmentationPL1
tTKMorseSmaleSegmentationPL1Display = Show(tTKMorseSmaleSegmentationPL1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'CriticalityIndex'
criticalityIndexLUT = GetColorTransferFunction('CriticalityIndex')
criticalityIndexLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0, 0.865003, 0.865003, 0.865003, 3.0, 0.705882, 0.0156863, 0.14902]
criticalityIndexLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKMorseSmaleSegmentationPL1Display.Representation = 'Surface'
tTKMorseSmaleSegmentationPL1Display.ColorArrayName = ['POINTS', 'Criticality Index']
tTKMorseSmaleSegmentationPL1Display.LookupTable = criticalityIndexLUT
tTKMorseSmaleSegmentationPL1Display.PointSize = 18.0
tTKMorseSmaleSegmentationPL1Display.RenderPointsAsSpheres = 1
tTKMorseSmaleSegmentationPL1Display.SelectTCoordArray = 'None'
tTKMorseSmaleSegmentationPL1Display.SelectNormalArray = 'None'
tTKMorseSmaleSegmentationPL1Display.SelectTangentArray = 'None'
tTKMorseSmaleSegmentationPL1Display.OSPRayScaleArray = 'Blend_Order'
tTKMorseSmaleSegmentationPL1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleSegmentationPL1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleSegmentationPL1Display.ScaleFactor = 0.1
tTKMorseSmaleSegmentationPL1Display.SelectScaleArray = 'Blend_Order'
tTKMorseSmaleSegmentationPL1Display.GlyphType = 'Arrow'
tTKMorseSmaleSegmentationPL1Display.GlyphTableIndexArray = 'Blend_Order'
tTKMorseSmaleSegmentationPL1Display.GaussianRadius = 0.005
tTKMorseSmaleSegmentationPL1Display.SetScaleArray = ['POINTS', 'Blend_Order']
tTKMorseSmaleSegmentationPL1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleSegmentationPL1Display.OpacityArray = ['POINTS', 'Blend_Order']
tTKMorseSmaleSegmentationPL1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleSegmentationPL1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleSegmentationPL1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleSegmentationPL1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 90600.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleSegmentationPL1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 90600.0, 1.0, 0.5, 0.0]

# find source
tTKMorseSmaleSegmentationPL1_2 = FindSource('TTKMorseSmaleSegmentationPL1')

# show data from tTKMorseSmaleSegmentationPL1_2
tTKMorseSmaleSegmentationPL1_2Display = Show(OutputPort(tTKMorseSmaleSegmentationPL1_2, 2), renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleSegmentationPL1_2Display.Representation = 'Surface'
tTKMorseSmaleSegmentationPL1_2Display.ColorArrayName = [None, '']
tTKMorseSmaleSegmentationPL1_2Display.LineWidth = 3.0
tTKMorseSmaleSegmentationPL1_2Display.SelectTCoordArray = 'None'
tTKMorseSmaleSegmentationPL1_2Display.SelectNormalArray = 'None'
tTKMorseSmaleSegmentationPL1_2Display.SelectTangentArray = 'None'
tTKMorseSmaleSegmentationPL1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleSegmentationPL1_2Display.SelectOrientationVectors = 'None'
tTKMorseSmaleSegmentationPL1_2Display.ScaleFactor = 0.1
tTKMorseSmaleSegmentationPL1_2Display.SelectScaleArray = 'None'
tTKMorseSmaleSegmentationPL1_2Display.GlyphType = 'Arrow'
tTKMorseSmaleSegmentationPL1_2Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleSegmentationPL1_2Display.GaussianRadius = 0.005
tTKMorseSmaleSegmentationPL1_2Display.SetScaleArray = [None, '']
tTKMorseSmaleSegmentationPL1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleSegmentationPL1_2Display.OpacityArray = [None, '']
tTKMorseSmaleSegmentationPL1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleSegmentationPL1_2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleSegmentationPL1_2Display.PolarAxes = 'PolarAxesRepresentation'

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'MorseSmaleManifold'
morseSmaleManifoldLUT = GetColorTransferFunction('MorseSmaleManifold')
morseSmaleManifoldLUT.RGBPoints = [0.0, 1.0, 0.0, 0.0, 1.7636666666666665, 0.0, 0.0, 0.360784313725, 3.515, 0.0, 1.0, 1.0, 5.2909999999999995, 0.0, 0.501960784314, 0.0, 7.0411, 1.0, 1.0, 0.0, 8.806, 1.0, 0.380392156863, 0.0, 10.569666666666667, 0.419607843137, 0.0, 0.0, 12.333333333333332, 0.8784313725490196, 0.6, 0.5450980392156862, 14.097, 0.6745098039215687, 0.2901960784313726, 0.6745098039215687, 15.848333333333334, 1.0, 0.380392156863, 0.0, 17.624333333333333, 1.0, 1.0, 0.0, 19.375666666666664, 0.0, 0.501960784314, 0.0, 21.139333333333333, 0.0, 1.0, 1.0, 22.903, 0.0, 0.0, 0.360784313725, 24.666666666666664, 0.278431372549, 0.278431372549, 0.858823529412, 24.666666666666664, 0.23921568627450981, 0.3254901960784314, 0.3607843137254902, 24.729114532470703, 0.5764705882352941, 0.8117647058823529, 0.8627450980392157, 24.729114532470703, 0.25098039215686274, 0.3568627450980392, 0.3764705882352941, 24.822786331176758, 0.25098039215686274, 0.3568627450980392, 0.3764705882352941, 26.6025333404541, 0.403921568627451, 0.7294117647058823, 0.5843137254901961, 28.18166666666667, 0.0, 1.0, 1.0, 29.957666666666665, 0.0, 0.501960784314, 0.0, 31.709, 1.0, 1.0, 0.0, 33.47266666666666, 1.0, 0.380392156863, 0.0, 35.236333333333334, 0.419607843137, 0.0, 0.0, 37.0, 0.878431372549, 0.301960784314, 0.301960784314]
morseSmaleManifoldLUT.ColorSpace = 'RGB'
morseSmaleManifoldLUT.ScalarRangeInitialized = 1.0
morseSmaleManifoldLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11', '12', '12', '13', '13', '14', '14', '15', '15', '16', '16', '17', '17', '18', '18', '19', '19', '20', '20', '21', '21', '22', '22', '23', '23', '24', '24', '25', '25', '26', '26', '27', '27', '28', '28', '29', '29', '30', '30', '31', '31', '32', '32', '33', '33', '34', '34', '35', '35', '36', '36', '37', '37', '38', '38', '39', '39', '40', '40', '41', '41', '42', '42', '43', '43', '44', '44', '45', '45', '46', '46', '47', '47', '48', '48', '49', '49']
morseSmaleManifoldLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0]
morseSmaleManifoldLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = ['POINTS', 'MorseSmaleManifold']
generateSurfaceNormals1Display.LookupTable = morseSmaleManifoldLUT
generateSurfaceNormals1Display.Opacity = 0.975
generateSurfaceNormals1Display.Specular = 0.32
generateSurfaceNormals1Display.SpecularPower = 95.0
generateSurfaceNormals1Display.Diffuse = 1.5
generateSurfaceNormals1Display.SelectTCoordArray = 'TextureCoordinates'
generateSurfaceNormals1Display.SelectNormalArray = 'Normals'
generateSurfaceNormals1Display.SelectTangentArray = 'None'
generateSurfaceNormals1Display.OSPRayScaleArray = 'Blend'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'None'
generateSurfaceNormals1Display.ScaleFactor = 0.1
generateSurfaceNormals1Display.SelectScaleArray = 'Blend'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'Blend'
generateSurfaceNormals1Display.GaussianRadius = 0.005
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'Blend']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'Blend']
generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals1Display.ScaleTransferFunction.Points = [-3.3288182535266104, 0.0, 0.5, 0.0, 4.534999266667052, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals1Display.OpacityTransferFunction.Points = [-3.3288182535266104, 0.0, 0.5, 0.0, 4.534999266667052, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'CriticalityIndex'
criticalityIndexPWF = GetOpacityTransferFunction('CriticalityIndex')
criticalityIndexPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
criticalityIndexPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'MorseSmaleManifold'
morseSmaleManifoldPWF = GetOpacityTransferFunction('MorseSmaleManifold')
morseSmaleManifoldPWF.Points = [0.0, 0.0, 0.5, 0.0, 37.0, 1.0, 0.5, 0.0]
morseSmaleManifoldPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(generateSurfaceNormals1)
# ----------------------------------------------------------------

SaveScreenshot("/home/noisyTerrainMSS.jpg")


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
