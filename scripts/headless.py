# Run through a series of commands to test the application
from test import Test
from session import Session
from db_config import DBConfig

# Verbosity Levels:
#
# 0 = Just prints "passed" if all tests passed or "failed" if any tests failed
# 1 = Prints the short summary with how many tests passed and failed
# 2 = Prints the pass/fail for each test and the summary
# 3 = Prints all details, including what modules are present

class HeadlessTest:
	def __init__(self, app, verbosity : int = 2):

		print(f"\n-- Headless Test --")
		results = []

		# Switch DB to test
		DBConfig().use_db(db = "test")

		# Display Connected Modules ---- DEPRECATED
		# if verbosity >= 3:
		# 	print(f"\nPresent :---:\n\n\tData Display: {app.sm.display is not None}\n\tUser: {app.sm.user is not None}\n\tSession: {app.session is not None}\n\tSession Manager: {app.sm is not None}\n\nTests   :---:")

		# Remote mode tests
		if app.remote:
     
			# User Tests

			# Test 2.1 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Create a new test user account",
															function_description = "User.register_user",
															test_function = app.sm.user.register_user("Test User", "Password123"),
															expected_result = "User created successfully",
															print_verbose = (verbosity >= 3)))

			# Test 2.1 End ------------------------------------------------------------------------------------


			# Test 2.2 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Log in as new test user",
															function_description = "User.log_in_user",
															test_function = app.sm.user.log_in_user("Test User", "Password123"),
															expected_result = "Login Success",
															print_verbose = (verbosity >= 3)))

			# Test 2.2 End ------------------------------------------------------------------------------------
    
    
			# Test 1.1 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Joining a test session",
											function_description = "SessionManager.create_session",
											test_function = app.sm.create_session("Test Session 1", public = True, redirect = True),
											expected_result = "Successfully joined session: 'Test Session 1'",
											print_verbose = (verbosity >= 3)))

			# Test 1.1 End ------------------------------------------------------------------------------------


			# Test 1.2 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Joining another test session",
									  			function_description = "SessionManager.create_session",
											test_function = app.sm.create_session("Test Session 2", public = True, redirect = True),
											expected_result = "Successfully joined session: 'Test Session 2'",
											print_verbose = (verbosity >= 3)))

			# Test 1.2 End ------------------------------------------------------------------------------------
	

			# Test 1.2.1 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Joining a private session",
									  			function_description = "SessionManager.create_session",
											test_function = app.sm.create_session("Private session", public = False, redirect = True),
											expected_result = "Successfully joined session: 'Private session'",
											print_verbose = (verbosity >= 3)))

			# Test 1.2.1 End ------------------------------------------------------------------------------------
   
   
			# Test 1.3 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "List both active public sessions",
									  			function_description = "SessionManager.get_remote_session_names",
											test_function = app.sm.get_remote_session_names(),
											expected_result = ['Test Session 1', 'Test Session 2'],
											print_verbose = (verbosity >= 3)))

			# Test 1.3 End ------------------------------------------------------------------------------------
	
 
 			# Test 1.3.1 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Return the first remote session",
									  			function_description = "SessionManager.search_sessions",
											test_function = app.sm.search_sessions("1"),
											expected_result = ['Test Session 1'],
											print_verbose = (verbosity >= 3)))

			# Test 1.3.1 End ------------------------------------------------------------------------------------


			# Test 1.3.2 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Fail to return a result for an invalid search",
												function_description = "SessionManager.search_sessions",
											test_function = app.sm.search_sessions("&"),
											expected_result = "No sessions found",
											print_verbose = (verbosity >= 3)))

			# Test 1.3.2 End ------------------------------------------------------------------------------------


			# Test 1.2.2.0 Start ------------------------------------------------------------------------------------

			results.append(Test(test_name = "Exit private session",
                       							function_description = "SessionManager.leave_session",
														test_function = app.sm.leave_session("Private session"),
														expected_result = "Successfully left session",
														print_verbose = (verbosity >= 3)))
   
			# Test 1.2.2.0 Start ------------------------------------------------------------------------------------


   		# Test 1.2.2 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Delete private session",
									  			function_description = "SessionManager.remove_session",
											test_function = app.sm.remove_session("Private session", app.sm.user),
											expected_result = "Session 'Private session' removed from database",
											print_verbose = (verbosity >= 3)))

			# Test 1.2.2 End ------------------------------------------------------------------------------------
   
   
			# Test 1.4 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Create a new dataset",
									  			function_description = "Session.new_dataset",
											test_function = app.sm.get_session_by_name("Test Session 1").new_dataset("Test Dataset"),
											expected_result = "Dataset 'Test Dataset' successfully created",
											print_verbose = (verbosity >= 3)))

			# Test 1.4 End ------------------------------------------------------------------------------------
	

			# Test 1.5 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Add the first test datasource to the dataset",
									  			function_description = "Session.add_datasource",
											test_function = app.sm.get_session_by_name("Test Session 1").add_datasource("test_data/test_data_a.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data/test_data_a.csv' successfully added to 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.5 End ------------------------------------------------------------------------------------
	

			# Test 1.6 Start ------------------------------------------------------------------------------------

			results.append(Test( test_name = "Compile with the single datasource",
									  			function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Test Session 1").compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'},
																									{'key': 'a', 'diff': 'banana', 'value': '2'},
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 1.6 End ------------------------------------------------------------------------------------


			# Test 1.7 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Add the second test datasource to the dataset",
													function_description = "Session.add_datasource",
											test_function = app.sm.get_session_by_name("Test Session 1").add_datasource("test_data/test_data_b.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data/test_data_b.csv' successfully added to 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.7 End ------------------------------------------------------------------------------------


			# Test 1.8 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile with both datasources",
													function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Test Session 1").compile_dataset("Test Dataset"),
											expected_result =  {'test_data_a.csv + 1 other(s)': [
																														{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'c', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'x', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'x', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'y', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'y', 'diff': 'banana', 'value': '2'}, 
																														{'key': 'z', 'diff': 'apple', 'value': '1'}, 
																														{'key': 'z', 'diff': 'banana', 'value': '2'}
																													]},
											print_verbose = (verbosity >= 3)))

			# Test 1.8 End ------------------------------------------------------------------------------------


			# Test 4 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Update the data display data",
			                    				function_description = "DataConfig.update_dataset",
													test_function = app.sm.get_session_by_name("Test Session 1").display.data_conf.update_dataset(app.sm.get_session_by_name("Test Session 1").compile_dataset("Test Dataset")),
													expected_result = None,
													print_verbose = (verbosity >= 3)))

			# Test 4 End ------------------------------------------------------------------------------------
			

			# Test 4.0.1 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Change graph x axis",
                        							function_description = "DataConfig.change_setting",
                               					test_function = app.sm.get_session_by_name("Test Session 1").display.data_conf.change_setting("x", "key"),
                                    			expected_result = "X key changed to key",
                                       		print_verbose = (verbosity >= 3)))

			# Test 4.0.1 End ------------------------------------------------------------------------------------


			# Test 4.0.2 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Change graph y axis",
                        							function_description = "DataConfig.change_setting",
                               					test_function = app.sm.get_session_by_name("Test Session 1").display.data_conf.change_setting("y", "value"),
                                    			expected_result = "Y key changed to value",
                                       		print_verbose = (verbosity >= 3)))

			# Test 4.0.2 End ------------------------------------------------------------------------------------


			# Test 4.0.3 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Change graph series key",
                        							function_description = "DataConfig.change_setting",
                               					test_function = app.sm.get_session_by_name("Test Session 1").display.data_conf.change_setting("series", "diff"),
                                    			expected_result = "Series key changed to diff",
                                       		print_verbose = (verbosity >= 3)))

			# Test 4.0.3 End ------------------------------------------------------------------------------------
   

			# Test 4.0.4 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Get data config settings",
                        							function_description = "DataConfig.get_settings",
                               					test_function = app.sm.get_session_by_name("Test Session 1").display.data_conf.get_settings(),
                                    			expected_result = {
																										"x": {"options": ["key", "diff", "value"], "selected": "key"},
																										"y": {"options": ["value"], "selected": "value"},
																										"series": {"options": ["key", "diff", "value"], "selected": "diff"},
																										"get": {"options": ["apple", "banana"], "selected": "apple"}
																									},
                                       		print_verbose = (verbosity >= 3)))

			# Test 4.0.4 End ------------------------------------------------------------------------------------

   
			# Test 1.9 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Generate a line graph from the test dataset",
															function_description = "DataDisplay.generate_chart_line",
															test_function = app.sm.get_session_by_name("Test Session 1").display.generate_chart_line(),
															expected_result = None,
															print_verbose = (verbosity >= 3)))

			# Test 1.9 End ------------------------------------------------------------------------------------


			# Test 1.10 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a bar graph from the test dataset",
													function_description = "DataDisplay.generate_chart_bar",
											test_function = app.sm.get_session_by_name("Test Session 1").display.generate_chart_bar(),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 1.10 End ------------------------------------------------------------------------------------


			# Test 1.11 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a pie chart from the test dataset",
													function_description = "DataDisplay.generate_chart_pie",
											test_function = app.sm.get_session_by_name("Test Session 1").display.generate_chart_pie(),
											expected_result = None,
											print_verbose = (verbosity >= 3)))

			# Test 1.11 End ------------------------------------------------------------------------------------


			# Test 1.12 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Remove the second datasource from the test dataset",
													function_description = "Session.remove_datasource",
											test_function = app.sm.get_session_by_name("Test Session 1").remove_datasource("test_data_b.csv", "Test Dataset"),
											expected_result = "Datasource 'test_data_b.csv' successfully removed from 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.12 End ------------------------------------------------------------------------------------


			# Test 1.13 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the test dataset without the second datasource",
													function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Test Session 1").compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 1.13 End ------------------------------------------------------------------------------------


			# Test 1.14 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Rename the test dataset",
													function_description = "Session.rename_dataset",
											test_function = app.sm.get_session_by_name("Test Session 1").rename_dataset("Test Dataset", "New Name"),
											expected_result = "Dataset 'Test Dataset' successfully renamed to 'New Name'",
											print_verbose = (verbosity >= 3)))
				
			# Test 1.14 End ------------------------------------------------------------------------------------


			# Test 1.15 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Fail to compile the old dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Test Session 1").compile_dataset("Test Dataset"),
											expected_result = "Invalid dataset: 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 1.15 End ------------------------------------------------------------------------------------


			# Test 1.16 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the new dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Test Session 1").compile_dataset("New Name"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 1.16 End ------------------------------------------------------------------------------------


			# Test 1.17 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Completely remove the test dataset",
															function_description = "Session.remove_dataset",
															test_function = app.sm.get_session_by_name("Test Session 1").remove_dataset("New Name"),
															expected_result = "Dataset 'New Name' successfully removed",
															print_verbose = (verbosity >= 3)))

			# Test 1.17 End ------------------------------------------------------------------------------------


			# User Tests

			# Test 2.3 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Send a message to the database",
															function_description = "Session.send_message",
															test_function = app.sm.get_session_by_name("Test Session 1").send_message(app.sm.user, "Hello World"),
															expected_result = "Message sent",
															print_verbose = (verbosity >= 3)))

			# Test 2.3 End ------------------------------------------------------------------------------------


			# Test 2.4 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Return the session's chat log",
															function_description = "Session.get_messages",
															test_function = app.sm.get_session_by_name("Test Session 1").get_messages(),
															expected_result = "Test User: Hello World",
															print_verbose = (verbosity >= 3)))

			# Test 2.4 End ------------------------------------------------------------------------------------
    
    
			# Test 1.18 Start ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Leave the first test session",
															function_description = "SessionManager.leave_session",
            											test_function = app.sm.leave_session("Test Session 1"),
															expected_result = "Successfully left session",
                                             print_verbose = (verbosity >= 3)))
	
			# Test 1.18 Start ------------------------------------------------------------------------------------


			# Test 1.19 Start ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Fail to leave a non-existant session",
															function_description = "SessionManager.leave_session",
            											test_function = app.sm.leave_session("Not a session"),
															expected_result = "Not in session",
                                             print_verbose = (verbosity >= 3)))
	
			# Test 1.19 Start ------------------------------------------------------------------------------------
   
   
			# Test 1.20 Start ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Rejoin the first test session",
															function_description = "SessionManager.join_session",
            											test_function = app.sm.join_session("Test Session 1"),
															expected_result = "Successfully joined session: 'Test Session 1'",
                                             print_verbose = (verbosity >= 3)))
	
			# Test 1.20 Start ------------------------------------------------------------------------------------
   
   		
			# User Tests

			# Test 2.5 Start ------------------------------------------------------------------------------------
			
			results.append(Test ( test_name = "Create a new account",
																function_description = "User.register_user",
																test_function = app.sm.user.register_user("Other User", "123Wordpass"),
																expected_result = "User created successfully",
																print_verbose = (verbosity >= 3)))
		
			# Test 2.5 Start ------------------------------------------------------------------------------------
	
	
			# Test 2.6 Start ------------------------------------------------------------------------------------
			
			results.append(Test ( test_name = "Log in to new account",
																function_description = "User.log_in_user",
																test_function = app.sm.user.log_in_user("Other User", "123Wordpass"),
																expected_result = "Login Success",
																print_verbose = (verbosity >= 3)))
		
			# Test 2.6 Start ------------------------------------------------------------------------------------
   
   
			# Test 1.21 Start ------------------------------------------------------------------------------------
			
			results.append(Test ( test_name = "Fail to delete the first test session with a non-creator account",
																function_description = "SessionManager.remove_session",
																test_function = app.sm.remove_session("Test Session 1", app.sm.user),
																expected_result = "User is not creator of session",
																print_verbose = (verbosity >= 3)))
		
			# Test 1.21 Start ------------------------------------------------------------------------------------
		
  
			# User Tests

			# Test 2.7 Start  ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Delete new user",
													function_description = "User.delete_user",
															test_function = app.sm.user.delete_user(),
														expected_result = "User deleted successfully",
												print_verbose = (verbosity >= 3)))

			# Test 2.7 End  ------------------------------------------------------------------------------------
	
	
			# Test 2.8 Start  ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Fail to delete a non-existant user",
															function_description = "User.delete_user",
															test_function = app.sm.user.delete_user(),
															expected_result = "Failed to delete user",
															print_verbose = (verbosity >= 3)))
	
			# Test 2.8 End  ------------------------------------------------------------------------------------
	
	
			# Test 2.9 Start ------------------------------------------------------------------------------------
			
			results.append(Test ( test_name = "Log in as original user",
																function_description = "User.log_in_user",
																test_function = app.sm.user.log_in_user("Test User", "Password123"),
																expected_result = "Login Success",
																print_verbose = (verbosity >= 3)))
		
			# Test 2.9 Start ------------------------------------------------------------------------------------
    
    
			# Test 1.21.1 Start ------------------------------------------------------------------------------------
    
			results.append(Test ( test_name = "Exit first test session",
															function_description = "SessionManager.leave_session",
															test_function = app.sm.leave_session("Test Session 1"),
															expected_result = "Successfully left session",
															print_verbose = (verbosity >= 3)))
    
    		# Test 1.21.1 End ------------------------------------------------------------------------------------
        
    
			# Test 1.21.2 Start ------------------------------------------------------------------------------------
    
			results.append(Test ( test_name = "Exit second test session",
															function_description = "SessionManager.leave_session",
															test_function = app.sm.leave_session("Test Session 2"),
															expected_result = "Successfully left session",
															print_verbose = (verbosity >= 3)))
    
    		# Test 1.21.2 End ------------------------------------------------------------------------------------
    
		  
			# Test 1.22 Start ------------------------------------------------------------------------------------
		
			results.append(Test ( test_name = "Delete the first test session",
															function_description = "SessionManager.remove_session",
															test_function = app.sm.remove_session("Test Session 1", app.sm.user),
															expected_result = "Session 'Test Session 1' removed from database",
															print_verbose = (verbosity >= 3)))
	
			# Test 1.22 Start ------------------------------------------------------------------------------------
   		
    
			# Test 1.22.1 Start ------------------------------------------------------------------------------------
		
			results.append(Test ( test_name = "Delete the second test session",
															function_description = "SessionManager.remove_session",
															test_function = app.sm.remove_session("Test Session 2", app.sm.user),
															expected_result = "Session 'Test Session 2' removed from database",
															print_verbose = (verbosity >= 3)))
	
			# Test 1.22.1 Start ------------------------------------------------------------------------------------
   
   
			# Test 1.23 Start ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Fail to remove a non-existant session from the database",
															function_description = "SessionManager.remove_session",
															test_function = app.sm.remove_session(Session("Not a real session"), app.sm.user),
															expected_result = "Session not in database",
															print_verbose = (verbosity >= 3)))
	
			# Test 1.23 Start ------------------------------------------------------------------------------------
		  
			# User Tests

			# Test 2.10 Start  ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Log out of test account",
													function_description = "User.log_out",
															test_function = app.sm.user.log_out(),
														expected_result = "Logged out",
												print_verbose = (verbosity >= 3)))

			# Test 2.10 End  ------------------------------------------------------------------------------------


			# Test 2.11 Start  ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Log out of no account",
													function_description = "User.log_out",
															test_function = app.sm.user.log_out(),
														expected_result = "Logged out",
												print_verbose = (verbosity >= 3)))

			# Test 2.11 End  ------------------------------------------------------------------------------------


			# Test 2.12 Start ------------------------------------------------------------------------------------
			
			results.append(Test ( test_name = "Log in as original user again",
																function_description = "User.log_in_user",
																test_function = app.sm.user.log_in_user("Test User", "Password123"),
																expected_result = "Login Success",
																print_verbose = (verbosity >= 3)))
		
			# Test 2.12 Start ------------------------------------------------------------------------------------
	

			# Test 2.13 Start  ------------------------------------------------------------------------------------
	
			results.append(Test ( test_name = "Delete test account",
															function_description = "User.delete_user",
															test_function = app.sm.user.delete_user(),
															expected_result = "User deleted successfully",
															print_verbose = (verbosity >= 3)))
	
			# Test 2.13 End  ------------------------------------------------------------------------------------
    
		# Session Tests
		elif len(app.sm.sessions) > 0:

			# Test 3.1 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Create a new dataset",
															function_description = "Session.new_dataset",
															test_function = app.sm.get_session_by_name("Local Session").new_dataset("Test Dataset"),
															expected_result = "Dataset 'Test Dataset' successfully created",
															print_verbose = (verbosity >= 3)))

			# Test 3.1 End ------------------------------------------------------------------------------------


			# Test 3.2 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Add the first test datasource to the dataset",
															function_description = "Session.add_datasource",
															test_function = app.sm.get_session_by_name("Local Session").add_datasource("test_data/test_data_a.csv", "Test Dataset"),
															expected_result = "Datasource 'test_data/test_data_a.csv' successfully added to 'Test Dataset'",
															print_verbose = (verbosity >= 3)))

			# Test 3.2 End ------------------------------------------------------------------------------------


			# Test 3.3 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile with the single datasource",
															function_description = "Session.compile_dataset",
															test_function = app.sm.get_session_by_name("Local Session").compile_dataset("Test Dataset"),
															expected_result = {'test_data_a.csv': [
																																			{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																																			{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																																			{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																																			{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																																			{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																																			{'key': 'c', 'diff': 'banana', 'value': '2'}
																																			]},
															print_verbose = (verbosity >= 3)))

			# Test 3.3 End ------------------------------------------------------------------------------------


			# Test 3.4 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Add the second test datasource to the dataset",
															function_description = "Session.add_datasource",
															test_function = app.sm.get_session_by_name("Local Session").add_datasource("test_data/test_data_b.csv", "Test Dataset"),
															expected_result = "Datasource 'test_data/test_data_b.csv' successfully added to 'Test Dataset'",
															print_verbose = (verbosity >= 3)))

			# Test 3.4 End ------------------------------------------------------------------------------------


			# Test 3.5 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile with both datasources",
															function_description = "Session.compile_dataset",
															test_function = app.sm.get_session_by_name("Local Session").compile_dataset("Test Dataset"),
															expected_result = {'test_data_a.csv + 1 other(s)': [
																																										{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																																										{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																																										{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																																										{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																																										{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																																										{'key': 'c', 'diff': 'banana', 'value': '2'}, 
																																										{'key': 'x', 'diff': 'apple', 'value': '1'}, 
																																										{'key': 'x', 'diff': 'banana', 'value': '2'}, 
																																										{'key': 'y', 'diff': 'apple', 'value': '1'}, 
																																										{'key': 'y', 'diff': 'banana', 'value': '2'}, 
																																										{'key': 'z', 'diff': 'apple', 'value': '1'}, 
																																										{'key': 'z', 'diff': 'banana', 'value': '2'}
																																										]},
															print_verbose = (verbosity >= 3)))

			# Test 3.5 End ------------------------------------------------------------------------------------


			# Test 4.1 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Update the data display data",
			                    				function_description = "DataConfig.update_dataset",
													test_function = app.sm.get_session_by_name("Local Session").display.data_conf.update_dataset(app.sm.get_session_by_name("Local Session").compile_dataset("Test Dataset")),
													expected_result = None,
													print_verbose = (verbosity >= 3)))

			# Test 4.1 Start ------------------------------------------------------------------------------------


			# Test 4.1.1 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Change graph x axis",
                        							function_description = "DataConfig.change_setting",
                               					test_function = app.sm.get_session_by_name("Local Session").display.data_conf.change_setting("x", "key"),
                                    			expected_result = "X key changed to key",
                                       		print_verbose = (verbosity >= 3)))

			# Test 4.1.1 End ------------------------------------------------------------------------------------


			# Test 4.1.2 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Change graph y axis",
                        							function_description = "DataConfig.change_setting",
                               					test_function = app.sm.get_session_by_name("Local Session").display.data_conf.change_setting("y", "value"),
                                    			expected_result = "Y key changed to value",
                                       		print_verbose = (verbosity >= 3)))

			# Test 4.1.2 End ------------------------------------------------------------------------------------


			# Test 4.1.3 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Change graph series key",
                        							function_description = "DataConfig.change_setting",
                               					test_function = app.sm.get_session_by_name("Local Session").display.data_conf.change_setting("series", "diff"),
                                    			expected_result = "Series key changed to diff",
                                       		print_verbose = (verbosity >= 3)))

			# Test 4.1.3 End ------------------------------------------------------------------------------------


			# Test 4.1.4 Start ------------------------------------------------------------------------------------

			results.append(Test (test_name = "Get data config settings",
															function_description = "DataConfig.get_settings",
															test_function = app.sm.get_session_by_name("Local Session").display.data_conf.get_settings(),
															expected_result = {
																										"x": {"options": ["key", "diff", "value"], "selected": "key"},
																										"y": {"options": ["value"], "selected": "value"},
																										"series": {"options": ["key", "diff", "value"], "selected": "diff"},
																										"get": {"options": ["apple", "banana"], "selected": "apple"}
																									},
															print_verbose = (verbosity >= 3)))

			# Test 4.1.4 End ------------------------------------------------------------------------------------
   

			# Test 3.6 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a line graph from the test dataset",
															function_description = "DataDisplay.generate_chart_line",
															test_function = app.sm.get_session_by_name("Local Session").display.generate_chart_line(),
															expected_result = not None,
															print_verbose = (verbosity >= 3)))

			# Test 3.6 End ------------------------------------------------------------------------------------


			# Test 3.7 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a bar graph from the test dataset",
															function_description = "DataDisplay.generate_chart_bar",
															test_function = app.sm.get_session_by_name("Local Session").display.generate_chart_bar(),
															expected_result = not None,
															print_verbose = (verbosity >= 3)))

			# Test 3.7 End ------------------------------------------------------------------------------------


			# Test 3.8 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Generate a pie chart from the test dataset",
															function_description = "DataDisplay.generate_chart_pie",
															test_function = app.sm.get_session_by_name("Local Session").display.generate_chart_pie(),
															expected_result = not None,
															print_verbose = (verbosity >= 3)))

			# Test 3.8 End ------------------------------------------------------------------------------------


			# Test 3.9 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Remove the second datasource from the test dataset",
															function_description = "Session.remove_datasource",
															test_function = app.sm.get_session_by_name("Local Session").remove_datasource("test_data_b.csv", "Test Dataset"),
															expected_result = "Datasource 'test_data_b.csv' successfully removed from 'Test Dataset'",
															print_verbose = (verbosity >= 3)))

			# Test 3.9 End ------------------------------------------------------------------------------------


			# Test 3.10 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the test dataset without the second datasource",
													function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Local Session").compile_dataset("Test Dataset"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 3.10 End ------------------------------------------------------------------------------------


			# Test 3.11 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Rename the test dataset",
													function_description = "Session.rename_dataset",
											test_function = app.sm.get_session_by_name("Local Session").rename_dataset("Test Dataset", "New Name"),
											expected_result = "Dataset 'Test Dataset' successfully renamed to 'New Name'",
											print_verbose = (verbosity >= 3)))

			# Test 3.11 End ------------------------------------------------------------------------------------


			# Test 3.12 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Fail to compile the old dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Local Session").compile_dataset("Test Dataset"),
											expected_result = "Invalid dataset: 'Test Dataset'",
											print_verbose = (verbosity >= 3)))

			# Test 3.12 End ------------------------------------------------------------------------------------


			# Test 3.13 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Compile the new dataset name",
													function_description = "Session.compile_dataset",
											test_function = app.sm.get_session_by_name("Local Session").compile_dataset("New Name"),
											expected_result = {'test_data_a.csv': [
																									{'key': 'a', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'a', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'b', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'b', 'diff': 'banana', 'value': '2'}, 
																									{'key': 'c', 'diff': 'apple', 'value': '1'}, 
																									{'key': 'c', 'diff': 'banana', 'value': '2'}
																								]},
											print_verbose = (verbosity >= 3)))

			# Test 3.13 End ------------------------------------------------------------------------------------


			# Test 3.14 Start ------------------------------------------------------------------------------------

			results.append(Test ( test_name = "Completely remove the test dataset",
													function_description = "Session.remove_dataset",
											test_function = app.sm.get_session_by_name("Local Session").remove_dataset("New Name"),
											expected_result = "Dataset 'New Name' successfully removed",
											print_verbose = (verbosity >= 3)))

			# Test 3.14 End ------------------------------------------------------------------------------------

		# Print the test results

		if verbosity >= 2:

			output_text = ""

			for result in results:
				output_text += result.output["text"]
				output_text += f"\n"

			print(output_text)

		# Print the result summary

		if verbosity >= 1:

			passed_tests = 0
			failed_tests = 0

			for result in results:
				if result.output["passed"] == True:
					passed_tests += 1
				else:
					failed_tests += 1

			summary = f"\nHeadless Test Summary :---:\n\n\t\033[92mPassed\033[0m: {passed_tests}\n\t\033[91mFailed\033[0m: {failed_tests}\n"

			print(summary)

		# Print if any tests failed or not
		else:
			for result in results:
				if result.output["passed"] == False:
					print(f"\nHeadless Test \033[91mFailed\033[0m\n")
					return
			
			print(f"\nHeadless Test \033[92mPassed\033[0m\n")