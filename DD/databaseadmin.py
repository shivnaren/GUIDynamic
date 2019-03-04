__author__ = 'user'
from . import connection


def getdatabase_name(dbname):
    databasename_sql = "SELECT name FROM sys.databases"
    databases_res = connection.execute_InsertSelect_sql(dbname, databasename_sql)
    databasenames = []
    for database in databases_res:
        databasenames.append(database[0])
    return databasenames


def get_component_form(dbname):
    sql = "Select formname , formguid from study.StudyForm order by 1"
    forms_res = connection.execute_InsertSelect_sql(dbname, sql)
    return forms_res

def get_component_task(dbname):
    sql = "Select name , taskguid from study.Studytask"
    task_res = connection.execute_InsertSelect_sql(dbname, sql)
    return task_res

def get_communication(dbname,componentname, componentType):
    dependency_Communication_res= ''
    if componentType == 'Forms':
        forms_sql = """ SELECt c.name , c.communicationguid FROM study.StudyForm SF JOIN [dbo].[ComponentDependency] CD
ON cd.SourceCompGUID =  CONVERT (NVARCHAR(100), sf.Formguid) JOIN dbo.communication c ON c.communicationguid = CD.DependentCompGUID
 WHERE SF.FormName = ?"""

        dependency_Communication_res = connection.execute_InsertSelect_sql(dbname, forms_sql, componentname)

    elif componentType == 'Tasks':
        tasks_sql = """SELECt c.name, c.communicationguid 
FROM study.StudyTask ST JOIN [dbo].[ComponentDependency] CD 
ON cd.SourceCompGUID =  CONVERT (NVARCHAR(100), ST.Taskguid) 
JOIN dbo.communication c ON c.communicationguid = CD.DependentCompGUID
WHERE ST.Name = ? """
        dependency_Communication_res = connection.execute_InsertSelect_sql(dbname, tasks_sql, componentname)
    return dependency_Communication_res

def get_Destination(dbname,Communication_name, componentType):
    dependency_dest_res = ''
    if componentType == 'Forms':
        forms_comm_dest_sql = """SELECt CASE WHEN fd.DestinationType = 0 AND fd.DestinationValueType = 0 THEN 'Fax'
			ELSE 'Email'
			END as DetinationType, 

	   CASE WHEN fd.DestinationType = 1 AND fd.DestinationValueType = 1 THEN 'Field'
			WHEN fd.DestinationType = 1 AND fd.DestinationValueType = 0 THEN 'Manual'
			ELSE 'Rule'
			END as DetinationSource,
	   
CASE when fd.destinationtype = 1 and (fd.destinationvaluetype = 1  OR fd.destinationvaluetype = 0) Then fd.destinationvalue
            when fd.destinationtype = 1 and fd.destinationvaluetype = 2 Then  sr.rulename
			ELSE fd.destinationvalue
			END as DetinationValue
 FROM study.StudyForm SF JOIN [dbo].[ComponentDependency] CD 
ON cd.SourceCompGUID =  CONVERT (NVARCHAR(100), sf.Formguid) 
JOIN dbo.communication c ON c.communicationguid = CD.DependentCompGUID
JOIN study.Notification N on N.CommunicationGUID = c.communicationguid
JOIN Study.NotificationDestinationAssociation Nd on Nd.NotificationId = N.NotificationId
JOIN study.formdestination FD ON FD.Destinationguid = ND.Destinationguid
left JOIN study.StudyRule SR ON  CONVERT (NVARCHAR(100), SR.StudyRuleGUID) = fd.destinationvalue
WHERE DependentCompType = 'Communication' AND
c.name = ?"""
        dependency_dest_res = connection.execute_InsertSelect_sql(dbname, forms_comm_dest_sql, Communication_name)
    elif componentType == 'Tasks':
        tasks_comm_dest_sql = """SELECT 
            CASE WHEN fd.DestinationType = 0 AND fd.DestinationValueType = 0 THEN 'Fax'
			     ELSE 'Email'
			     END as DetinationType, 

	        CASE WHEN fd.DestinationType = 1 AND fd.DestinationValueType = 1 THEN 'Field'
			     WHEN fd.DestinationType = 1 AND fd.DestinationValueType = 0 THEN 'Manual'
			     ELSE 'Rule'
			     END as DetinationSource,
	   
            CASE WHEN fd.destinationtype = 1 and (fd.destinationvaluetype = 1  OR fd.destinationvaluetype = 0) Then fd.destinationvalue
                 WHEN fd.destinationtype = 1 and fd.destinationvaluetype = 2 Then  sr.rulename
			     ELSE fd.destinationvalue
			     END as DetinationValue
 FROM study.StudyTask ST JOIN [dbo].[ComponentDependency] CD 
ON cd.SourceCompGUID =  CONVERT (NVARCHAR(100), ST.Taskguid) 
JOIN dbo.communication c ON c.communicationguid = CD.DependentCompGUID
JOIN study.Notification N on N.CommunicationGUID = c.communicationguid
JOIN Study.NotificationDestinationAssociation Nd on Nd.NotificationId = N.NotificationId
JOIN study.formdestination FD ON FD.Destinationguid = ND.Destinationguid
left JOIN study.StudyRule SR ON  CONVERT (NVARCHAR(100), SR.StudyRuleGUID) = fd.destinationvalue
WHERE DependentCompType = 'Communication' AND
c.name = ? """
        dependency_dest_res = connection.execute_InsertSelect_sql(dbname, tasks_comm_dest_sql, Communication_name)

    return dependency_dest_res

