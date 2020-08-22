#! /usr/bin/env python3

import json 

def read_json(file_json):
  with open(file_json, 'r', encoding='utf8') as f:
    return json.load(f)

# returns the list of people without duplicates
def find_people(role, data):
  list_people = []
  for value in data:
    if len(value) == 1:
      list_people.append(value[role])
    else:
      for v in value[role]:
        list_people.append(v)
  
  return sorted(set(list_people))

# sort the data according to 'priority'
def get_my_key(obj):
  return obj['priority']

# returns a person's project list depending on their job title
def find_projects(name, role, list_data):
  projects = []
  for keyval in list_data:
    if name in keyval[role]:
      projects.append(keyval['name'])

  return projects

# populate and write a json file
def populate_json(role, list_people, data):
  list_result = []
  for people in list_people:
    list_result.append([people,find_projects(people,role, data)])

  people_to_json = []

  for n in list_result:
    people_to_json.append({n[0]:n[1]})

  with open(role+'.json', 'w') as outfile:
    json.dump(people_to_json, outfile)

data = read_json('source_file_2.json')

data.sort(key=get_my_key)

watchers = find_people('watchers', data)
managers = find_people('managers', data)

populate_json('watchers',watchers, data)
populate_json('managers',managers, data)

print(str('Sucess!!!'))