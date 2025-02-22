import numpy as np
import pyqtgraph as pg
from tests.image_testing import assertImageApproved


def test_PlotCurveItem():
    p = pg.GraphicsLayoutWidget()
    p.resize(200, 150)
    p.ci.setContentsMargins(4, 4, 4, 4)  # default margins vary by platform
    p.show()
    v = p.addViewBox()
    data = np.array([1,4,2,3,np.inf,5,7,6,-np.inf,8,10,9,np.nan,-1,-2,0])
    c = pg.PlotCurveItem(data)
    v.addItem(c)
    v.autoRange()
    
    # Check auto-range works. Some platform differences may be expected..
    checkRange = np.array([[-1.1457564053237301, 16.145756405323731], [-3.076811473165955, 11.076811473165955]])
    assert np.allclose(v.viewRange(), checkRange)
    
    assertImageApproved(p, 'plotcurveitem/connectall', "Plot curve with all points connected.")
    
    c.setData(data, connect='pairs')
    assertImageApproved(p, 'plotcurveitem/connectpairs', "Plot curve with pairs connected.")
    
    c.setData(data, connect='finite')
    assertImageApproved(p, 'plotcurveitem/connectfinite', "Plot curve with finite points connected.")
    
    c.setData(data, connect=np.array([1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0]))
    assertImageApproved(p, 'plotcurveitem/connectarray', "Plot curve with connection array.")

    p.close()
