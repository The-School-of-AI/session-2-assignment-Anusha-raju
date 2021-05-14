# Session 2 assignment of EPAi3.0
Object Mutability and Interning
-	This assignment was all about debugging errors.
-	The assignment was given as a link, which directed to an automatically generated repository of session2 assignment.
-	The assignment is directly solved using github actions. 
-	The repository included the following files:
	- .github
	- .gitignore
	- README.md
	- requirements.txt
	- session2.py
	- test_session2.py
	- Here the requirements file indicates that only memory profiler and pytest is required

## PROBLEM: To find the debugs in session2.py file such that all the test cases in test_session2.py file is passed.
###### Given: There are 10 test cases in test_session2.py file ( Three are already solved).

-	The first part of the session2 file is based on memory leak.
-	There is cyclic reference between classes Something and SomethingNew.
-	The clear_memory is not able to do its job, as there is a bug there.
-	add_something function takes in two parameters ( list , interger), creates objects of Something class and SomethingNew class and appends the Something class object to collection list.
-	The second part of the session2 file includes string comparison.
-	 The compare_strings_old(n) function is already defined for us which compares two strings “a” and “b” is exactly same or not.
-	After that we are trying to see if we have a particular character in that string or not. char_list consists of all the characters in string ‘a’.
-	But the function is sub-optimal hence we have to redefine the code of the compare_strings_new(n) function such that it takes 1/10 the current time. The sleep function is just to simulate your "slow" code.
-	__init__ is one of the reserved methods in Python, used to initialize attributes of the class.

## SOLUTION:

#### Test cases related to readme file:
- test_readme_exists(): This test case is used to check if the readme file exists. The readme file was automatically generated when the repository was created.
	Hence this test case was passed automatically.
- test_readme_contents(): This function is used to check the minimum word limit (500) of the readme file.
- test_readme_proper_description(): This function is used to check the content of the readme file. There is a predefined list README_CONTENT_CHECK_FOR[]  which consists of the key words that should be included in the readme file. 
  The function iterates through the readme file and check for the key words if not found READMELOOKSGOOD == False.
- test_readme_file_for_formatting(): This function checks for the number of  ‘#’ strings in the file. This should be a minimum of 10.

#### Test cases related to optimizing the string comparison:
- test_performance(): This function compares the performance of the compare_strings_old(n) and compare_strings_new(n) functions of the seesion2.py file.
The compare_strings_new(n) function should reduce the performance time by 1/10.
	- Solution: the compare_strings_old uses the equality(==) operator which evidently consumes more time, whereas the compare_strings_new uses the ‘is’ operator which check for memory addresses.

#### Test cases related to formatting of the session2.py file.
- test_indentations(): This function check for the indentations in the session2 file. The code should follow the PEP8 guidelines.
- test_function_name_had_cap_letter(): This function checks if any function name has a capital letter.
- test_class_repr(): This function checks for __repr__() in Something and SomethingNew class. Here ‘s’ is an object of Something class and ‘s_n’ is an object of SomethingNew class. 

#### Test cases related to memory_usage of critical_function().
- test_clear_memory(): This test function is to check if the clear_memory function invoked by critical_function performed its task or not. 
- test_memory_actually_increased():This test will check whether we are actually increase the memory during running the critical function.

