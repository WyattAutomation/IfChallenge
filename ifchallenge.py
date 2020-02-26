import json


class jsonTree(object):

	def __init__(self, file):
		# Load data + hierarchy structure from json file
		input_file = open(file)
		self.json_data = json.load(input_file)

		# Initialize a list for gathering salary totals to sum later
		self.salary_totals = []

	def callback(self):
		# Top level iterative search through "executive staff" for CEO, sorted alphabetically by name 
		# Leaving sort() here in the event additional executive staff need to be added to this
		for element in sorted(self.json_data["executive staff"]):
			if element["Title"] == "CEO":
				# Append the element's salary to the salary list, cast to int() so sum() will work later on
				self.salary_totals.append(int(element["salary"]))
				# Print the name.  No spacing for exec staff
				print(element["name"])
				print("Employees of: " + element["name"])
				# Iterate though alpabetically sorted dicts of employees that are 
				# nested directly under "executive staff" list.
				# Print their names with proper spacing for tree representation, 
				# cast their salaries to int and append them to salary totals list.
				for emp in sorted(element["employees"], key= lambda i :i["name"]):
					self.salary_totals.append(int(emp["salary"]))
					print("      " + emp["name"])
					# Check for the presence of elements in employee[] dict, 
					# if elements are present, iterated through them, sorted alphabetically
					if emp["employees"]:
						print("      " + "Employees of: " + emp["name"])
						for emp2 in sorted(emp["employees"], key= lambda i :i["name"]):
							print("            " + emp2["name"])
							self.salary_totals.append(int(emp2["salary"]))
		# get the sum of the salaries, and print it.
		saltotes = sum(self.salary_totals)
		print("Total salary: $" + str(saltotes))

if __name__ == '__main__':
	treeprint = jsonTree('./emp1.json')
	treeprint.callback()