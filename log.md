> Commit: GUI keys
>
> - Added keys to each GUI element so that it can be accessed later

> Commit: GUI menus
>
> - Created python files for each menu
> - Implemented each menus GUI elements
> - app.py now opens the login GUI if remote or the DES viewer if local

> Commit: Blocking session deletion when in use
>
> - The session manager now checks if the find link by session function returns a value before deleting the session
> - Changed the find by functions to return data rather than a cursor

> Commit: Tracking user sessions
>
> - Created a session user manager class which creates, breaks and finds links between users and sessions
> - Joining and leaving a session now create and break links
> - Deleting a user now breaks all links to that user
> - Modified headless testing to correctly leave all sessions
> - The session user manager now can find links by either username or session
> - Unbound session deletion from current sessions
> - Changed get all session function to actually return an array instead of a cursor

> Commit: Data config display
>
> - The data config class now also has a function which returns a structured collection of data
> - Added a headless test to check that the correct result is returning
> - Updated the test module to also include its own dictionary comparer

> Commit: Data config changing
>
> - The data config class now has a function to change a heading
> - This works by taking two strings, a heading and a key
> - The key a string of one of: x, y, series, or get
> - The heading is a string representing the custom value that this key should be changed to
> - The function checks that the values are all valid before changing anything
> - This does allow for the same value to be set for multiple keys, but this actually works with matplotlib since the only requirement is that the y key is a number
> - Added headless tests to set the test graphs to the correct settings

> Commit: Seperating create and join room functions
>
> - Seprated create and join functions
> - Create function takes a redirect boolean argument which will tell it if it should try to join the room if it already exists
> - Updated headless test to use correct function

> Commit: Allowing for graph configuration options
>
> - Created a data configuration class which stores and handles the settings for the data being shown by the data display
> - The data display now has a data configuration which it uses in place of function values

> Commit: Adjusting headless testing comparer to more accurately check
>
> - Gave the variables on the bar graph data display function more descriptive names
> - Changed the headless testing to compare if both the expected and actual result have the exact same number of the exact same values
> - I am making the headless checker compare the values based on type with a switch since every type needs to be compared slightly differently
> - Never mind that, I can just sort the two results before comapring them to make sure they will always be the same

> Commit: Session searching and publicity
>
> - Added a function to the session manager which takes a search term and returns a list of results containing the search term
> - Added headless tests for searching sessions
> - Added public value to session class
> - Database manager now pushes and pulls publicity to/from the database
> - Session manager now only returns public sessions when getting all sessions
> - Added headless tests for session publicity
> - Fixed issue with headless tests not comparing their expected and outputted result correctly
> - Changed remove session function to take a session name instead of the whole session

> Commit: Command line arguments
>
> - app.py now parser arguments for remote mode and headless testing mode / test result verbosity
> - Replaced the app classes instantiating headless flag with a verbosity level which automatically triggers the headless test if it is 0 or more

> Commit: Logging out and removing users from database
>
> - Added function to user class to log out user
> - Added function to delete a user from the database by name in the user class and user manager class
> - Added headless tests for log out and user removal, log out should currently always succeed since it will always set the username to none no matter what
> - Added some formatting to the headless output in the form of coloured text and bold test headings

> Commit: Ending sessions / Storing session user data
>
> - Added function to session manager which removes session from database
> - Added headless tests for successful and failed session removal
> - Sessions now track their creator and current users
> - Session managers are sessions now take a user when initialising
> - Replaced the remote flag when initialising sessions with a check for if a user is set
> - Session removal also takes a user which must match the creator of the session
> - Added headless tests for user creation and log in

> Commit: Leaving sessions
>
> - Added leave session function to session manager'
> - Adjusted headless comment naming for clarity
> - Added headless tests for successfully and unsuccessfully leaving sessions
> - Changed headless result checking to allow for arrays in different orders
> - Database connection can now remove sessions

> Commit: Headless testing simplification and summary
>
> - Created a Test class which returns a result string and pass/fail bool when created
> - Updated headless testing to use Test classes instead of existing process
> - Added a final print to the headless testing which states how many tests passed and how many failed
> - Changed verbose argument to verbosity now using a number between 0 and 3 instead of a boolean

> Commit: Better headless reporting
>
> - Verbose headless testing now returns the expected and actual result
> - Headless testing now returns a simple pass/fail message for each test to make the output cleaner

> Commit: Added verbose headless testing mode
>
> - Removed data display import from headless.py
> - Changed headless testing from using individual modules to taking one app object
> - Gave the headless testing a verbose argument
> - Each headless test now has extra information if verbose mode is used

> Commit: Headless mode (basic run through)
>
> - Added remote flag to app.py
> - Added headless flag to app.py
> - Created Headless class which stores a series of commands and their arguments
> - app.py can now run through all of the commands in headless.py if the headless flag is active
> - Removed existence check from the join_session function
> - Changed the join_session function in the session manager to have a more descriptive name or join_or_create_session
> - Newly created sessions now also push themselves to the database after pulling
> - Added docstrings to all functions
> - Fixed an issue with dataset renaming not properly applying

> Commit: Session manager
>
> - Created session manager class to manage multiple sessions
> - Added function to database connection class to retrieve all sessions
> - Added function to session manager to select a session
> - Adjusted the session manager to hold a list of sessions

> Commit: User integration
>
> - Creating an account now automatically sets the user to the newly created one
> - Sending a chat message now takes a user object and extracts the name from that

> Commit: Accounts
>
> - Created a user class to store the currently signed in user
> - Database connection class now has functions to create and retrieve users
> - Seperated the user database connection into its own class to seperate responsibilities

> Commit: Chat system
>
> - Created a chat class which creates and holds messages
> - Created a message class which hold information about a message
> - Fixed an incorrect reference to files in the database connection class
> - Sessions now have a chat which they control to also connect chat to the database
> - Chat messages are also now pushed and pulled from/to the database

> Commit: Data management unification
>
> - A session now has a database manager if it is set as remote when created
> - The file manager is now interacted with through the session functions which also run database functions if available
> - Graph generation now uses a try statement to catch any issues with data compilation
> - Renamed the files variable in session to \_files to avoid accidental usage since it should only be used through the session

> Commit: Database connection
>
> - Moved remote mode files into main folder
> - Created a database connection class to push and pull the locally stored session data to the mongo database
> - Created a session class which holds information and data from a session
> - Created a config file to store database configuration settings

> Commit: Generating Graphs
>
> - Created functions to generate line, pie and bar graphs
> - Updated file manager importer function to get csv data
> - Data complier now returns data as a key value pair of chart name and chart data for easier generation

> Commit: File manager
>
> - Moved remote mode specific files to their own folder for now to keep the working path clean.
> - Created file manager class and its functions to add, remove or rename a dataset, add/remove a file and compile a dataset.

> Commit: Project environment setup
>
> - Created a requirements.txt file with all necesary packages.
> - Creates some starting classes for the application
