# list_of_tuples = [('CEN-CohortStatusChangeForm-W-1', 'CBS_COM_CohortStatusChangeFormW1_Success_Fax'),
#  ('CEN-CohortStatusChangeForm-W-1', 'CBS_COM_CohortStatusChangeFormW1_Success_Email'),
#  ('CEN-CohortStatusChangeForm-W-1', 'CBS_COM_CohortStatusChangeFormW1_Reject')]

# list_of_tuples = [('CEN-CohortStatusChangeForm-W-1',),
#  ('CEN-CohortStatusChangeForm-W-1',),
#  ('CEN-CohortStatusChangeForm-W-1',)]
#
# comm = [( 'CBS_COM_CohortStatusChangeFormW1_Success_Fax'),
#         ( 'CBS_COM_CohortStatusChangeFormW1_Success_Email'),
#         ('CBS_COM_CohortStatusChangeFormW1_Reject')]
#
# keys = ("formname", )
# for value in list_of_tuples:
#     print(dict(zip(keys,value)))
#
# def get_list_of_dict(keys, list_of_tuples):
#     list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
#     return list_of_dict
#
#     # print(component_names_raw)
#
#
# final_dict = get_list_of_dict(keys,component_names_raw )
# context = { 'data': [
#                     {
#                         'name': 'Celeb 1',
#                         'worth': '3567892',
#                         'dependentcommunication':[
#
#                         {'commname': 'aaaaaaaaaa'},
#                         {'commname': 'bbbbbbbbbb'},
#                         {'commname': 'cccccccccc'}
#                         ]
#                     },
#                     {
#                         'name': 'Celeb 2',
#                         'worth': '23000000'
#                     },
#                     {
#                         'name': 'Celeb 3',
#                         'worth': '1000007'
#                     },
#
#                 ]
#                 }






data = [('Country-1', 'state1'), ('Country-1', 'state2'), ('Country-1', 'state3'),
        ('Country-2', 'state1'), ('Country-2', 'state2'), ('Country-2', 'state3'),
        ('Country-3', 'state1'), ('Country-3', 'state2'), ('Country-3', 'state3')]

reformatted_data = {}

for pair in data:

    state_list = reformatted_data.get(pair[0], None)

    if state_list:
        if pair[1] in state_list:
            pass
        else:
            reformatted_data[pair[0]].append(pair[1])
    else:
        reformatted_data[pair[0]] = [pair[1]]

# Try this print in your console to make sure it's working properly
print(reformatted_data)



























