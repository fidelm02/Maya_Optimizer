"""
Modeling.

This is the master class that contains all methods
for modeling optimization.
"""
import General
reload (General)
from General import GeneralControls

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

class ModelingControls(GeneralControls):

    """
    Title.

    Description
    """

    def __init__(self):
        """
        Title.

        Description
        """
        GeneralControls.__init__(self)

    def transformations(self, fix):
        """
        First line.

        Description.
        """

        all_geos = cmds.ls(geometry=1, l = 1)
        attrs = ['X', 'Y', 'Z']
        problem = False
        problems_active = False

        for geo in all_geos:
            current_problem = False
            geo = cmds.listRelatives(geo, p=1)[0]
            for attr in attrs:
                if cmds.getAttr(geo + '.translate' + attr) != 0.0:
                    problem = True
                    current_problem = True
                if cmds.getAttr(geo + '.rotate' + attr) != 0.0:
                    problem = True
                    current_problem = True
                if cmds.getAttr(geo + '.scale' + attr) != 1.0:
                    problem = True
                    current_problem = True

            if current_problem:
                if problems_active is False:
                    self.details.append("Transformations problems")
                    problems_active = True
                if fix:
                    cmds.lockNode(geo, lock=0)
                    cmds.makeIdentity(geo, apply=1, t=1, r=1, s=1, n=0)
                    self.details.append("\tModified: " + str(geo))
                else:
                    self.details.append("\t" + str(geo))

        if problem:
            self.posible_fix.append("Transformation problems")
        else:
            self.posible_fix.append("All transformations: Clear")

    def history(self, fix):
        """
        First line.

        Description.
        """
        problems = False
        meshes = cmds.ls(type="mesh")
        problems_active = False

        for mesh in meshes:
            historyElements = cmds.listHistory(mesh)
            if (len(historyElements) > 1):
                problems = True
                if fix:
                    if problems_active is False:
                        self.details.append("History problems")
                        problems_active = True
                    self.details.append("\t"+str(mesh))
                    cmds.delete(mesh, ch=1)
                else:
                    if problems_active is False:
                        self.details.append("History problems")
                        problems_active = True
                    self.details.append("\t"+str(mesh))

        if problems:
            if fix:
                self.posible_fix.append("History fixed")
            else:
                self.posible_fix.append("History problems")

    def hierarchy(self, fix):
        """
        Hierarchy method

        This method will help to strcture the orden in
        the outliner and helps to clear your mess in the scene.
        """

        print("Hierarchy " + str(fix)+ " not specified yet")

    def names_method(self, fix):
        """
        Names method

        This method will help you to fix all repeated names in the
        geometries and groups.

        This help to avoid problems with reconnection materials
        and reloading the file as a reference.

        """

        dags = cmds.ls(tr=1)
        number = 1
        repeatedNames = []
        problems = False
        problems_message = False

        for element in dags:
            # Comparison with the others dag objects
            c_index = dags.index(element)
            for comparison in dags[c_index:]:

                # avoid the comparison with itself
                if element is not comparison:

                    # Comparing the names
                    n_element = self.minName(s_name=str(element))
                    n_comparison = self.minName(s_name=str(comparison))

                    if n_element == n_comparison:
                        problems = True

                        if (repeatedNames.count(n_element) == 0):
                            repeatedNames.append(n_element)

                        if problems_message is False:
                            problems_message = True
                            self.details.append("Names problems")

                        if (fix):
                            n_name = self.minName(
                                str(comparison))+'_'+str(number)
                            cmds.rename(comparison, n_name)
                            self.details.append(
                                "\t"+n_element+" --> "+n_name)
                        else:
                            self.details.append("\t"+n_element)

                        number = number + 1

        geos = cmds.ls(geometry = 1)

        if problems:
            self.posible_fix.append("Names problem "+str(len(repeatedNames)))
        else:
            self.posible_fix.append("Names clear")

    def minName(self, s_name):
        """
        get the individual name without the full path
        """
        if s_name.count('|') == 0:
            return s_name
        else:
            new_subname = s_name.partition('|')[2]
            return self.minName(s_name=new_subname)

    def materials(self, fix):
        """
        Check materials.

        In the exist only should exist initial materials.
        """
        all_geometry = cmds.ls(type="mesh")

        problems = False
        problems_message = False
        for geo in all_geometry:
            lambert1_found = False
            current_elements = cmds.listConnections(geo, source=1)
            for c_element in current_elements:
                con1 = str(c_element).count('lambert1') > 0
                con2 = str(c_element).count('initialShadingGroup') > 0
                if con1 or con2:
                    lambert1_found = True

            if lambert1_found is False:
                problems = True

                if problems_message is False:
                    problems_message = True
                    self.details.append("Materials problems")
                self.details.append("\t" + str(geo))
                if fix:
                    cmds.hyperShade(geo, assign="lambert1")

        if problems:
            if fix:
                ins = 'hyperShadePanelMenuCommand('
                ins = ins + '"hyperShadePanel1", "deleteUnusedNodes");'
                try:
                    mel.eval(ins)
                except:
                    self.details.append("Problems deleted un used nodes")
                self.posible_fix.append("Materials fixed")
            else:
                self.posible_fix.append("Materials problems")
        else:
            self.posible_fix.append("Materials clear")

    def uv_sets(self, fix):
        """
        First line.

        Description.
        """

        problems = False
        details = False

        # lists all the mesh type objects
        objects = cmds.ls(type='mesh')
        objects_len = len(objects)

        if objects_len:
            for o in objects:
                # checks if there are more than one UV set
                uv_set = cmds.polyUVSet(o, q=1, auv=1)
                uv_set_len = len(uv_set)
                if not details:
                    details = True
                    self.details.append("UV set problems")
                self.details.append("\t" + str(o))
                if uv_set_len > 1:
                    if not fix:
                        problems = True
                    else:
                        # deletes all the extra UV sets
                        for current_set in uv_set:
                            original_uv_set = cmds.polyUVSet(o, q=1, cuv=1)
                            cmds.polyUVSet(o, cuv=1, uvs=current_set)
                            converted_uvset = cmds.polyListComponentConversion(
                                o + '.vtx[0]', fv=1, tuv=1)
                            cmds.polyUVSet(o, cuv=1, uvs=original_uv_set[0])
                            if current_set != uv_set[0]:
                                if converted_uvset:
                                    cmds.polyCopyUV(
                                        o, uvi=current_set, uvs=uv_set[0])
                                cmds.polyUVSet(o, d=1, uvs=current_set)
                        if uv_set[0] != 'map1':
                            cmds.polyUVSet(o, uvs=uv_set[0], rn=1, nuv='map1')

        if problems:
            if fix:
                self.posible_fix.append("UV sets fixed")
            else:
                self.posible_fix.append("UV sets problems")
        else:
            self.posible_fix.append("UV sets clear")

    def center(self, fix):
        """
        Geometry in the center.

        Detect if are only one geometry in the scene.
        """
        geos = cmds.ls(geometry=1, l=1)
        root_nodes = []
        main_root = []
        feedback_header = False
        problems = False
        cant = 0
        for geo in geos:
            rootElement = self.get_root_node(element=geo)

            if len(root_nodes) == 0:
                root_nodes.append(rootElement)
            else:
                agregar = True
                for rEle in root_nodes:
                    if rEle == rootElement:
                        agregar = False
                
                if agregar:
                    root_nodes.append(rootElement)
            
        """
        for i in range(0, len(root_nodes) - 1):
            current = root_nodes[i]
            repeated = False
            if i is not len(root_nodes) - 1:
                for j in range(i + 1, len(root_nodes) - 1):
                    evaluated = root_nodes[j]
                    if current == evaluated:
                        repeated = True
            if repeated is False:
                main_root.append(current)
        """

        for root_node in root_nodes:

            corners = cmds.exactWorldBoundingBox(root_node)

            button_point = [
                (corners[0] + corners[3]) / 2, corners[1],
                (corners[2] + corners[5]) / 2]

            wrong = False
            for position in button_point:
                if position != 0:
                    wrong = True

            if wrong:
                cant = cant + 1
                problems = True
                if feedback_header is False:
                    feedback_header = True
                    self.details.append("Center elements")
                if fix:
                    cmds.xform(root_node, piv=button_point, ws=1)
                    cmds.move(0, 0, 0, root_node, rpr=1)
                    cmds.makeIdentity(root_node, apply=1, t=1, r=1, s=1, n=0)

                    str_fix = (str(root_node) + " was moved")
                    self.details.append("\t" + str_fix)
                else:
                    str_chk = (str(root_node) + " needs to be fixed")
                    self.details.append("\t" + str_chk)
        if problems:
            if cant > 0:
                self.posible_fix.append("Center objects problems ")
            else:
                self.posible_fix.append("Center object problems ")
        else:
            self.posible_fix.append("Center objects clear")

    def get_root_node(self, element):
        allElements = str(element).split("|")
        if allElements[0] == " ":
            return "|" + allElements[0]
        else:
            return "|" + allElements[1]