def get_externalroles(dbname):
    extroles_sql = """SELECT RoleName FROM study.ExternalRole Where ActiveInactive = 1"""
    External_res = connection.execute_InsertSelect_sql(dbname, extroles_sql)
    return External_res

# def get_groupbyvalues():
#     groupBy_sql = """SELECT GroupByName FROM study.ResponseByGroups"""
#     connection.cursor.execute(groupBy_sql)
#     Groupby_res = connection.cursor.fetchall()
#     return Groupby_res

# def get_System_DestinationValues():
#     Sys_Dest_Val_sql = """SELECT DestinationValue FROM Study.FormDestination WHERE DestinationType = 1 and DestinationValueType = 1"""
#     connection.cursor.execute(Sys_Dest_Val_sql)
#     Sys_Dest_Vals_res = connection.cursor.fetchall()
#     return Sys_Dest_Vals_res


def get_notificationid(dbname, CommunicationName):
    noftification_sql = """SELECT NotificationId FROM [Study].[Notification] N JOIN [dbo].[Communication] C 
    ON C.CommunicationGUID = N.CommunicationGUID
    WHERE C.name = ? And N.CommunicationGUID = 
    (Select CommunicationGUID FROM dbo.Communication WHERE Name = ?)"""
    notificationid = connection.execute_InsertSelect_sql(dbname, noftification_sql, CommunicationName, CommunicationName)
    return notificationid


def get_destinationvalguid(dbname,DestinationValue_Selected_Source, DestinationValue_Selected):
    destinationguid = ''
    if DestinationValue_Selected_Source == "Field" or DestinationValue_Selected_Source == "Manual" :
        destinationguid_sql = """SELECT DestinationGUID FROM [Study].[FormDestination] WHERE  DestinationValue = ?"""
    elif  DestinationValue_Selected_Source == "Rule":
        destinationguid_sql = """SELECT  DestinationGUID FROM Study.FormDestination FD JOIN Study.StudyRule SR 
    ON FD.DestinationValue = SR.StudyRuleGUID WHERE FD.DestinationType = 1 AND FD.DestinationValueType = 2 AND SR.RuleName = ?"""

    destinationguid = connection.execute_InsertSelect_sql(dbname, destinationguid_sql, DestinationValue_Selected)

    return destinationguid


def get_componentguid(dbname, ComponentName_Selected, ComponentType):
    # print("calling Inside of getting ComponentGUID", ComponentName_Selected,ComponentType )
    ComponentGUID = ''
    componentguid_forms_sql = """SELECT FORMGUID FROM study.StudyForm WHERE formname = ?"""
    componentguid_tasks_sql = """SELECT TASKGUID FROM Study.StudyTask WHERE name = ?"""
    if ComponentType == 'Forms':
        # print("calling Inside of getting ComponentGUID of form type", ComponentName_Selected, ComponentType)
        ComponentGUID = connection.execute_InsertSelect_sql(dbname, componentguid_forms_sql, ComponentName_Selected)

        # print("After Inside of getting ComponentGUID", ComponentName_Selected, ComponentType,ComponentGUID)
    elif ComponentType == 'Tasks':
        ComponentGUID = connection.execute_InsertSelect_sql(dbname, componentguid_tasks_sql, ComponentName_Selected)

    return ComponentGUID


