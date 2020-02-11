def sentence(*apam):
	'''把列表中的单词拼接成一个句子'''

    word = ''
    for i in apam[1:len(apam)-1]:
        word += (i+' ')
    sentence = apam[0].title() + ' ' + word + 'and '+apam[-1]+'.'
    return sentence


ls = ['apple','bananas','tofu','cats','pich','huoche']
print (sentence(*ls))