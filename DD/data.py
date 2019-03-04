from DD import connection
from DD import databaseadmin

# def get_component_form(dbname):
#     sql = "Select formname , formguid from study.StudyForm order by 1"
#     forms_res = connection.execute_InsertSelect_sql(dbname, sql)
#     return forms_res


def get_communication(dbname):
    dependency_Communication_res= ''
    forms_sql = """ SELECt sf.formname, c.name   FROM study.StudyForm SF JOIN [dbo].[ComponentDependency] CD
ON cd.SourceCompGUID =  CONVERT (NVARCHAR(100), sf.Formguid) JOIN dbo.communication c ON c.communicationguid = CD.DependentCompGUID
"""
    # WHERE
    # SF.FormName = ?
    dependency_Communication_res = connection.execute_InsertSelect_sql(dbname, forms_sql)
    return dependency_Communication_res

print(get_communication('testdb'))