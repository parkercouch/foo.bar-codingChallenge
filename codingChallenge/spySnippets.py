# Spy snippets
# ============
# 
# You've been recruited by the team building Spy4Rabbits, a highly advanced 
# search engine used to help fellow agents discover files and intel needed to 
# continue the operations against Dr. Boolean's evil experiments. The team is 
# known for recruiting only the brightest rabbit engineers, so there's no 
# surprise they brought you on board. While you're elbow deep in some important 
# encryption algorithm, a high-ranking rabbit official requests a nice 
# aesthetic feature for the tool called "Snippet Search." While you really 
# wanted to tell him how such a feature is a waste of time in this intense, 
# fast-paced spy organization, you also wouldn't mind getting kudos from a 
# leader. How hard could it be, anyway?
# 
# When someone makes a search, Spy4Rabbits shows the title of the page. Your 
# commander would also like it to show a short snippet of the page containing 
# the terms that were searched for. 
# 
# Write a function called answer(document, searchTerms) which returns the 
# shortest snippet of the document, containing all of the given search terms. 
# The search terms can appear in any order.
# 
# The length of a snippet is the number of words in the snippet. For example, 
# the length of the snippet "tastiest color of carrot" is 4. (Who doesn't like 
# a delicious snack!)
# 
# The document will be a string consisting only of lower-case letters [a-z] and 
# spaces. Words in the string will be separated by a single space. A word could 
# appear multiple times in the document.
# searchTerms will be a list of words, each word comprised only of lower-case 
# letters [a-z]. All the search terms will be distinct.
# 
# Search terms must match words exactly, so "hop" does not match "hopping".
# 
# Return the first sub-string if multiple sub-strings are shortest. For 
# example, if the document is "world there hello hello where world" and the 
# search terms are ["hello", "world"], you must return "world there hello".
# 
# The document will be guaranteed to contain all the search terms.
# 
# The number of words in the document will be at least one, will not exceed 
# 500, and each word will be 1 to 10 letters long. Repeat words in the document 
# are considered distinct for counting purposes.
# The number of words in searchTerms will be at least one, will not exceed 100, 
# and each word will not be more than 10 letters long.


def answer(document, searchTerms):
	
	# Easier to iterate through a list
	document = document.split(" ")
	doc_length = len(document)
	# Easier to check for subset
	term_length = len(searchTerms)
	searchTerms = set(searchTerms)

# Sweeping from min list required to whole document; not fast but should work
# And there has to be a better way to loop, but I'm too tired to think
	for x in range(0, (doc_length - term_length)):
		i = 0
		for j in range((term_length + x), doc_length + 1):
			if searchTerms <= set(document[i:j]):
				return ' '.join(document[i:j])
			else:
				i += 1
				j += 1