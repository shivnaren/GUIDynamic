from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DD import ScrollableLF, databaseadmin, LoadDatabase

root = Tk()

root.geometry("1366x705+0+0")
root.title("Top Frame")
root.configure(background="white")

#################################################################################
# Frames
#################################################################################
Header_F = Frame(root)
Header_F.place(relx=0.0, rely=0.0, relheight=0.106, relwidth=0.999)
Header_F.configure(borderwidth="2")
Header_F.configure(borderwidth="2")
Header_F.configure(background="#d9d9d9")
Header_F.configure(width=1366)

Components_F = ttk.LabelFrame(root, text="Components")
Components_F.place(relx=0.0, rely=0.113, relheight=0.887, relwidth=0.248)
Components_F.configure(borderwidth="2")
# Components_F.configure(background="#d9d9d9")
Components_F.configure(width=525)

Communication_F = ttk.LabelFrame(root, text="Communication")
Communication_F.place(relx=0.250, rely=0.113, relheight=0.395, relwidth=0.333)
Communication_F.configure(borderwidth="2")
# Communication_F.configure(background="#d9d9d9")
Communication_F.configure(width=455)

Destination_F = ttk.LabelFrame(root, text="Destinations")
Destination_F.place(relx=0.250, rely=0.514, relheight=0.380, relwidth=0.333)
# Destination_F.configure(background="#d9d9d9")
Destination_F.configure(width=455)

Actions_LF = ttk.LabelFrame(root)
Actions_LF.place(relx=0.586, rely=0.113, relheight=0.780, relwidth=0.115)
# Actions_LF.configure(foreground="black")
Actions_LF.configure(text='Action')
# Actions_LF.configure(background="#d9d9d9")
Actions_LF.configure(width=780)

ExtRole_Dest_LF = ttk.LabelFrame(root )
ExtRole_Dest_LF.place(relx=0.704, rely=0.113, relheight=0.427, relwidth=0.285)
ExtRole_Dest_LF.configure(relief='flat')
# ExtRole_Dest_LF.configure(foreground="black")
ExtRole_Dest_LF.configure(text='ExternalRoles')
# ExtRole_Dest_LF.configure(background="#d9d9d9")
ExtRole_Dest_LF.configure(width=600)

DynamicDest_Scrollable_LF = ScrollableLF.Scrollable(ExtRole_Dest_LF)
ExternalRole_Lable = ttk.Label(DynamicDest_Scrollable_LF, text = 'External Role', background = 'White')
ExternalRole_Lable.grid(row = 0, column = 0, padx = 10)
# ExternalRole_Lable.place(relx=0.01, rely=0.0, relheight=0.100, relwidth=0.300)

GroupBy_Lable = ttk.Label(DynamicDest_Scrollable_LF, text = 'Group By', background = 'White')
GroupBy_Lable.grid(row =0, column = 1, padx = 50)
# GroupBy_Lable.place(relx=0.45, rely=0.0, relheight=0.100, relwidth=0.300)

# ExtRole_Dest_LF.update_idletasks()


System_Dest_LF = ttk.LabelFrame(root)

System_Dest_LF.place(relx=0.704, rely=0.546, relheight=0.191, relwidth=0.285)
System_Dest_LF.configure(relief='groove')
System_Dest_LF.configure(text='SystemDestations')
System_Dest_LF.configure(width=360)

SystemDest_Scrollable_LF = ScrollableLF.Scrollable(System_Dest_LF)

Manual_Dest_LF = ttk.LabelFrame(root)
Manual_Dest_LF.place(relx=0.704, rely=0.745, relheight=0.149, relwidth=0.285)
Manual_Dest_LF.configure(relief='groove')
Manual_Dest_LF.configure(text='Manual Destinations')
Manual_Dest_LF.configure(width=360)

ManualDest_Scrollable_LF = ScrollableLF.Scrollable(Manual_Dest_LF)


def OnTopLevelDeleteButtonClick(event=None):

    deleteresult = databaseadmin.delete_dest_val(databasename, ComponentType_Filtered,
                                                 ComponentName_Selected,
                                                 CommunicationName_Selected,
                                                 DestinationValue_Selected,
                                                 isResponseUserRoleChecked)
    for widget in delete_configure_Win_popup.winfo_children():
        widget.destroy()
    delete_configure_Win_popup.withdraw()


    messagebox.showinfo('Destination Delete', 'Destination(s) Removed Successfuly')





