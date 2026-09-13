marks={
        'Aryan':80,
        'shubham':56,
        'Rohan':23,
}
# print(marks,type(marks))
# print(marks['Rohan'])
# marks['Rohan']=45#updating the value so dictionary is mutable
# print(marks['Rohan'])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({'Rohan':45,'rajeev':45})# it is used to add new key value pair in dictionary
# print(marks)
print(marks.get('shubham'))# it is used to get the value of key but if key is not present then it shows none
print(marks['shubham'])# it is also used to get the value of key but if key is not present then it shows error 
print(marks.pop('Rohan'))