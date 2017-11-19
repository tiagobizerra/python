# Working with strings

# assign strings
brian = "Hello life!"

caesar = "Graham"
praline = "John"
viking = "Teresa"

print caesar
print praline
print viking

# print specials characters correctly
print  'This isn\'t flying, this is falling with style!'

# Access by index

c = "cats"[0]
n = "Ryan"[3]

"""
index always start on 0
"PYTHON"[1] will print 'Y', not 'P'
"""
fifth_letter = "MONTY"[4]
print fifth_letter

### String methods
# len()
parrot = "Norwegian Blue"
print len (parrot)

# lower()
print parrot.lower()

# upper()
print parrot.upper()

# str()
pi = 3.14
print str(pi)

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

# simple string print
print "Monty Python"

#assign string and print
the_machine_goes = "Ping!"
print the_machine_goes


# String Concatenation
print "String Concatenation"

print "Spam " + "and " + "eggs"

print "The value of pi is around " + str(3.14) 

# String formatting with %
# part 1
string_1 = "Camelot"
string_2 = "place"

print "Let's not got to %s. 'Tis a silly %s." % (string_1, string_2)

# part 2

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# Exercise

my_string = "eh nois!"
print len(my_string)
print my_string.upper()