delete_configure_Win_popup = Toplevel(width = 1300, height = 300, bg = 'white')

delete_configure_Win_popup.withdraw()

def OnCloseButton(event= None):
    if len(Dynamic_Dest_Config_Values) > 0:
        Dynamic_Dest_Config_Values.clear()
    for widget in delete_configure_Win_popup.winfo_children():
        widget.destroy()
    delete_configure_Win_popup.withdraw()




def OnDeleteBtnClick(event=None):

    if len(DestinationValue_Selected) == 0:
        messagebox.showinfo('Information', 'Please Select The Destination Value To Delete')
    else:


        if delete_configure_Win_popup.state() == 'normal':
            for widget in delete_configure_Win_popup.winfo_children():
                widget.destroy()

            delete_configure_Win_popup.withdraw()


        delete_configure_Win_popup.wm_title("Deleting Destination Value")
        delete_configure_Win_popup.deiconify()

        def donothing():
            pass

        delete_configure_Win_popup.protocol('WM_DELETE_WINDOW', donothing)
        # delete_configure_Win_popup.wm_attributes("-topmost", 1)

        tree = ttk.Treeview(delete_configure_Win_popup,
                            columns=("ComponentName",
                                     "CommunicationName",
                                     "DestinationValue",
                                     "DestinationType",
                                     "DestinationSource",),
                            style="mystyle.Treeview")

        # tree.pack(fill=BOTH, expand=True)
        tree.place(relx=0.0, rely=0.0, relheight=0.600, relwidth=0.999)

        close_Button = Button(delete_configure_Win_popup, text="Close", command=OnCloseButton)
        # close_Button.pack(side=LEFT, padx=300)
        close_Button.place(relx=0.30, rely=0.75, relheight=0.10, relwidth=0.05)

        Delete_Button = Button(delete_configure_Win_popup, text="Delete", command=OnTopLevelDeleteButtonClick)
        # Delete_Button.pack(side=RIGHT, padx=300)
        Delete_Button.place(relx=0.70, rely=0.75, relheight=0.10, relwidth=0.05)

        tree['show'] = 'headings'

        tree.heading("ComponentName", text="Component Name")
        tree.heading("CommunicationName", text="Communication Name")
        tree.heading("DestinationValue", text="Destination Value")
        tree.heading("DestinationType", text="Destination Type")
        tree.heading("DestinationSource", text="Destination Source")

        tree.column("ComponentName", anchor=CENTER, minwidth=0, width=100, stretch=YES)
        tree.column("CommunicationName", anchor=CENTER, width=100)
        tree.column("DestinationType", anchor=CENTER, width=50)
        tree.column("DestinationValue", anchor=CENTER, width=100)
        tree.column("DestinationSource", anchor=CENTER, width=100)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 10, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        tree.insert("", "end", 0, text="", values=(ComponentName_Selected,
                                                   CommunicationName_Selected,
                                                   DestinationValue_Selected[2],
                                                   DestinationValue_Selected[0],
                                                   DestinationValue_Selected[1]),
                    )

        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#DFDFDF')
    # messagebox.showinfo('Destination Delete', 'Destination(s) Removed Successfuly')


Delete_Button = ttk.Button(root)
Delete_Button.place(relx=0.330, rely=0.920, height=34, width=77, bordermode='ignore')
Delete_Button.configure(text='''Delete''')
Delete_Button.configure(width=77)
Delete_Button.configure(state=DISABLED)
Delete_Button.configure(command=OnDeleteBtnClick)


def OnTopLevelConfigureButtonClick(event=None):
    databaseadmin.Configure_Destinations(databasename, Dynamic_Dest_Config_Values)
    for widget in delete_configure_Win_popup.winfo_children():
        widget.destroy()
    for widget in DynamicDest_Scrollable_LF.winfo_children():
        widget.destroy()
    for widget in SystemDest_Scrollable_LF.winfo_children():
            widget.destroy()
    for widget in ManualDest_Scrollable_LF.winfo_children():
        widget.destroy()
    SystemDestinations_selected_list.clear()



    delete_configure_Win_popup.withdraw()
    messagebox.showinfo('Destination Configure', 'Destination(s) Configured Successfuly')