def delete_responseby_UserRole(dbname,ComponentType, ComponentName, ComponentGuid, ExternalRoleID, GroupByID):
    del_resp_userrole_sql = """DELETE FROM Study.ResponseByUserRole WHERE ComponentName = ? AND ComponentGUID = ? AND ComponentType = ? AND ExternalRoleID = ? AND GroupByID = ?"""
    connection.execute_delete_sql(dbname, del_resp_userrole_sql, ComponentName, ComponentGuid, ComponentType, ExternalRoleID, GroupByID)


def get_externalroleid(dbname,Externalrolename):
    externalroleid_sql = """SELECT ExternalRoleID FROM Study.ExternalRole Where RoleName = ?"""
    externalroleid = connection.execute_InsertSelect_sql(dbname, externalroleid_sql, Externalrolename)
    return externalroleid

def get_groupbyid_By_DestVal(dbname,DestinationValue_Selected):
    groupbyid = 0
    groupby_string = DestinationValue_Selected[19:]
    groupbyid_sql = """SELECT GroupByID FROM Study.ResponseByGroups Where GroupByName = ?"""
    if groupby_string.startswith('Depot'):
        groupby_string = DestinationValue_Selected[19: 24]
        groupbyid = connection.execute_InsertSelect_sql(dbname, groupbyid_sql, groupby_string)

    else:
        groupbyid = connection.execute_InsertSelect_sql(dbname, groupbyid_sql, groupby_string)

    return groupbyid

def get_groupbyid_By_GroupByName(dbname,GroupByName):
    groupby_string = GroupByName
    print("Calling Inside Getting group by iD ", GroupByName)
    groupbyid_sql = """SELECT GroupByID FROM Study.ResponseByGroups Where GroupByName = ?"""
    if groupby_string.startswith('Depot'):
        groupby_string = groupby_string[: 5]
        groupbyid = connection.execute_InsertSelect_sql(dbname, groupbyid_sql, groupby_string)
    else:
        groupbyid = connection.execute_InsertSelect_sql(dbname, groupbyid_sql, groupby_string)
    return groupbyid


def delete_dest_val(dbname,ComponentType,ComponentName_Selected, CommunicationName_Selected,DestinationValue_Selected, isResponseUserRoleChecked):

    notificationid = int(get_notificationid(dbname, CommunicationName_Selected)[0][0])

    destuinationValueGUID = get_destinationvalguid(dbname,DestinationValue_Selected[1],DestinationValue_Selected[2] )[0][0]

    if isResponseUserRoleChecked == 1 and  DestinationValue_Selected[1] == "Rule":
        ComponentGUID = get_componentguid(dbname,ComponentName_Selected, ComponentType)[0][0]
        ExternalRoleID =  int(DestinationValue_Selected[1][17:18])
        GroupByID = get_groupbyid_By_DestVal(dbname,DestinationValue_Selected[1])

        if GroupByID != 0:
            delete_responseby_UserRole(dbname,ComponentType, ComponentName_Selected, ComponentGUID, ExternalRoleID, GroupByID)

    delete_dest_val_sql = """DELETE FROM [Study].[NotificationDestinationAssociation] WHERE NotificationId = ? AND DestinationGUID = CONVERT(uniqueidentifier, ?)"""
    groupbyid = connection.execute_delete_sql(dbname, delete_dest_val_sql, notificationid, destuinationValueGUID)


