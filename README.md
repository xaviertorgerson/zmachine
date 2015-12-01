Emulator of the Oxford Z Machine

The Z Machine was described here http://blog.jgc.org/2013/05/the-two-problems-i-had-to-solve-in-my.html in a blog post by John Graham-Cumming.  It was a theoretical machine that was used in interviewing brainteasers at Oxford University, UNTIL NOW!

The Z Machine has a simple memory layout representing an infinite array where the first element corrosponds to index 0.  The memory can be opperated on by simple commands.
My Z Machine emulator uses all of the classic commands
	Z - Zeros a memory location
		Example: Z2 sets memory location 2 to 0
	I - Increments a memory location
		Example: I3 adds 1 to whatever is currently stored in location 3
	J - Compares two memory locations and branches if they are different
		Example: J18,19,3 would compare the contents of memory locations 18 and 19, if they are different the program runs from line 3

I have also included the A command for ease-of-use
	A - Assigns a value to a memory location
		Example: A4,7 assigns 7 to memory location 4

Try running testAdder.z with 
	python zmachine.py testAdder.z

	It adds the numbers 3 and 10 for the spoooky result of 13
	