def is_dynamicEmptyCombobox(Dynamic_Dest_list):
    for key, dynamdest in Dynamic_Dest_list.items():
        if dynamdest[0].get() == '' or dynamdest[1].get() == '':
            return True
        else:
            return False

def is_StaticEmptyCombobox(SystemDestinations_selected_list):
    for key, sysdest in SystemDestinations_selected_list.items():
        if sysdest.get() == '':
            return True
        else:
            return False

def is_ManualEmptyCombobox(ManualDestinations_list):
    for key, manualdest in ManualDestinations_list.items():
        if manualdest.get() == '':
            return True
        else:
            return False



Dynamic_Dest_Config_Values = []

def OnPreviewButtonClick(event=None):

    if DataBaseFilter_cb.get() == '':
        # An information box

        messagebox.showwarning("Warning", "Please Select a Database Before Adding the ExternalRole and Group By")
    elif ComponentName_Selected == '':
        messagebox.showinfo('information', 'Please Select The Component Name')
    elif CommunicationName_Selected == '':
        messagebox.showinfo('information', 'Please Select the Communication Name')
    elif len(Dynamic_Dest_list) == 0 and len(ManualDestinations_list) == 0 and len(SystemDestinations_selected_list) == 0:
        messagebox.showinfo('information', 'Please Add either of Dynamic/System/Manual Destination Type to Proceed')
    elif len(Dynamic_Dest_list) > 0 and is_dynamicEmptyCombobox(Dynamic_Dest_list) == True:
        messagebox.showinfo('information', 'You have added a Dynamic Destionation, but not selected any value. Please select atlease one value or delete it')
    elif len(ManualDestinations_list) > 0 and is_ManualEmptyCombobox(ManualDestinations_list) == True:
        messagebox.showinfo('information',
                            'You have added a Manual Destination, but not selected any value. Please select atlease one value or delete it')

    elif len(SystemDestinations_selected_list) > 0 and is_StaticEmptyCombobox(SystemDestinations_selected_list) == True:
        messagebox.showinfo('information',
                            'You have added a Static Destination, but not selected any value. Please select atlease one value or delete it')

    else:

        if delete_configure_Win_popup.state() == 'normal':
            for widget in delete_configure_Win_popup.winfo_children():
                widget.destroy()

            delete_configure_Win_popup.withdraw()
        delete_configure_Win_popup.deiconify()
        delete_configure_Win_popup.wm_title("Configuring the Destination Values")


        def donothing():
            pass

        delete_configure_Win_popup.protocol('WM_DELETE_WINDOW', donothing)


        tree = ttk.Treeview(delete_configure_Win_popup,
                            columns=("ComponentType",
                                     "ComponentName",
                                     "CommunicationName",
                                     "DestinationValue",
                                     "ExternalRole",
                                     "GroupBy",
                                     "DestinationSource",),
                            style="mystyle.Treeview")
        tree.pack(fill=BOTH, expand=True)

        close_Button = Button(delete_configure_Win_popup, text="Close", command=OnCloseButton)
        close_Button.pack(side=LEFT, padx=300)

        Delete_Button = Button(delete_configure_Win_popup, text="Configure", command=OnTopLevelConfigureButtonClick)
        Delete_Button.pack(side=RIGHT, padx=300)

        tree['show'] = 'headings'

        tree.heading("ComponentType", text="Component Type")
        tree.heading("ComponentName", text="Component Name")
        tree.heading("CommunicationName", text="Communication Name")
        tree.heading("DestinationValue", text="Destination Value")
        tree.heading("ExternalRole", text="External Role")
        tree.heading("DestinationSource", text="Destination Source")
        tree.heading("GroupBy", text="Group By")

        tree.column("ComponentType", anchor=CENTER, minwidth=0, width=5, )
        tree.column("ComponentName", anchor=CENTER, minwidth=0, width=100, stretch=YES)
        tree.column("CommunicationName", anchor=CENTER, width=100)
        tree.column("DestinationValue", anchor=CENTER, width=100)
        tree.column("ExternalRole", anchor=CENTER, width=15)
        tree.column("GroupBy", anchor=CENTER, width=15)
        tree.column("DestinationSource", anchor=CENTER, width=15)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 10, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders



        for key, sysdest in SystemDestinations_selected_list.items():
            Dynamic_Dest_Config_Values.append((ComponentType_Filtered, ComponentName_Selected, CommunicationName_Selected,
                                               sysdest.get(), None, None, "Field"))

        for key, manudest in ManualDestinations_list.items():
            Dynamic_Dest_Config_Values.append((ComponentType_Filtered,
                                               ComponentName_Selected,
                                               CommunicationName_Selected,
                                               manudest.get(),
                                               None,
                                               None,
                                               "Manual"))
        for key, dynamdest in Dynamic_Dest_list.items():

            Dynamic_Dest_Config_Values.append((ComponentType_Filtered,
                                               ComponentName_Selected,
                                               CommunicationName_Selected,
                                               'CBS_DEST_UR_Role ' + str(
                                                   databaseadmin.get_externalroleid(databasename, dynamdest[0].get())[
                                                                             0][0]) + '_' + dynamdest[1].get()
                                               ,
                                               dynamdest[0].get(),
                                               dynamdest[1].get(),
                                               "Rule"))



        for dest in Dynamic_Dest_Config_Values:
            # pass
            # tree.insert("", "end", 0, text="", values=(ComponentType_Filtered,
            #                                       ComponentName_Selected,
            #                                       CommunicationName_Selected,
            #                                       DestinationValue_Selected,
            #                                       ExternalRole,
            #                                       GroupBy,
            #                                       DestinationValue_Source_Selected)
            #                                      )
            tree.insert("", "end", text="", values=(dest[0],
                                                    dest[1],
                                                    dest[2],
                                                    dest[3],
                                                    dest[4],
                                                    dest[5],
                                                    dest[6])
                        )


        # tree.tag_configure('odd', background='#E8E8E8')
        # tree.tag_configure('even', background='#DFDFDF')


