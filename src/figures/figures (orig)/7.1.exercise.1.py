from figures import *

dx = 15
rtmargin = 8
lbmargin = 15
width = 8*dx + rtmargin + lbmargin
height = 8*dx +  rtmargin + lbmargin

beginfigure("7.1.exercise.1", width, height)
setupcoordinates([lbmargin, lbmargin, width-rtmargin, height-rtmargin],
                 [0, -3, 120, 5])

xrange = [0, 15, 120]
yrange = [-3,1,5]
Grid(xrange, yrange, color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks(xrange, yrange)
axes.drawticks()
axes.setlabels([0, 30, 120], yrange)
axes.drawlabels()

Label(r"$T$", [120,0], offset=[-3,3], alignment="rb").draw()
Label(r"$\displaystyle\frac{dT}{dt}$", [0,5], offset=[3,-3], alignment="lt").draw()

endfigure()