def configure_fetch_sysdest(dbname,systemdestination):
    SystemDestination_sql = """
    DECLARE @DestinationGuid uniqueidentifier, @isExists INT = 0
    IF Exists (SELECT DestinationGUID FROM STudy.FormDestination WHERE DestinationValue = ? 
                                   AND DestinationType = 1 AND DestinationValueType = 1)

                                   BEGIN 
                                   SET @DestinationGuid =(SELECT DestinationGUID FROM STudy.FormDestination 
                                   WHERE DestinationValue = ? AND DestinationType = 1 AND DestinationValueType = 1)
                                   SET @isExists = 1
    					   END
    					   SELECT CAST (@DestinationGuid AS UNIQUEIDENTIFIER) , @isExists"""

    sysdest_guid = connection.execute_InsertSelect_sql(dbname, SystemDestination_sql, systemdestination,systemdestination)
    systemDestinationGUID , isExists = sysdest_guid[0][0], sysdest_guid[0][1]
    if isExists == 0:
        SystemDestination_sql = """
        INSERT INTO Study.FormDestination (DestinationID, DestinationGUID, DestinationValue, DestinationType, DestinationValueType, IsDefault, LastModifiedDate, ActiveInactive, UserResponseType, IsPredefined)  
        VALUES ((SELECT Max(DestinationID) FROM Study.FormDestination) + 1 , NEWID(),?, 1, 1, 0, GETDATE(),1 , 2, 0)
        """
        sysdest_InsertedRows = connection.execute_Insert_sql(dbname, SystemDestination_sql, systemdestination, systemdestination)
        print(sysdest_InsertedRows)
        if sysdest_InsertedRows[0][0] > 0:
            SystemDestination_sql = """
            DECLARE @DestinationGuid uniqueidentifier, @isExists INT = 0
            IF Exists (SELECT DestinationGUID FROM STudy.FormDestination WHERE DestinationValue = ? 
                                           AND DestinationType = 1 AND DestinationValueType = 1)

                                           BEGIN 
                                           SET @DestinationGuid =(SELECT DestinationGUID FROM STudy.FormDestination 
                                           WHERE DestinationValue = ? AND DestinationType = 1 AND DestinationValueType = 1)
                                           SET @isExists = 1
            					   END
            					   SELECT CAST (@DestinationGuid AS UNIQUEIDENTIFIER) , @isExists"""
            sysdest_guid = connection.execute_InsertSelect_sql(dbname, SystemDestination_sql, systemdestination,systemdestination)
            systemDestinationGUID = sysdest_guid[0][0]
            return systemDestinationGUID
    return systemDestinationGUID



def configure_fetch_Manualdest(dbname,manualdestination):
    print("Inside the Mnaul Dest GUID Fetch started", )
    ManualDestination_sql = """
        DECLARE @DestinationGuid uniqueidentifier, @isExists INT = 0
        IF Exists (SELECT DestinationGUID FROM STudy.FormDestination WHERE DestinationValue = ? 
                                       AND DestinationType = 1 AND DestinationValueType = 0)

                                       BEGIN 
                                       SET @DestinationGuid =(SELECT DestinationGUID FROM STudy.FormDestination 
                                       WHERE DestinationValue = ? AND DestinationType = 1 AND DestinationValueType = 0)
                                       SET @isExists = 1
        					   END
        					   SELECT CAST (@DestinationGuid AS UNIQUEIDENTIFIER) , @isExists"""
    print("Before executing Select Statement", ManualDestination_sql)
    Manualdest_guid = connection.execute_InsertSelect_sql(dbname, ManualDestination_sql, manualdestination, manualdestination)

    ManualDestinationGUID, isExists = Manualdest_guid[0][0], Manualdest_guid[0][1]
    print("After the executing Select Statement GUID Fetch",ManualDestinationGUID , isExists)
    if isExists == 0:
        print("Since not exist the Destination Coming inside the Insert start")
        ManualDestination_sql = """
            INSERT INTO Study.FormDestination (DestinationID, DestinationGUID, DestinationValue, DestinationType, DestinationValueType, IsDefault, LastModifiedDate, ActiveInactive, UserResponseType, IsPredefined)  
            VALUES ((SELECT Max(DestinationID) FROM Study.FormDestination) + 1 , NEWID(),?, 1, 0, 0, GETDATE(),1 , 2, 0)
            """
        manualdest_InsertedRows = connection.execute_Insert_sql(dbname, ManualDestination_sql, manualdestination)
        print("After  Coming inside the Insert , after executing the insert query", manualdest_InsertedRows)
        # print(manualdest_InsertedRows)
        if manualdest_InsertedRows > 0:
            print("Successfully Inserted", 'again executing the select query start')
            ManualDestination_sql = """
                DECLARE @DestinationGuid uniqueidentifier, @isExists INT = 0
                IF Exists (SELECT DestinationGUID FROM STudy.FormDestination WHERE DestinationValue = ? 
                                               AND DestinationType = 1 AND DestinationValueType = 0)

                                               BEGIN 
                                               SET @DestinationGuid =(SELECT DestinationGUID FROM STudy.FormDestination 
                                               WHERE DestinationValue = ? AND DestinationType = 1 AND DestinationValueType = 0)
                                               SET @isExists = 1
                					   END
                					   SELECT CAST (@DestinationGuid AS UNIQUEIDENTIFIER) , @isExists"""
            manualdest_guid = connection.execute_InsertSelect_sql(dbname, ManualDestination_sql, manualdestination,  manualdestination)
            ManualDestinationGUID = manualdest_guid[0][0]
            print("Successfully Inserted", 'again executing the select query end', ManualDestinationGUID, type(ManualDestinationGUID))
            return ManualDestinationGUID
    return ManualDestinationGUID



