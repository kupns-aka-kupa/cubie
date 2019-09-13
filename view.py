import tools; import cube; import grid; import data

tools = tools.Tools()
data = data.Data()
colors = data.colors

class Viewport():

    def __init__(self, camera, pygame):
        self.camera = camera
        self.pg = pygame
        self.grid = grid.Grid(self.camera, self.pg, data, tools)

#       UP_CORNERS
#       start_coord(y,x,z)
        self.corner_YOB = cube.Cube(self.camera, self.pg, data, tools, (2, -2, -2))
        self.corner_YBR = cube.Cube(self.camera, self.pg, data, tools, (2, -2, 2))
        self.corner_YRG = cube.Cube(self.camera, self.pg, data, tools, (-2, -2, 2))
        self.corner_YGO = cube.Cube(self.camera, self.pg, data, tools, (-2, -2, -2))

        self.cube = [self.corner_YOB, self.corner_YBR, self.corner_YRG, self.corner_YGO]
##       DOWN_CORNERS
#        self.corner_WBO = Cube(self.camera, self.pg, data, tools, (2, 2, -2))
#        self.corner_WRB = Cube(self.camera, self.pg, data, tools, (2, 2, 2))
#        self.corner_WGR = Cube(self.camera, self.pg, data, tools, (-2, 2, 2))
#        self.corner_WOG = Cube(self.camera, self.pg, data, tools, (-2, 2, -2))
##       UP_EDGES
#        self.edge_YB = Cube(self.camera, self.pg, data, tools, (2, -2, 0))
#        self.edge_YR = Cube(self.camera, self.pg, data, tools, (0, -2, 2))
#        self.edge_YG = Cube(self.camera, self.pg, data, tools, (-2, -2, 0))
#        self.edge_YO = Cube(self.camera, self.pg, data, tools, (0, -2, -2))
##       MIDDLE_EDGES
#        self.edge_OB = Cube(self.camera, self.pg, data, tools, (2, 0, -2))
#        self.edge_BR = Cube(self.camera, self.pg, data, tools, (2, 0, 2))
#        self.edge_RG = Cube(self.camera, self.pg, data, tools, (-2, 0, 2))
#        self.edge_GO = Cube(self.camera, self.pg, data, tools, (-2, 0, -2))
##       DOWN_EDGES
#        self.edge_WB = Cube(self.camera, self.pg, data, tools, (2, 2, 0))
#        self.edge_WR = Cube(self.camera, self.pg, data, tools, (0, 2, 2))
#        self.edge_WG = Cube(self.camera, self.pg, data, tools, (-2, 2, 0))
#        self.edge_WO = Cube(self.camera, self.pg, data, tools, (0, 2, -2))
##       СENTERS
#        self.center_Y = Cube(self.camera, self.pg, data, tools, (0, -2, 0))
#        self.center_W = Cube(self.camera, self.pg, data, tools, (0, 2, 0))
#        self.center_B = Cube(self.camera, self.pg, data, tools, (2, 0, 0))
#        self.center_G = Cube(self.camera, self.pg, data, tools, (-2, 0, 0))
#        self.center_O = Cube(self.camera, self.pg, data, tools, (0, 0, -2))
#        self.center_R = Cube(self.camera, self.pg, data, tools, (0, 0, 2))
#
    def display_order(self, list):
        pass

    def update(self):
#       render
        self.grid.render()
##       UP_CORNERS

        self.corner_YOB.render([colors.orange, colors.blue, colors.yellow, colors.black])
#        self.corner_YBR.render([colors.black, colors.blue, colors.yellow, colors.red, colors.black])
#        self.corner_YRG.render([colors.black, colors.black, colors.yellow, colors.red, colors.green, colors.black])
#        self.corner_YGO.render([colors.orange, colors.black, colors.yellow, colors.black, colors.green, colors.black])
##       DOWN_CORNERS
#        self.corner_WBO.render([colors.orange, colors.blue, colors.black, colors.black, colors.black, colors.white])
#        self.corner_WRB.render([colors.black, colors.blue, colors.black, colors.red, colors.black, colors.white])
#        self.corner_WGR.render([colors.black, colors.black, colors.black, colors.red, colors.green, colors.white])
#        self.corner_WOG.render([colors.orange, colors.black, colors.black, colors.black, colors.green, colors.white])
##       UP_EDGES
#        self.edge_YB.render([colors.black, colors.blue, colors.yellow, colors.black])
#        self.edge_YR.render([colors.black, colors.black, colors.yellow, colors.red, colors.black])
#        self.edge_YG.render([colors.black, colors.black, colors.yellow, colors.black, colors.green, colors.black])
#        self.edge_YO.render([colors.orange, colors.black, colors.yellow, colors.black])
##       MIDDLE_EDGES
#        self.edge_OB.render([colors.orange, colors.blue, colors.black])
#        self.edge_BR.render([colors.black, colors.blue, colors.black, colors.red, colors.black])
#        self.edge_RG.render([colors.black, colors.black, colors.black, colors.red, colors.green, colors.black])
#        self.edge_GO.render([colors.orange, colors.black, colors.black, colors.black, colors.green, colors.black])
##       DOWN_EDGES
#        self.edge_WB.render([colors.black, colors.blue, colors.black, colors.black, colors.black, colors.white])
#        self.edge_WR.render([colors.black, colors.black, colors.black, colors.red, colors.black, colors.white])
#        self.edge_WG.render([colors.black, colors.black, colors.black, colors.black, colors.green, colors.white])
#        self.edge_WO.render([colors.orange, colors.black, colors.black, colors.black, colors.black, colors.white])
##       СENTERS
#        self.center_O.render([ colors.orange, colors.black])
#        self.center_B.render([ colors.black, colors.blue, colors.black])
#        self.center_Y.render([ colors.black, colors.black, colors.yellow, colors.black])
#        self.center_R.render([ colors.black, colors.black, colors.black, colors.red, colors.black])
#        self.center_W.render([ colors.black, colors.black, colors.black, colors.black, colors.black, colors.white])
#        self.center_G.render([ colors.black, colors.black, colors.black, colors.black, colors.green, colors.black])
