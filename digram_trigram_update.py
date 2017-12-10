__author__ = 'ian'
import codecs
import numpy as np
import itertools

with codecs.open("readinput.txt","r",encoding="utf-8") as f:
    readString = f.read()
replacedString = readString.replace(" ","$")
replacedString = replacedString.replace(".","$")
replacedString = replacedString.replace(",","$")
replacedString = replacedString.replace(":","$")
replacedString = replacedString.replace("-","$")
replacedString = replacedString.replace("/","$")
replacedString = replacedString.replace("(","$")
replacedString = replacedString.replace(")","$")
replacedString = replacedString.replace("\r","$")
replacedString = replacedString.replace("\n","$")
replacedString = replacedString.replace(";","$")
replacedString = replacedString.replace("\t","$")
replacedString = replacedString.replace("!","$")
replacedString = replacedString.replace("[","$")
replacedString = replacedString.replace("]","$")
replacedString = replacedString.replace("1","$")
replacedString = replacedString.replace("2","$")
replacedString = replacedString.replace("3","$")
replacedString = replacedString.replace("4","$")
replacedString = replacedString.replace("5","$")
replacedString = replacedString.replace("6","$")
replacedString = replacedString.replace("7","$")
replacedString = replacedString.replace("8","$")
replacedString = replacedString.replace("9","$")
replacedString = replacedString.replace("0","$")
replacedString = replacedString.replace("%","$")
replacedString = replacedString.replace("&","$")
replacedString = replacedString.replace("#","$")
replacedString = replacedString.replace("\"","$")
replacedString = replacedString.replace("\'","$")
replacedString = replacedString.replace("=","$")
replacedString = replacedString.replace("+","$")
replacedString = replacedString.replace("<","$")
replacedString = replacedString.replace(">","$")
replacedString = replacedString.replace("?","$")
replacedString = replacedString.replace("^","$")

for i in range(0,100):
    replacedString = replacedString.replace("$$","$")#in instances where multiple $ signs were inserted, we reduce them
replacedString = replacedString.lower()
splitString = replacedString.split('$')
digram_partners = splitString[1::1]
digrams = [m+' '+n for m,n in zip(splitString,digram_partners)]
trigram_partners = splitString[2::1]
trigrams = [m+' '+n+' '+o for m,n,o in zip(splitString,digram_partners,trigram_partners)]
merge_words_digrams_trigrams = splitString# + digrams + trigrams
uniqueWords = list(set(merge_words_digrams_trigrams))

# import the learner's database
with codecs.open("learnersDatabase.txt","r",encoding="utf-8") as f:
    learnersDatabase = f.read()
olddict = learnersDatabase.split("\n")  # converts file into list according to line breaks
olddictCounts = np.zeros((len(olddict)))  # a numpy array storing just the count data from the old dictionary
for word in range(0, len(olddict)-1):  # goes through line by line and splits according to data type
    olddict[word] = olddict[word].split(", ")
    olddict[word][1] = int(olddict[word][1])  # converts the string data into an integer data type
    olddictCounts[word] = olddict[word][1]  # sets numpy value to the same integer as above line
olddict_words = [0]*len(olddict)  # creates a single array with just the words from old dict

for i in range(0, len(olddict)-1):
    olddict_words[i] = olddict[i][0]
combinedList = olddict_words + uniqueWords
completeUniques = list(set(combinedList))
completereadCounts = np.zeros((len(completeUniques)), dtype=int)
for word in range(0, len(olddict)-1):
    get_index = completeUniques.index(olddict_words[word])
    completereadCounts[get_index] = olddict[word][1]

# scan the new text document and update the dictionary
readCounts = np.zeros((len(uniqueWords)), dtype=int)
for unique in range(0, len(uniqueWords)):
    counter = 0
    get_index = completeUniques.index(uniqueWords[unique])
    for word in range(0, len(merge_words_digrams_trigrams)):
        if uniqueWords[unique] == merge_words_digrams_trigrams[word]:
            counter += 1
            completereadCounts[get_index] += 1
        else:
            pass
    readCounts[unique] = counter
ranks =list(-np.argsort(completereadCounts,axis=0))
ranked_words = [x for _,x in sorted(zip(completereadCounts,completeUniques))]
ranked_counts = sorted(completereadCounts)

with codecs.open("learnersDatabase.txt", "w", encoding="utf-8") as f:
    for word in range(-1,-1*len(completeUniques),-1):
        outputString = unicode(ranked_words[word])
        f.write(outputString+', '+str(ranked_counts[word])+'\r\n')


#with codecs.open("ranked_list.txt", "w", encoding="utf-8") as f:
#    for word in range(-1,-1*len(completeUniques),-1):
#        outputString = unicode(ranked_words[word])
#        f.write(outputString+', '+str(ranked_counts[word])+'\r\n')