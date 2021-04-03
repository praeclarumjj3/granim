from manimlib.imports import *

####....... Helper Functions and Classes .......####

# This function returns data from .csv to an array
def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords


class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

####....... Main Classes .......####

# PlotCSV
class PlotCSV(GraphFromData):
    CONFIG = {
        "y_max": 110,
        "x_max": 12,
        "x_axis_label": "$Epochs$",
        "y_axis_label": "$Loss$",
        "axes_color": ORANGE,
        "exclude_zero_label": False,
        }

    def construct(self, csv_path='granim/data', color=BLUE, is_gif=True):
        self.setup_axes(animate=True)
        # Get coords
        coords = get_coords_from_csv(csv_path)
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=color)
        # Set dots
        dots = self.get_dots_from_coords(coords, 0.05)

        if is_gif:
            self.add(dots)
            self.play(ShowCreation(graph,run_time=4))
            self.wait(2)
        else:
            self.add(dots,graph)

# PlotPoints
class PlotPoints(GraphFromData):
    CONFIG = {
        "y_max": 50,
        "x_max": 17,
        "x_axis_label": "$Epochs$",
        "y_axis_label": "$Loss$",
        "axes_color": ORANGE,
        "exclude_zero_label": False,
        }
    def construct(self, x_pts=None, y_pts=None, color=BLUE, is_gif=True):
        self.setup_axes(animate=True)
        x_pts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        y_pts = [40.22, 35.88, 30.66, 25.34, 22.78, 19.35, 17.65, 16.89, 14.56, 12.89, 9.98, 7.75, 6.65, 5.55, 3.00]

        if x_pts is None:
            coords = [[i,py] for i,py in enumerate(y_pts)]
        else:    
            coords = [[px,py] for px,py in zip(x_pts,y_pts)]

        points = self.get_points_from_coords(coords)
        
        graph = SmoothGraphFromSetPoints(points,color=color)
        dots = self.get_dots_from_coords(coords, 0.05)

        if is_gif:
            self.add(dots)
            self.play(ShowCreation(graph,run_time=4))
            self.wait(3)
        else:
            self.add(dots,graph)
