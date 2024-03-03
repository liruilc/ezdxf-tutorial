import ezdxf
import os


doc = ezdxf.new("R2010")
msp = doc.modelspace()

points = [(0, 0, 0.1, 0.15), (3, 0, 0.2, 0.25), (6, 3, 0.3, 0.35), (6, 6)]
msp.add_lwpolyline(points)
file_path = os.path.join(r"C:\Users\wcndy\ezdxf_p_y", "lwpolyline1.dxf")

doc.saveas(file_path)


# lwpolyline 5

doc = ezdxf.new("R2010")
msp = doc.modelspace()

points = [(0, 0, 0, 0.05), (3, 0, 0.1, 0.2, -0.5), (6, 0, 0.1, 0.05), (9, 0)]
msp.add_lwpolyline(points)

file_path = os.path.join(r"C:\Users\wcndy\ezdxf_p_y", "lwpolyline2.dxf")
doc.saveas(file_path)


# lwpolyline 6

doc = ezdxf.new("R2010")
msp = doc.modelspace()
msp.add_lwpolyline([(0, 0, 0), (10, 0, 1), (20, 0, 0)], format="xyb")
msp.add_lwpolyline([(0, 10, 0), (10, 10, 0.5), (20, 10, 0)], format="xyb")
msp.add_lwpolyline([(0, 20, 0.5), (10, 20, 0)], format="xyb")
msp.add_lwpolyline([(0, 30, 2), (10, 30, 0)], format="xyb")
msp.add_lwpolyline(
    [(0, 40, 0.5), (10, 40, 0), (20, 40, -0.5), (30, 40, 0)], format="xyb"
)
msp.add_lwpolyline([(0, 50, 0.5), (10, 50, -0.5), (20, 50, 0)], format="xyb")
file_path = os.path.join(r"C:\Users\wcndy\ezdxf_p_y", "lwpolyline3.dxf")
doc.saveas(file_path)


# lwpolyline 7

doc = ezdxf.new("R2018", setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()
msp.add_lwpolyline(
    [(0.3111, 0, -0.7627), (-3.7404, 0, 0.7627), (-7.7919, 0, 0)], format="xyb"
)
msp.add_linear_dim(base=[0, 12], p1=(0.3111, 0), p2=(0, 0), dimstyle="EZDXF")


msp.add_lwpolyline(
    [(0, 10, -0.7627), (-4.0515, 10, 0.7627), (-8.1030, 10, 0)], format="xyb"
)

msp.add_line((0, 0), (0, 20))

file_path = os.path.join(r"C:\Users\wcndy\ezdxf_p_y", "lwpolyline4.dxf")
doc.saveas(file_path)


doc = ezdxf.new("R2018", setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()

msp.add_lwpolyline(
    [(0, 0, 1), (0, 10, 1), (0, 0, 0)],
    close=True,
    format="xyb",
    dxfattribs={"const_width": 0.4},
)

file_path = os.path.join(r"C:\Users\wcndy\ezdxf_p_y", "lwpolyline5.dxf")
doc.saveas(file_path)


doc = ezdxf.new("R2018", setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()

circle = msp.add_circle(
    center=(0, 0), radius=10, dxfattribs={"color": ezdxf.const.GREEN}
)
circle.to_spline()

file_path = os.path.join(r"C:\Users\wcndy\ezdxf_p_y", "lwpolyline6.dxf")
doc.saveas(file_path)
