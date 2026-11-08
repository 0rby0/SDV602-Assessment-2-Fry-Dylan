# Executes a specified test and returns the results
from matplotlib.figure import Figure

class Test:

	# test_name = The natural language description of what the test is doing (e.g. Get the name of the current session)
	# function_description = The high level format of the function being called (e.g. Session.get_session instead of app.sm.sessions[0].get_session())
	# test_function = The call to the exact function being tested (e.g. app.sm.sessions[0].get_session("Test Session"))
	# expected_result = The output that the function needs to return for the test to be considered a successful execution (e.g. {"name": "Test Session", "data": ["a", "b", "c"]})
	# print_verbose = Inherited from the headless runner, tells the test whether or not to return the extra details of its run
	def __init__(self, test_name, function_description, test_function, expected_result, print_verbose):
		output = {"text": f"\n\n\033[1m{test_name}\033[0m - ", "passed": False}

		result = test_function

		if print_verbose:
				output["text"] += f"\n\tFunction: {function_description}"
				output["text"] += f"\n\tExpected Result: |{expected_result}|"
				output["text"] += f"\n\tActual Result: |{result}|"

		# Attempt down the list of checks
		try:
			if type(result) is Figure:
				valid_result = True
			else:
				valid_result = self.compare_dicts(result = result, expected = expected_result)
		except:
			try: 
				valid_result = (sorted(result) == sorted(expected_result))
			except:
				try: 
					valid_result = (result == expected_result)
				except:
					valid_result = False
			
		if valid_result:
				output["text"] += f"\n\033[92mPassed\033[0m"
				output["passed"] = True
		else:
				output["text"] += f"\n\033[91mFailed\033[0m"
				output["passed"] = False

		self.output = output
  
	def compare_dicts(self, result, expected):
		# Fail if the results are different sizes
		if len(result) != len(expected):
			return False
	  
		# Go through each key in the actual result
		for key in result:
			# If the key from the actual result is not in the expected result
			if key not in expected:
				return False
 
			# If the values are the same between the two dictionaries
			if result[key] != expected[key]:
				return False
		
		# Only pass the check if all other checks didn't fail
		return True