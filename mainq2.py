#Question 2
dog= dict()
#The update() method inserts the specified dictionary
dog.update({"name":"Chris", "color":"Green", "breed":"Husky", "legs":4, "age":3})
print("Added key-value pair to dog: ",dog)
#used  dict() function which creates a empty dictionary
student_dict = dict()
keyList = ["first_name", "last_name", "gender","age","marital status","skills","country","city","address"]
#added only keys to the dictionary with None value using update method
student_dict.update({key: None for key in keyList})
print("\nStudent_Dictionary after adding keys: ",student_dict)
#utilised len(dictionary) function to calculate the length
print("Length of Student_Dictionary: ", len(student_dict))
#updated student_dict with sample values
student_dict.update({"first_name": "Akhil", "last_name": "Reddy", "gender": "Male", "age": "24",
                     "marital status": "Single", "skills": ["Python","sql"], "country": "India","city": "Jmd",
                     "address": " Street"})

print("\nStudent_dict ", student_dict)
#accessing paritcular value of key in dict: dict["key"]
print("\nAccessing Skills value in dictionary: ",student_dict["skills"])
#type(value) - function gives the datatype of provided values
print("Data Type of Skills in Student Dict: ", type(student_dict["skills"]))
#The extend() adds all the elements of an iterable (list, tuple, string etc.) to the end of the list
student_dict["skills"].extend(["Apex", "JavaScript"])
print("Updated Skills list after adding new values: ", student_dict["skills"])
# dict.keys() and values() gives the list of keys and values as a list respectively
print("\n",student_dict.keys())
print(student_dict.values())
