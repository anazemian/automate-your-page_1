def geneterate_concept_HTML(concept_title, concept_description):
	html_text_1='''
<div class="concept">
	<div class="concept-title">
		''' + concept_title
	html_text_2 = '''
	</div>
	<div class="concept-description">
		''' + concept_description
	html_text_3 = '''
	</div>
</div>'''

	full_html_text = html_text_1 + html_text_2 + html_text_3
	return full_html_text

def get_title(concept):
	start_location = concept.find('TITLE:')
	end_location = concept.find('DESCRIPTION:')
	title = concept[start_location+7 : end_location-1]
	return title

def get_description(concept):
	start_location = concept.find('DESCRIPTION:')
	description = concept[start_location+13 :]
	return description

def get_concept_by_number(text, concept_number):
	counter = 0
	while counter < concept_number:
		counter = counter + 1
		next_concept_start = text.find('TITLE:')
		next_concept_end = text.find('TITLE', next_concept_start + 1)
		if next_concept_end >= 0:
			concept = text[next_concept_start:next_concept_end]
		else:
			next_concept_end = len(text)
			concept = text[next_concept_start:]
		text = text[next_concept_end:]
	return concept

	
	
TEST_TEXT = """TITLE: Python
DESCRIPTION: Python is a programming language. It provides a programmer a way to write
instructions in way a computer can understand and then execute using arithmetic expressions.
TITLE: The Variable 
DESCRIPTION: A <Name> in Python can be any sequence of letters, numbers, and underscores(_) that does not
start with a number. We usually use all lowercase letters for variables names, but capitalization
must match exactly. Here are some valid examples of names in Python:
my_name
one2one
Dorino
this_is_a_very_long_variable_name
TITLE: Strings
DESCRIPTION: Strings are generally text values. The will be defined with a start and an end quote. 
Such as 'Lee' or "Lee". The quotations that you start and end with must be the same. 
You can not start with a single and end with a double. If you do not end a quote it will be an error.
This makes it very handy for using the other kind in the text as 
EVERYTHING will be concidered text until you have closed the quotation. 
So you can write print "The landscapers forgot to bring their tools today. They'll need to go back to get them.". 
This would return a value of The landscapers forgot to bring their tools today. They'll need to go back to get them.
TITLE: Loops
DESCRIPTION: A loop is just what is sounds like, a loop of an action that just repeates. We start with the WHILE loop.
TITLE: While Loops
DESCRIPTION: The WHILE loop starts with an expression that will validate the running of the loop followed by a colon.
This is called a test expression. Inside of that we have the block that will run as long as the test expression is true.
The difference between this and IF command, is that once it runs the command will go back to check if the test expression is still true. If it is, 
the block of code will run again and again and again until the test expression returns a false value.
TITLE: Break Statement
DESCRIPTION: A break statement is a way to stop the loop even when the loop is still returning TRUE. You could stick this 
in an IF command in the WHILE loop which will check to see if there is a reason to break the process or let it continue.
If this IF statement is TRUE and you break the loop, you will then continue the code after the while loop. If the IF statement is false, 
it will continue to run the code and the loop and will check the IF statement the next time around.
TITLE: Debugging
DESCRIPTION: Bugs happen in any and all code. It is inevitable to have an error in code, however DEbugging will help correct these errors. 
Not all bugs will crash a program which makes it a little harder to spot the bug. Sometimes bugs are as simple as trying to 
concatinate a string and a value, but sometimes they are more complex and will still return an output, a wrong output."""

def generate_all_html(text):
	current_concept_number = 1
	concept = get_concept_by_number(text, current_concept_number)
	all_html = ''
	while concept != '':
		title = get_title(concept)
		description = get_description(concept)
		concept_html = geneterate_concept_HTML(title,description)
		all_html = all_html + concept_html
		current_concept_number = current_concept_number + 1
		concept = get_concept_by_number(text, current_concept_number)
	return all_html

print generate_all_html(TEST_TEXT)

		