1. What is the output of the program 
	t = 2 * (2,3)
	print(t)

2. What gets printed here? 
	print(r"\nwoow")

3. What is the length of following list?
	A = [ 1,2,3,None,(), [] ]

4. What gets printed here?

	D = lambda p:p x 2                                                           
	T = lambda p:p x 3                                                         
	Y = 2 
	X = D(Y)  
	Y = T(X)
	X = D(Y)
	print(X)
	
5. How many except statements can a try-except block have?

	a) 0
	b) 1
	c) More than 1
	d) More than 0

6. Is the following code valid?                                   
	try:                                                                        		# Do something                                                    
	except:
		# Do something
	else:    
		# Do something

	a) No there is no such a thing as else with try / except
	b) No there is no such a thing as else
	c) No else must always come before except
	d) Yes

7. Can one block of try statements handle multiple blocks of except statements?

	a) Yes like except TypeError, SyntaxError
	b) Yes like except [TypeError, SyntaxError]
	c) No
	d) None of the above

8. What is the output of the following program? 
	def f():                                                                         
		try:                                                                     	print(1)                                                     
		finally:                                                                 	print(2)

	a) 1 2
	b) 1
	c) 2
	d) None

9. What happens when '1' == 1 is executed?
	a) True
	b) False
	c) TypeError
	d) ValueError

10. What is the output of the following ?                  
	my_string = 'abcdefghijklsdjflj'
	k = [print(i) for i in my_string if i not in "aeiou"]

	a) prints all the vowels in my_string
	b) prints all the consonants in my_string
	c) prints all characters of my_string that aren't vowels
	d) prints only on executing print(k)

11. What does os.name contain?
	
	a) Name of the operating system
	b) The address of the module
	c) Error, it should have been os.name()
	d) None of the above


12. What does os.fchmod(fd,mode) do?
	
	a) Change the permission bits of a file
	b) Change the permission bits of a file or directory
	c) Change the permission bits of a directory
	d) None of the above

13. Which of the following returns a present working directory ?
	
	a) os.getcwd()
	b) os.pwd()
	c) os.cwd()
	d) os.getpwd()

14. What is the difference between bash, .bashrc and .bash_profile?

15. What are environment variables in bash? Give some examples?

16. What is the difference between expression and a statement in python?

17. Explain what the following functions does in python?  
	1. zip     
	2. sorted and sort - explain the difference   

18. Explain what the following functions does in python?
	1. setattr and getattr                                                 
	2. slice

19. Explain the following commands.                    
	1. cat (what happens when cat commands are combined with redirection >)  
	2. chmod

20. Explain the following commands.  	                                                      
	1. man/info     
	2. chown