def configure_fetch_dynamicdest(dbname,Rulename):
    Dynmic_Destination_sql = """
    
            DECLARE @DestinationGuid uniqueidentifier, @isExists INT = 0
            IF Exists (SELECT FD.DestinationGUID FROM Study.FormDestination FD
JOIN Study.StudyRule SR ON CONVERT(NVARCHAR(100),SR.StudyRuleGUID ) = FD.DestinationValue 
WHERE SR.RuleName = ? AND DestinationType = 1 AND DestinationValueType = 2
)

                                           BEGIN 
                                           SET @DestinationGuid =  ( SELECT FD.DestinationGUID FROM Study.FormDestination FD
JOIN Study.StudyRule SR ON CONVERT(NVARCHAR(100),SR.StudyRuleGUID ) = FD.DestinationValue 
WHERE SR.RuleName = ? AND DestinationType = 1 AND DestinationValueType = 2)
     SET @isExists = 1
            					   END
            					   SELECT CAST (@DestinationGuid AS UNIQUEIDENTIFIER) , @isExists"""

    Dynamicdest_guid = connection.execute_InsertSelect_sql(dbname, Dynmic_Destination_sql, Rulename,Rulename)

    DynamicDestinationGUID, isExists = Dynamicdest_guid[0][0], Dynamicdest_guid[0][1]
    if isExists == 0:
        Dynmic_Destination_sql = """
                INSERT INTO Study.FormDestination (DestinationID, DestinationGUID, DestinationValue, DestinationType, DestinationValueType, IsDefault, LastModifiedDate, ActiveInactive, UserResponseType, IsPredefined)  
VALUES ((SELECT Max(DestinationID) FROM Study.FormDestination) + 1 ,NEWID(),CONVERT(NVARCHAR(100), (SELECT StudyRuleGUID FROM study.StudyRule WHERE RuleName = ?)), 1, 2, 0, GETDATE(),1 , 2, 0)
                """
        Dynamicdest_InsertedRows = connection.execute_Insert_sql(dbname, Dynmic_Destination_sql, Rulename)
        print(Dynamicdest_InsertedRows)
        if Dynamicdest_InsertedRows[0][0] > 0:
            Dynmic_Destination_sql = """                    
            DECLARE @DestinationGuid uniqueidentifier, @isExists INT = 0
            IF Exists (SELECT FD.DestinationGUID FROM Study.FormDestination FD
JOIN Study.StudyRule SR ON CONVERT(NVARCHAR(100),SR.StudyRuleGUID ) = FD.DestinationValue 
WHERE SR.RuleName = ? AND DestinationType = 1 AND DestinationValueType = 2)
                                           BEGIN 
                                           SET DestinationGuid =  ( SELECT FD.DestinationGUID FROM Study.FormDestination FD
JOIN Study.StudyRule SR ON CONVERT(NVARCHAR(100),SR.StudyRuleGUID ) = FD.DestinationValue 
WHERE SR.RuleName = ? AND DestinationType = 1 AND DestinationValueType = 2)
     SET @isExists = 1
            					   END
            					   SELECT CAST (@DestinationGuid AS UNIQUEIDENTIFIER) , @isExists"""
            Dynamicdest_guid = connection.execute_InsertSelect_sql(dbname, Dynmic_Destination_sql, Rulename,Rulename)
            DynamicDestinationGUID = Dynamicdest_guid[0][0]
            return DynamicDestinationGUID
    return DynamicDestinationGUID



