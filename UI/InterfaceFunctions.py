"""
Interface script.

Control all ui elements to modify and get signals
of buttons ands checkboxes marked.
"""

#from ..Core.Steps import Modeling, Animation, Rigging, Shading, VFX, Lighting

class InterfaceActions():

    """
    Control of UI elements.

    This class has methods that will return values of selected
    elements, checked box, or current elements to analize.
    """

    def __init__(self, window_interface, status_window, detail_window, ctrlObjects):
        """
        Start Interfaces control.

        This method creates buttons to analize what actions
        will evaluate the class.
        """
        # Create buttons identifiers main window
        self.btn_check = window_interface.btn_Check
        self.btn_ok = window_interface.btn_Ok
        self.btn_details = window_interface.btn_details
        self.tabs_window = window_interface.tabs_master
        self.btn_check_all = window_interface.chk_box_checkall

        # Create buttons identifiers detail window
        self.detail_btn_ok = detail_window.btn_ok
        self.detail_lbl_detail = detail_window.lbl_details
        self.win_details = detail_window

        # Make buttons connections
        self.btn_ok.clicked.connect(self.fix_elements)
        self.btn_details.clicked.connect(self.show_details)
        self.btn_check.clicked.connect(self.check_elements)
        self.btn_check_all.clicked.connect(self.mark_all)
        self.detail_btn_ok.clicked.connect(self.close_show_window)

        self.status_window = status_window
        self.master_window = window_interface
        self.status_lbl_status = status_window.lbl_status
        self.status_lbl_elements = status_window.lbl_elements
        self.status_progress_bar = status_window.progressBar_01
        self.status_lbl_step = status_window.lbl_step

        # Global value for the method check or uncheck all
        self.checkall = True

        # Conjunto de funciones por etapa
        #mdl_ins = Modeling.ModelingControls()
        mdl_ins = ctrlObjects["Modelling"]
        mdl_methods = [("Transformations", mdl_ins.transformations),
                       ("History", mdl_ins.history),
                       ("Hierarchy", mdl_ins.hierarchy),
                       ("Names", mdl_ins.names_method),
                       ("Materials", mdl_ins.materials),
                       ("UV Sets", mdl_ins.uv_sets),
                       ("Center", mdl_ins.center),
                       ("Unknown Nodes", mdl_ins.unknown_nodes),
                       ("Invalid Names", mdl_ins.invalid_names),
                       ("Feedback", mdl_ins.return_feedback)]

        #anim_ins = Animation.AnimationControls()
        anim_ins = ctrlObjects["Animation"]
        anim_methods = [("Atom Nodes", anim_ins.atom_nodes),
                        ("Unknown Nodes", anim_ins.unknown_nodes),
                        ("Non referenced", anim_ins.non_referenced),
                        ("Invalid Names", anim_ins.invalid_names),
                        ("Feedback", anim_ins.return_feedback)]

        #rig_ins = Rigging.RiggingControls()
        rig_ins = ctrlObjects["Rigging"]
        rig_methods = [("Unknown Nodes", rig_ins.unknown_nodes),
                       ("Non referenced", rig_ins.non_referenced),
                       ("Invalid Names", rig_ins.invalid_names),
                       ("Feedback", rig_ins.return_feedback)]

        #shd_ins = Shading.ShadingControls()
        shd_ins = ctrlObjects["Shading"]
        shd_methods = [("Repeated shaders", shd_ins.repeated_shaders),
                       ("External shaders", shd_ins.external_shaders),
                       ("Local Textures", shd_ins.local_textures),
                       ("Unknown Nodes", shd_ins.unknown_nodes),
                       ("Non referenced", shd_ins.non_referenced),
                       ("Invalid Names", shd_ins.invalid_names),
                       ("Feedback", shd_ins.return_feedback)]

        #vfx_ins = VFX.VfxControls()
        vfx_ins = ctrlObjects["Vfx"]
        vfx_methods = [("Unknown Nodes", vfx_ins.unknown_nodes),
                       ("Non referenced", vfx_ins.non_referenced),
                       ("Invalid Names", vfx_ins.invalid_names),
                       ("Feedback", vfx_ins.return_feedback)]

        #lgt_ins = Lighting.LightingControls()
        lgt_ins = ctrlObjects ["Lighting"]
        light_methods = [("External lights", lgt_ins.external_lights),
                         ("Unknown Nodes", lgt_ins.unknown_nodes),
                         ("Non referenced", lgt_ins.non_referenced),
                         ("Invalid Names", lgt_ins.invalid_names),
                         ("Feedback", lgt_ins.return_feedback)]

        # Array for different arraylists that contain
        # diferent methods oriented in a specific step.
        self.hub_methods = [mdl_methods, rig_methods,
                            anim_methods, light_methods,
                            shd_methods, vfx_methods]

        self.update_checkboxes_status()

    def get_step(self):
        """
        Detect step.

        Determinate which tab is selected or active
        in the MainWindow.
        """
        step_names = [
            "Modeling", "Rig", "Animation",
            "Lighting", "Shading", "VFX"]
        current_tab = self.tabs_window.currentIndex()
        step_info = [step_names[current_tab], current_tab]
        return step_info

    def scan_chekboxes(self, step_id, fix):
        """
        Scan all the checkboxes.

        Analize active check boxes from the widget selected.
        """
        self.update_checkboxes_status()

        self.check_element_status(step_id=step_id, fix=fix)

    def update_checkboxes_status(self):
        chk_modeling = [
            self.master_window.chk_mdl_transformation,
            self.master_window.chk_mdl_history,
            self.master_window.chk_mdl_hierarchy,
            self.master_window.chk_mdl_names,
            self.master_window.chk_mdl_materials,
            self.master_window.chk_mdl_uvSets,
            self.master_window.chk_mdl_center,
            self.master_window.chk_mdl_unknown,
            self.master_window.chk_mdl_invalidNames]

        chk_rig = [
            self.master_window.chk_rig_reference,
            self.master_window.chk_rig_unknown,
            self.master_window.chk_rig_invalidNames]

        chk_animation = [
            self.master_window.chk_anim_atom,
            self.master_window.chk_anim_reference,
            self.master_window.chk_anim_unknown,
            self.master_window.chk_anim_invalidNames]

        chk_lighting = [
            self.master_window.chk_light_external,
            self.master_window.chk_light_reference,
            self.master_window.chk_light_unknown,
            self.master_window.chk_light_invalidNames]

        chk_shading = [
            self.master_window.chk_shd_repeated,
            self.master_window.chk_shd_external,
            self.master_window.chk_shd_reference,
            self.master_window.chk_shd_textures,
            self.master_window.chk_shd_unknown,
            self.master_window.chk_shd_invalidNames]

        chk_vfx = [
            self.master_window.chk_vfx_reference,
            self.master_window.chk_vfx_unknown,
            self.master_window.chk_vfx_invalidNames]

        self.widget_groups_checkboxes = [
            chk_modeling, chk_rig, chk_animation,
            chk_lighting, chk_shading, chk_vfx]

        self.labels_fix_feedback = [
            self.master_window.lbl_mdl_fix,
            self.master_window.lbl_rig_fix,
            self.master_window.lbl_anim_fix,
            self.master_window.lbl_light_fix,
            self.master_window.lbl_shd_fix,
            self.master_window.lbl_vfx_fix]

        self.labels_ref_feedback = [
            self.master_window.lbl_mdl_reference,
            self.master_window.lbl_rig_reference,
            self.master_window.lbl_anim_reference,
            self.master_window.lbl_light_reference,
            self.master_window.lbl_shd_reference,
            self.master_window.lbl_vfx_reference]

    def check_element_status(self, step_id, fix):
        """
        Temp status method.

        Check all the checkboxes an call other methods
        depending of what elements are active.

        Operations
        "Transformations" "History" "Materials"
        "UV Sets" "Center"
        "Unknown Nodes" "Non referenced"
        "Atom Nodes" "External lights"
        "Repeated shaders" "External shaders"
        "Local Textures"
        """
        # Using an array that contains all the check boxes from
        # a specific window, this windows will be determinated by
        # the step_id.
        active_step = self.widget_groups_checkboxes[step_id]

        # Check all check boxes and call a method that will fix
        # or check depending on button clicked
        # this method will differenciate that with the fix
        # value.
        # fix = True --> Fix button pressed
        # fix = False -> Check button pressed
        active_methods = self.hub_methods[step_id]
        active_chkboxes = []
        for current_chk in active_step:
            if current_chk.isChecked():
                active_chkboxes.append(current_chk)

        # Initial state of processing window...
        process_cant = len(active_chkboxes)
        completed_task = 0
        cant_string = str(completed_task) + "/" + str(process_cant)
        self.status_window.lbl_elements.setText(cant_string)

        # Display processing window
        self.status_window.show()

        # Lock the intercae window until all tasks will be completed
        self.master_window.setEnabled(False)

        history = False
        history_method = active_methods[1]

        # Start all fixing or checking tasks
        for method in active_methods:
            for current_chk in active_chkboxes:
                if current_chk.text() == method[0]:
                    # Using the method!
                    if current_chk.text() == "History":
                        history = True
                        history_method = method[1]

                    method[1](fix=fix)

                    completed_task = completed_task + 1
                    cant_string = str(completed_task) + "/" + str(process_cant)
                    self.status_window.lbl_elements.setText(cant_string)
                    if (process_cant is not 0):
                        percentage = (completed_task / process_cant) * 100
                        self.status_window.progressBar_01.setValue(percentage)
        if history and fix:
            #print('Testing history method')
            history_method(fix=fix)

        # Use the method "return_feedback" tu get two strings with all
        # Details generated in each method
        arrayfeedbacks = active_methods[len(active_methods) - 1]
        feedbacks = arrayfeedbacks[1]()
        feedbackfix = ""
        feedbackref = ""
        feedbackdetails = ""

        for i in feedbacks[0]:
            feedbackfix = feedbackfix + "\n" + i

        for i in feedbacks[1]:
            feedbackref = feedbackref + "\n" + i

        for i in feedbacks[2]:
            feedbackdetails = feedbackdetails + "\n" + i

        self.master_window.setEnabled(True)
        # self.status_window.hide()
        self.status_window.close()

        self.labels_fix_feedback[step_id].setText(feedbackfix)
        self.labels_ref_feedback[step_id].setText(feedbackref)
        self.detail_lbl_detail.setText(feedbackdetails)

    def mark_all(self):
        """
        Check uncheck master.

        Mark or unmark all the checkboxes.
        """
        active_index = self.get_step()[1]

        for checkbox in self.widget_groups_checkboxes[active_index]:
            checkbox.setChecked(self.checkall)
        if not self.checkall:
            self.btn_check_all.setText("Check all")
        else:
            self.btn_check_all.setText("Uncheck all")
        self.checkall = not self.checkall

    def show_details(self):
        """
        Show detail window.

        This method will display the details window
        and show a complete description for all problems in the scene
        this description will be given by every method called
        in the script.
        """
        self.win_details.show()

    def close_show_window(self):
        """
        Close details window.

        This method should be calle by the Ok
        button in the show window!
        """
        self.win_details.close()

    def check_elements(self):
        """
        Analiaze indicated elements.

        Analiza the elements selected indicated with the checkboxes and
        the context given by the active widget tab.
        """
        step_info = self.get_step()
        step_name = step_info[0]
        step_index = step_info[1]
        self.status_lbl_step.setText(step_name)
        self.status_lbl_status.setText("...Checking...")
        self.scan_chekboxes(step_index, fix=False)

    def fix_elements(self):
        """
        Ok button method.

        Description.
        """
        step_info = self.get_step()
        step_name = step_info[0]
        step_index = step_info[1]
        self.status_lbl_step.setText(step_name)
        self.status_lbl_status.setText("...Fixing...")
        self.scan_chekboxes(step_index, fix=True)


        
