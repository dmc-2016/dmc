import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
from System.Drawing import Rectangle, Point, Size, Color
import math
import time
import subprocess
import os

sc.doc = Rhino.RhinoDoc.ActiveDoc

obj = rs.GetObject("Select object for prediction")
orbitRes = rs.GetReal("Number of images per revolution", number=10)
vertRes = rs.GetReal("Number of revolutions", number=5)
distMult = rs.GetReal("Distance from object", number=5)

sc.doc.Objects.Select(obj)
rs.Command("_Invert")
rs.Command("_Hide")

w = 64
h = 64

rView = Rhino.RhinoDoc.ActiveDoc.Views.Add("view", Rhino.Display.DefinedViewportProjection.Perspective, Rectangle(Point(100, 100), Size(w, h)), True);

# http://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Display_RhinoViewport.htm
rView.TitleVisible = False
rView.MainViewport.ConstructionGridVisible = False
rView.MainViewport.ConstructionAxesVisible = False
rView.MainViewport.WorldAxesVisible = False

Rhino.ApplicationSettings.AppearanceSettings.ViewportBackgroundColor = Color.White
shaded = Rhino.Display.DisplayModeDescription.FindByName("Shaded")
rView.ActiveViewport.DisplayMode = shaded

tar = rs.SurfaceVolumeCentroid(obj)[0]

#http://4.rhino3d.com/5/rhinoscript/geometry_methods/boundingbox.htm
bb = rs.BoundingBox(obj)
dist = max([bb[1].X - bb[0].X, bb[3].Y - bb[0].Y, bb[4].Z - bb[0].Z]) * distMult

id = str(int(time.time()))

print("Gathering views...")

for j in range(int(vertRes)):
    
    z = tar.Z + math.sin(math.pi / 2 * j/float(vertRes)) * dist
    dist_2 = math.cos(math.pi / 2 * j/float(vertRes)) * dist
    
    for i in range(int(orbitRes)):
        
        x = tar.X + math.sin(2 * math.pi * i/float(orbitRes)) * dist_2
        y = tar.Y + math.cos(2 * math.pi * i/float(orbitRes)) * dist_2
        
        p = rs.AddPoint(x, y, z)
        pt = rs.coerce3dpoint(p)
        
        rView.ActiveViewport.SetCameraLocation(pt, False)
        rView.ActiveViewport.SetCameraDirection(tar - pt, True)
        
        rs.DeleteObjects(p)
        
        Rhino.RhinoDoc.ActiveDoc.Views.Redraw()
        
        size = Size(w, h)
        capture = rView.CaptureToBitmap(size)
        
        capture.Save("-temp//" + "_".join([id, str(j), str(i)]) + ".png")

rView.Close()
rs.Command("_Show")

print("Making predictions...")

dir = os.path.expanduser("~\\Documents")

sshProcess = subprocess.Popen(["ssh", "-p", "2222", "vagrant@127.0.0.1", "-i", dir + "\\GitHub\\dmc\\.vagrant\\machines\\default\\virtualbox\\private_key"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
sshProcess.stdin.write("cd 'notebooks/workshop-2'\n")
sshProcess.stdin.write("/home/vagrant/anaconda2/bin/python 03-use_model.py\n")
sshProcess.stdin.close()

output = []

for line in sshProcess.stdout:
    s = line.split("python: ")
    if len(s) > 1:
        output.append(s[1].strip())
    
for line in sshProcess.stderr:
    print line

folder = '-temp'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    os.unlink(file_path)

print( "predicted " + output[0] + " with " + output[1] + " confidence")