def get_groupbyname(groupByName):
    if groupByName.startswith('Depot'):
        return 'Depot'
    else:
        return groupByName


def Configure_Destinations(dbname,Destinations):
    dynamicdestconfigure_sql = """INSERT INTO Study.NotificationDestinationAssociation (SystemIdentifier, NotificationId, DestinationGUID, CreatedBy, CreatedDate, ModifiedBy, LastModifiedDate)
    VALUES ( (SELECT MAX(SystemIdentifier) +1 FROM Study.NotificationDestinationAssociation), ?,CAST(? AS UNIQUEIDENTIFIER),'cenduit/sjampala', GETDATE(), 	NULL, GETDATE())"""

    responsebyuserroleConfig_sql = """IF NOT EXISTS (SELECT * FROM STudy.ResponseByUserRole WHERE ComponentGUID = ? AND ComponentName = ? AND ExternalRoleID = ? AND GroupByID = ? AND ComponentType = ?)
 INSERT INTO Study.ResponseByUserRole  (ComponentGUID,	ComponentName,	ExternalRoleID,	ExternalRoleName,	GroupByID,	GroupByName,	ComponentType,	LastModifiedDate)
 VALUES (?,	?,	?,	?,	?,	?,	?,	GETDATE())"""
    print (Destinations)
    for dest in Destinations:
          # dest[0], dest[1], dest[2], dest[3], dest[4], dest[5],
          CommunicationName = dest[2]
          Notificationid = get_notificationid(dbname,CommunicationName)[0][0]

          DestinationVal_Source = dest[6]

          if DestinationVal_Source == 'Field':
             sysdestguid = configure_fetch_sysdest(dbname,dest[3])
             # print(dynamicdestconfigure_sql,sysdestguid,Notificationid)
             print("Calling Inside Field Configure", dbname, dynamicdestconfigure_sql, Notificationid, sysdestguid )
             connection.execute_Insert_sql(dbname, dynamicdestconfigure_sql, Notificationid, sysdestguid)

          elif DestinationVal_Source == 'Manual':
              print("printing the final manual guid",configure_fetch_Manualdest(dbname,dest[3])[0][0],configure_fetch_Manualdest(dbname,dest[3]) )
              manualdestguid = configure_fetch_Manualdest(dbname,dest[3])
              print("Calling Inside Manual Configure", dbname, dynamicdestconfigure_sql, Notificationid, manualdestguid)
              connection.execute_Insert_sql(dbname, dynamicdestconfigure_sql, Notificationid, manualdestguid)

          elif DestinationVal_Source == 'Rule':
              dynamicdestguid = configure_fetch_dynamicdest(dbname,dest[3])
              ComponentName = dest[1]
              ComponentType = dest[0]
              ComponentGUID = get_componentguid(dbname,ComponentName, ComponentType)[0][0]
              ExternalRoleName = dest[4]
              ExternalRoleID = int(get_externalroleid(dbname,ExternalRoleName)[0][0])
              GroupByName = get_groupbyname(dest[5])
              print(GroupByName)

              print("Calling Inside dynamic Configure", dbname, dynamicdestconfigure_sql, Notificationid, dynamicdestguid)

              GroupByID = int(get_groupbyid_By_GroupByName(dbname,GroupByName)[0][0])
              print("Calling Inside dynamic Configure", dbname, responsebyuserroleConfig_sql, ComponentGUID,
                    ComponentName, ExternalRoleID, GroupByID, ComponentType,
                    ComponentGUID, ComponentName, ExternalRoleID, ExternalRoleName, GroupByID, GroupByName,
                    ComponentType)

              connection.execute_Insert_sql(dbname, dynamicdestconfigure_sql, Notificationid, dynamicdestguid)
              connection.execute_Insert_sql(dbname, responsebyuserroleConfig_sql, ComponentGUID, ComponentName, ExternalRoleID, GroupByID, ComponentType,
                                                  ComponentGUID, ComponentName, ExternalRoleID, ExternalRoleName, GroupByID, GroupByName, ComponentType)















