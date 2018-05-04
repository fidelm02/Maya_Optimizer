# -*- coding: utf-8 -*- 

"""
General.

Description
"""
import maya.cmds as cmds
import pymel.core as pm

class GeneralControls():
    """
    Title.

    Description
    """

    def __init__(self):
        """
        Title.

        Description
        """
        self.posible_fix = []
        self.reference_to_fix = []
        self.details = []

    def unknown_nodes(self, fix):
        """
        Unkwnon and disconnected nodes.

        This methos will delete all unnecesary
        nodes from the scene.
        """
        useless_nodes = []
        element_types = [
            'groupId', 'hyperGraphInfo', 'hyperLayout',
            'hyperView', 'reference', 'mesh']

        # Put the elements to delete into the useless_node list
        for current_type in element_types:
            elements = cmds.ls(type=current_type)
            for element in elements:
                if current_type is 'mesh' or 'groupId':
                    if cmds.listConnections(element) is None:
                        useless_nodes.append(element)
                if current_type is 'hyperGraphInfo':
                    if element is not 'hyperGraphInfo':
                        useless_nodes.append(element)
                if current_type is 'hyperLayout':
                    if element is not 'hyperGraphLayout':
                        useless_nodes.append(element)
                if current_type is 'hyperView':
                    if element is not 'hyperView':
                        useless_nodes.append(element)
                if current_type is 'reference':
                    if str(element).count("UNKNOWN_REF_NODE"):
                        useless_nodes.append(element)

        cant = len(useless_nodes)
        ref_problems = []
        if cant > 0:
            self.posible_fix.append("Unknown nodes " + str(cant))
            reference_feedback = False
            for element in useless_nodes:
                if fix:
                    cmds.lockNode(element, l=0)
                    try:
                        NoDeletable = ['hyperGraphInfo', 'hyperGraphLayout']
                        for NoD in NoDeletable:
                            if element != unicode(NoD):
                                #print type(element)
                                cmds.delete(element)
                        self.details.append(
                            "\t Unknown: " + str(element) +
                            "deleted.")
                    except:
                        self.details.append(
                            "\t Unknown referenced: " + str(element))
                        if cmds.referenceQuery(element, isNodeReferenced=True):
                            namespace = cmds.referenceQuery(
                                element, referenceNode=True)
                            ref_problems.append(namespace)
                else:
                    if cmds.referenceQuery(element, isNodeReferenced=True):
                        if reference_feedback is False:
                            reference_feedback = True
                            self.reference_to_fix.append(
                                "\t  Unknown referenced nodes in the scene")
                        self.details.append(
                            "\t Unknown referenced: " + str(element))

                        namespace = cmds.referenceQuery(
                                element, referenceNode=True)
                        ref_problems.append(namespace)

    def non_referenced(self, fix):
        """
        Title.

        Description.
        """
        problems = False
        all_geos = cmds.ls(shapes=1)
        all_lights = cmds.ls(lights=1)
        all_lists = [all_geos, all_lights]

        for current_list in all_lists:
            for current_object in current_list:
                if cmds.objExists(current_object):
                    if cmds.referenceQuery(current_object, inr=1) == 0:
                        if problems is not True:
                            self.details.append("Non Referenced objects")
                            problems = True

                        #print str(current_object) + " is not a reference"
                        if fix:
                            # Add details of the current object
                            self.details.append(
                                "\tDeleted: " + str(current_object))

                            # Unlock the current object (if is needed)
                            cmds.lockNode(current_object, lock=0)

                            # Delete current object
                            NoDeletable = ['hyperGraphInfo', 'hyperGraphLayout']
                            for NoD in NoDeletable:
                                if current_object != NoD:
                                    cmds.delete(current_object)

                        else:
                            self.details.append(
                                "\t" + str(current_object))

        if problems:
            if fix:
                self.posible_fix.append(
                    "All non referenced objects were deleted.")
            else:

                self.posible_fix.append("Non referenced objects in the scene.")
        else:
            self.posible_fix.append("Non referenced: Clean")

    def return_feedback(self):
        """
        Return feedback.

        This method only return in an array the
        two strings that have the respective feedback.
        """
        posible = self.posible_fix
        reference = self.reference_to_fix
        details = self.details
        feedback_strings = [posible, reference, details]
        self.posible_fix = []
        self.reference_to_fix = []
        self.details = []
        return feedback_strings

    def invalid_names(self, fix):
        """
        ASCII invalid

        Validation that denied access to invalid ascii characters
        """
        allObjects = pm.ls(tr = 1, l = 1)
        equivalencias = [ ("ñ", 'n'), ("á", 'a'), ("é", 'e'),
            ("í", 'i'), ("ó", 'o'), ("ú", 'u'), ("Á", 'A'),
            ("É", 'E'), ("Í", 'i'), ("Ó", 'O'), ("Ú", 'U'),
            ("Ñ", "N")]

        problems = []
        refProblems = []
        filesProblems = []
        for obj in allObjects:
            #obj = cmds.listRelatives(unicode(obj), parent = 1)[0]
            try:
                str(obj)
            except:
                if (fix):
                    badString = unicode(obj)
                    newString = ''
                    for s in badString:
                        cur = s
                        for eq in equivalencias:
                            if cur.encode('utf-8') == eq[0]:
                                cur = unicode(eq[1])
                        newString = newString + cur
                    # Renombrando con el nuevo string
                    if unicode(obj.longName()).find(":") is not -1:
                        refProblems.append(obj)
                        refNode = pm.referenceQuery(obj, rfn=1)
                        valid = True
                        for rfN in filesProblems:
                            if rfN == refNode:
                                valid = False
                        if valid:
                            filesProblems.append(refNode)
                    else:
                        cmds.rename(unicode(obj), str(newString))
                        problems.append(obj)
                else:
                    if unicode(obj.longName()).find(":") is not -1:
                        refProblems.append(obj)
                    else:
                        problems.append(obj)

        if len(refProblems) != 0:
            refC = str(len(refProblems))
            self.reference_to_fix.append("Invalid Names ( " + refC + " )")

        if len(problems) == 0:
            #problems
            self.posible_fix.append("No invalid names")
            if len(refProblems) == 0:
                self.details.append("No invalid names")
            else:
                self.details.append("Invalid names from references")
                print "Reference nodes with invalid names"
                for rFile in filesProblems:
                    print "\t" + rFile

        else:
            cantP = str(len(problems))
            if (fix):
                self.posible_fix.append("Invalid names solved (" + cantP + ")")
                self.details.append("Invalid names solved")
                print "Invalid names fixed"
            else:
                self.posible_fix.append("Invalid name problems")
                self.details.append("Invalid name problems")
                print "Invalid names list"

            if len(problems) != 1:
                self.details.append("\t" + str(len(problems))+ " elements. Check Script Editor")
            else:
                self.details.append("\t" + str(len(problems))+ " element. Check Script Editor")

            for pEl in problems:
                print "\t" + pEl.longName()