Preview_Button = ttk.Button(root)
Preview_Button.place(relx=0.893, rely=0.920, height=34, width=77)
Preview_Button.configure(text='''Preview''')
Preview_Button.configure(command=OnPreviewButtonClick)

global isResponseUserRoleChecked
isResponseUserRoleChecked = 0
# CheckVar2.set(0)

def onResponseByUserRoleCheck(event=None):
    isResponseUserRoleChecked = var.get()



var = IntVar()
ResponseByUserRole_CB = Checkbutton(root, text="Response By User Role", variable=var, command=onResponseByUserRoleCheck)
ResponseByUserRole_CB.place(relx=0.450, rely=0.920, height=34, width=180, bordermode='ignore')

isResponseUserRoleChecked = var.get()
global System_Dest_row
System_Dest_row = 0

# Sys_dest_selected_list = list()





SystemDest_list = ['StudyVariable.ExternalUserPrimaryEmail',
                   'Site.ConsigneeEmail',
                   'Site.MainContactEmail']

SystemDestinations_selected_list = {}
def OnSysDestdeleteButtonClick(event, System_Dest_cb):
    w= event.widget

    SystemDestinations_selected_list.pop(w.grid_info()['row'], None)
    w.destroy()
    System_Dest_cb.destroy()


def fn_SystemDest():
    global System_Dest_row
    System_Dest_col = 0
    if DataBaseFilter_cb.get() == '':
        # An information box

        messagebox.showwarning("Warning", "Please Select a Database Before Adding the System Destination")

    else:
        System_Dest_cb = ttk.Combobox(SystemDest_Scrollable_LF, values=SystemDest_list)
        System_Dest_cb.grid(row=System_Dest_row, column=System_Dest_col, padx=10, pady = 5)

        SystemDestinations_selected_list[System_Dest_row] = (System_Dest_cb)
        # System_Dest_cb.bind('<<ComboboxSelected>>', OnSystemDest_SameValue_Select)
        deletebutton = Button(SystemDest_Scrollable_LF, text="X")
        deletebutton.grid(row=System_Dest_row, column=System_Dest_col + 1, padx=10, pady = 5)
        deletebutton.bind('<Button-1>', lambda event: OnSysDestdeleteButtonClick(event, System_Dest_cb))

        System_Dest_cb.configure(width=15)

        System_Dest_row += 1
        SystemDest_Scrollable_LF.update()




global Dynamic_Dest_row_cb
# Dynamic_Dest_row_cb = 0.110
Dynamic_Dest_row_cb = 5

Dynamic_Dest_list = {}

