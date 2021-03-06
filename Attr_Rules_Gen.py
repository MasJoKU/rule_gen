# Python based rule generator and attribute counter

from operator import attrgetter
from itertools import groupby

class Project_rule:
    
    def __init__(self, id):
        self.id = id
        self.u_adminRole = input("u.adminRole: ")
        self.r_type = input ("r.type: ")
        self.u_department = input ("u.department: ")
        self.r_department = input ("r.department: ")
        self.u_projectLed = input ("u.projectLed: ")
        self.u_project = input ("u.project: ")
        self.r_project = input ("r.project: ")
        self.u_task = input ("u.task: ")
        self.r_proprietary = input ("r.proprietary: ")
        self.u_expertise = input ("u.expertise: ")
        self.u_isEmployee = input ("u.isEmployee: ")
        self.action = input ("action: ")

class University_rule:
    
    def __init__(self, id):
        self.id = id
        self.r_type = input("u.adminRole: ")
        self.u_courseTaken = input ("r.type: ")
        self.u_courseTaught = input ("u.department: ")
        self.u_position = input ("r.department: ")
        self.u_isChair = input ("u.projectLed: ")
        self.u_department = input ("u.project: ")
        self.r_department = input ("r_department: ")
        self.u_uid = input ("r.project: ")
        self.action = input ("action: ")
		
class temp: 
    def __init__(self, id, action, r_department, r_project, r_proprietary, r_type, u_adminRole, u_department, u_expertise, u_project, u_projectLed, u_task, u_isEmployee):
        self.id = id
        self.u_adminRole = u_adminRole
        self.r_type = r_type
        self.u_department = u_department
        self.r_department = r_department
        self.u_projectLed = u_projectLed
        self.u_project = u_project
        self.r_project = r_project
        self.u_task = u_task
        self.r_proprietary = r_proprietary
        self.u_expertise = u_expertise
        self.u_isEmployee = u_isEmployee
        self.action = action

def ProjectP_rule(n_rule):
    ProP = []
    for i in range (n_rule):
        print ("Rule number: ", i+1 )
        ProP.append(Project_rule(i+1))
    return ProP

def ProjectN_rule(n_rule):
    ProN = []
    for i in range (n_rule):
        print ("Rule number: ", i+1 )
        ProN.append(Project_rule(i+1))
    return ProN

def UniversityP_rule(n_rule):
    UniP = []
    for i in range (n_rule):
        print ("Rule number: ", i+1 )
        UniP.append(Project_rule(i+1))
    return UniP

def UniversityN_rule(n_rule):
    UniN = []
    for i in range (n_rule):
        print ("Rule number: ", i+1 )
        UniN.append(Project_rule(i+1))
    return UniN

def ProjectP():
	PP_n_rule = int (input ("Number of Project's Positive Rules? "))
	ProjectP = ProjectP_rule(PP_n_rule)
	return ProjectP

def ProjectN():
	PN_n_rule = int (input ("Number of Project's Negative Rules? "))
	ProjectN = ProjectN_rule(PN_n_rule)
	return ProjectN

def UniversityP():
	UP_n_rule = int (input ("Number of University's Positive Rules? "))
	UniversityP = UniversityP_rule(UP_n_rule)
	return UniversityP

def UniversityN():
	PN_n_rule = int (input ("Number of University's Negative Rules? "))
	UniversityN = UniversityN_rule(PN_n_rule)
	return UniversityN

def merge_ProjectPN(ProjectP, ProjectN):
	ProjectPN = ProjectP + ProjectN
	return ProjectPN

def merge_universityPN(UniversityP, UniversityN):
	UniversityPN = UniversityP + UniversityN
	return UniversityPN

def count_atr(rule_list):
	objects_list = []
	for i in range (len(rule_list)):
		objects_list.append(rule_list[i]) 
	
	attrs = list(x for x in dir(rule_list[1]) if not x.startswith('__') and x != 'id')

	listx = []
	Atr_list = []
	for u_adminRole, group in groupby(sorted(objects_list, key=attrgetter('u_adminRole')),
						  key=attrgetter('u_adminRole')):
		# create result object with lists as attributes
		result = temp(u_adminRole, *[[]]*len(attrs))
		
		# merge elements
		for x in group:
			for a in attrs:
				if getattr(x, a) != "":
					if getattr(x, a) != getattr(result, a):
						setattr(result, a, getattr(result, a) + [getattr(x, a)])
						Atr_list.append(a)
	
		listx = listx + result.action + result.r_department + result.r_project + result.r_proprietary + result.r_type + result.u_adminRole + result.u_department + result.u_expertise + result.u_project + result.u_projectLed + result.u_task

	fin_value_list = list(set(listx))
	fin_atr_list = list(set(Atr_list))
	
	print ("Number of Attributes: ", len (fin_atr_list))
	print ("Active Attributes: ", fin_atr_list)
	print ("Number of Attribute Values: ", len (fin_value_list))
	print ("Attribute Values: ", fin_value_list)

comm = ''
while comm != 'exit':
	print('your command? ("help" for commands list)')
	comm = input()
	if comm == "c1": #"create_ProjectP_rule":
		ProP = ProjectP()
	elif comm == "c2": #"create_ProjectN_rule":
		ProN = ProjectN()
	elif comm == "c3": #"create_UniversityP_rule":
		UniP = UniversityP()
	elif comm == "c4": # "create_UniversityN_rule":
		UniN = UniversityN()
	elif comm == "c5": #"merge_Project_rule":
		ProPN = merge_ProjectPN(ProP, ProN)
		print ("merge succeed")
	elif comm == "c6": #"merge_University_rule":
		UniPN = merge_universityPN(UniP, UniN)
		print ("merge succeed")
	elif comm == "c7": #"count_Attribute(Project_rule)":
		count_atr(ProPN)
	elif comm == "c8": #"count_Attribute(University_rule)":
		count_atr(UniPN)
	elif comm == "help":
		print ("'c1': create_ProjectP_rule")
		print ("'c2': create_ProjectN_rule")
		print ("'c3': create_UniversityP_rule")
		print ("'c4': create_UniversityN_rule")
		print ("'c5': merge_Project_rule")
		print ("'c6': merge_University_rule")
		print ("'c7': count_Attribute(Project_rule)")
		print ("'c8': count_Attribute(University_rule)")
		print ("'exit': exit program")
	else:
		print ("wrong command")