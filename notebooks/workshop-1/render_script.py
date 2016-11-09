from PyQt4.QtGui import QImage
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPainter

def makeImage(dow, tod):
    layer = qgis.utils.iface.activeLayer()
    renderer = layer.rendererV2()

    renderer.setClassAttribute("-predicted_pickup_"+str(dow)+"_"+str(tod))
    
    #http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/composer.html
    
    # create image
    img = QImage(QSize(800, 1000), QImage.Format_ARGB32_Premultiplied)

    # set image's background color
    color = QColor(255, 255, 255)
    img.fill(color.rgb())

    # create painter
    p = QPainter()
    p.begin(img)
    p.setRenderHint(QPainter.Antialiasing)

    render = QgsMapRenderer()

    # set layer set
    layers_to_draw = []
    
    for l in iface.mapCanvas().layers():
        if l.name() in ['grid', 'nyc_projected']:
            layers_to_draw.append(l.id())
    
    #lst = [layer.id()]
    lst = layers_to_draw  # add ID of every layer
    render.setLayerSet(lst)

    # set extent
    rect = QgsRectangle(render.fullExtent())
    rect.scale(1.1)
    render.setExtent(rect)

    # set output size
    render.setOutputSize(img.size(), img.logicalDpiX())

    # do the rendering
    render.render(p)
    p.end()
    
    # create file path
    imPath = '/Users/danil/Documents/GitHub/dmc/notebooks/workshop-1/-screenshots/'
    imName = str(dow) + "_" + str(tod)
    
    # save image
    img.save(imPath + imName + '.png',"png")


for i in range(24):
    makeImage(1,i)