def OnDynamicDestdeleteButtonClick(event, ExternalRole_cb, GroupBy_cb):
    w= event.widget


    Dynamic_Dest_list.pop(w.grid_info()['row'], None)
    w.destroy()
    ExternalRole_cb.destroy()
    GroupBy_cb.destroy()

def fn_DynamicDest():

    global Dynamic_Dest_row_cb
    ExternalRole_Cb_column = 0
    GroupBy_Cb_column = 1
    if DataBaseFilter_cb.get() == '':
        # An information box

        messagebox.showwarning("Warning", "Please Select a Database Before Adding the ExternalRole and Group By")

    else:
        ExtRoles = []
        for extrole in databaseadmin.get_externalroles(databasename):
            ExtRoles.append(extrole[0])

        groupbyValues = ['Site','SiteCountry','SiteRegion','Depot_Receiving','Depot_Shipping','Globally']
        # for groupby in databaseadmin.get_groupbyvalues():
        #     groupbyValues.append(groupby[0])

        ExternalRole_cb = ttk.Combobox(DynamicDest_Scrollable_LF, values=ExtRoles)
        GroupBy_cb = ttk.Combobox(DynamicDest_Scrollable_LF, values=groupbyValues, width = 10)
        ExternalRole_cb.grid(row=Dynamic_Dest_row_cb, column=ExternalRole_Cb_column, padx=5, pady=5)
        # ExternalRole_cb.place(relx=0.01, rely=Dynamic_Dest_row_cb, relheight=0.106, relwidth=0.300)
        GroupBy_cb.grid(row=Dynamic_Dest_row_cb, column=GroupBy_Cb_column, padx=5, pady=5)

        deletebutton = Button(DynamicDest_Scrollable_LF, text="X")
        deletebutton.grid(row=Dynamic_Dest_row_cb, column=GroupBy_Cb_column + 1, pady=5)
        deletebutton.bind('<Button-1>', lambda event: OnDynamicDestdeleteButtonClick(event, ExternalRole_cb,GroupBy_cb))
        Dynamic_Dest_list[Dynamic_Dest_row_cb] = [ExternalRole_cb, GroupBy_cb]
        Dynamic_Dest_row_cb += 1
        DynamicDest_Scrollable_LF.update()


global Manual_row
Manual_row = 0

ManualDestinations_list = {}
def OnManualdeleteButtonClick(event,Manual_Dest_E ):

    w = event.widget
    ManualDestinations_list.pop(w.grid_info()['row'], None)
    w.destroy()
    Manual_Dest_E.destroy()

def fn_ManualDest():
    global Manual_row
    Manual_Dest_col = 0
    if DataBaseFilter_cb.get() == '':
        # An information box

        messagebox.showwarning("Warning", "Please Select a Database Before Adding the Manual Destintion")

    else:
        Manual_Dest_E = Entry(ManualDest_Scrollable_LF)
        Manual_Dest_E.grid(row=Manual_row, column=Manual_Dest_col, padx=10)
        deletebutton = Button(ManualDest_Scrollable_LF, text="X")
        deletebutton.grid(row=Manual_row, column=Manual_Dest_col + 1, padx=10)
        deletebutton.bind('<Button-1>', lambda event: OnManualdeleteButtonClick(event, Manual_Dest_E))
        ManualDestinations_list[Manual_row] = Manual_Dest_E

        Manual_row += 1
        ManualDest_Scrollable_LF.update()


def onActionSelect():
    radioValue = Radio_var.get()

    if radioValue == 1:
        fn_SystemDest()
    if radioValue == 2:
        fn_ManualDest()
    if radioValue == 3:
        fn_DynamicDest()


Radio_var = IntVar()

Dynamic_Dest_RB = ttk.Radiobutton(Actions_LF, variable=Radio_var, val=3)
Dynamic_Dest_RB.place(relx=0.06, rely=0.250, relheight=0.070, relwidth=0.850, bordermode='ignore')

# Dynamic_Dest_RB.configure(background="#d9d9d9")
# Dynamic_Dest_RB.configure(justify='left')
Dynamic_Dest_RB.configure(text='''Dynamic Destination''')
# Dynamic_Dest_RB.deselect()

System_Dest_RB = ttk.Radiobutton(Actions_LF, variable=Radio_var, val=1)
System_Dest_RB.place(relx=0.06, rely=0.600, relheight=0.070, relwidth=0.850, bordermode='ignore')

# System_Dest_RB.configure(background="#d9d9d9")
# System_Dest_RB.configure(justify='left')
System_Dest_RB.configure(text='''System Destination''')
System_Dest_RB.configure(width=100)
# System_Dest_RB.deselect()

Manual_Dest_RB = ttk.Radiobutton(Actions_LF, variable=Radio_var, val=2)
Manual_Dest_RB.place(relx=0.06, rely=0.850, relheight=0.070, relwidth=0.850)
# Manual_Dest_RB.configure(background="#d9d9d9")
# Manual_Dest_RB.configure(justify='left')
Manual_Dest_RB.configure(text='''Manual Destination''')
Manual_Dest_RB.configure(width=148)
# Manual_Dest_RB.deselect()



Destination_Add_Button = ttk.Button(root, command=onActionSelect)
Destination_Add_Button.place(relx=0.630, rely=0.920, height=34, width=77, bordermode='ignore')
Destination_Add_Button.configure(text='''Add''')

#################################################################################
# Header Frame  widgets
#################################################################################
global DestinationValue_Selected
DestinationValue_Selected = []


def onDestinationSelect(event=None):
    # print("in Destination Select")
    if event:
        # print("in Destination Select Event Happend")
        global DestinationValue_Selected
        Delete_Button.configure(state=ACTIVE)
        curItem = DestinationValues_tree.focus()
        DestinationValue_Selected = DestinationValues_tree.item(curItem)['values']
        # print(DestinationValue_Selected)

        # print(DestinationValues_tree.item(DestinationValues_tree.selection())['values'])

        # for item in event.widget.selection():
        #     item_text = event.widget.item(item, "text")
        #     print(item_text)


global CommunicationName_Selected
CommunicationName_Selected = ''


def onCommunicationSelect(event=None):
    global CommunicationName_Selected

    if event:

        if len(DestinationValues_tree.get_children()) > 0:
            DestinationValues_tree.delete(*DestinationValues_tree.get_children())
        # print("in Communication")
        # if DestinationListbox.size() == 0:
        #     pass
        # else:
        #     DestinationListbox.delete(0, END)

        w = event.widget
        if len(w.curselection()) > 0:
            CommunicationName = w.get(int(w.curselection()[0]))
            CommunicationName_Selected = CommunicationName
            # Destinations = databaseadmin.get_Destination(CommunicationName, ComponentType_Filtered)

            # print(CommunicationName)
            Destinations = databaseadmin.get_Destination(databasename, CommunicationName, ComponentType_Filtered)
            for eachDest in Destinations:
                DestinationValues_tree.insert("", "end", text="", values=(eachDest[0], eachDest[1], eachDest[2]))


global ComponentName_Selected
ComponentName_Selected = ''


def onComponentSelect(event=None):
    if event:
        global ComponentName_Selected
        # print("in Component")
        if CommunicationListbox.size() == 0:
            pass
        else:
            CommunicationListbox.delete(0, END)
        w = event.widget
        if len(w.curselection()) > 0:
            ComponentName = w.get(int(w.curselection()[0]))
            ComponentName_Selected = ComponentName
            Dependency_Communications = databaseadmin.get_communication(databasename, ComponentName, ComponentType_Filtered)

            # print(ComponentName)

            for communicationname in range(0, len(Dependency_Communications)):
                CommunicationListbox.insert(communicationname, Dependency_Communications[communicationname][0])

    # print('You selected item %d: "%s"' % (index, value))


global ComponentType_Filtered
ComponentType_Filtered = ''


def OnComponentFilter(event=None):
    # if event:
    #     print(event.widget.get())
    global ComponentType_Filtered
    # print(DataBaseFilter_cb.get())
    if event:
        if DataBaseFilter_cb.get() == '':
            # An information box

            messagebox.showinfo("Information", "Please Select a Database Before Filter Component Type ")
        else:
            if ComponentsListbox.size() == 0:
                pass
            else:
                ComponentsListbox.delete(0, END)

            ComponentType_Filtered = event.widget.get()
            if event.widget.get() == 'Forms':
                studyforms = databaseadmin.get_component_form(databasename)
                for formname in range(0, len(studyforms)):
                    ComponentsListbox.insert(formname, studyforms[formname][0])
            elif event.widget.get() == 'Tasks':
                studytasks = databaseadmin.get_component_task(databasename)
                for taskname in range(0, len(studytasks)):
                    ComponentsListbox.insert(taskname, studytasks[taskname][0])


CommunicationListbox = Listbox(Communication_F, selectmode=SINGLE, exportselection=False)
CommunicationListbox.bind('<<ListboxSelect>>', onCommunicationSelect)
CommunicationListbox.grid(row=1, column=1)
CommunicationListbox.config(width=74, height=16)

ComponentsListbox = Listbox(Components_F, selectmode=SINGLE, exportselection=False)
ComponentsListbox.bind('<<ListboxSelect>>', onComponentSelect)
ComponentsListbox.config(width=55, height=38)

ComponentsListbox.grid(row=1, column=1)

##########################################################################################################################
# Destinations Frame Widgets  Start
########################################################################################################

DestinationValues_tree = ttk.Treeview(Destination_F,
                                      columns=("DestinationType",
                                               "DestinationSource",
                                               "DestinationValue"),
                                      style="mystyle.Treeview")

DestinationValues_tree.pack(fill=BOTH, expand=True)

DestinationValues_tree.bind("<<TreeviewSelect>>", onDestinationSelect)
DestinationValues_tree['show'] = 'headings'

DestinationValues_tree.heading("DestinationType", text="Destination Type")
DestinationValues_tree.heading("DestinationSource", text="Destination Source")
DestinationValues_tree.heading("DestinationValue", text="Destination Value")

DestinationValues_tree.column("DestinationType", anchor=CENTER, width=15)
DestinationValues_tree.column("DestinationSource", anchor=CENTER, width=23)
DestinationValues_tree.column("DestinationValue", anchor=CENTER, width=150)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 10, 'bold'))  # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

DestinationValues_tree.tag_configure('odd', background='#E8E8E8')
DestinationValues_tree.tag_configure('even', background='#DFDFDF')

##########################################################################################################################
# Destinations Frame Widgets  END
########################################################################################################
global databasename
databasename = ''
def OnDatabaseFilter(event):
    global databasename
    if event:
        databasename = str(event.widget.get())
        DB_Conn_Info_Label = ttk.Label(Header_F, text='')
        DB_Conn_Info_Label.place(relx=0.590, rely=0.620, relheight=0.300, relwidth=0.150)
        DB_Conn_Info_Label.config(text = 'Connected Database: '+str(databasename))
        DB_Conn_Info_Label.config(background = 'Orange')
        # print(databasename)
#
# databasenames = []
# def loadDatabase():
#     print("calling inside database load event and calling function to load database names")
#     for database in databaseadmin.getdatabase_name():
#         databasenames.append(database[0])
#     print(databasenames)
#     return databasenames

ComponentFilter = ttk.Label(Header_F, text="Component Type")
# ComponentFilter.grid(row=1, column=1)

ComponentFilter.place(relx=0.010, rely=0.200, relheight=0.300, relwidth=0.090)

ComponentsFilter_cb = ttk.Combobox(Header_F, values=('Forms', 'Tasks', 'Modules'))
# ComponentsFilter_cb.grid(row=1, column=2)
ComponentsFilter_cb.place(relx=0.110, rely=0.200, relheight=0.300, relwidth=0.090)
ComponentsFilter_cb.bind('<<ComboboxSelected>>', OnComponentFilter)


DataBaseFilter = ttk.Label(Header_F, text="DataBase")
# ComponentFilter.grid(row=1, column=1)
DataBaseFilter.place(relx=0.590, rely=0.200, relheight=0.300, relwidth=0.090)


DataBaseFilter_cb = ttk.Combobox(Header_F, values=tuple(LoadDatabase.loadDatabase()))
# ComponentsFilter_cb.grid(row=1, column=2)
DataBaseFilter_cb.place(relx=0.690, rely=0.200, relheight=0.300, relwidth=0.090)
DataBaseFilter_cb.bind('<<ComboboxSelected>>', OnDatabaseFilter)







# def close_window():
#     # for key, value in ManualDestinations_list.items():
#     #     print(value.get())
#     # for key, value in SystemDestinations_list.items():
#     #     print(value.get())
#     # for key, value in Dynamic_Dest_list.items():
#     #     for i in range(len(value)):
#     #         print(value[i].get())
#     print(ComponentType_Filtered)
#
# root.protocol("WM_DELETE_WINDOW", close_window)

root.mainloop()


