#The using of n-stage LDA method

import gensim
import string
from gensim import corpora, models
from gensim.models import LdaModel
from gensim.models import CoherenceModel
import time

def n_stage_LDA(model_name, topic_no, stage_no, word_num, sentencesTokens)
	#n-stage processes
	for stage in range(2, stage_no+1):
		#Load your LDA model
		lda = gensim.models.LdaModel.load(str(model_name) + '.model')
		info_LDA = lda.show_topics(num_topics= topic_no, num_words=word_num)
		topics = str(info_LDA).split('\'), (')
		topics[0] = str(topics[0])[2:]

		words = []
		weights = []
		totalWords = []
		for topic in topics:
			i = str(topic).find(',')
			topicNo = topic[:i]
			words_weights = str(str(topic[i+3:]).strip()).split('+')
			total_weight = 0
			for wordInfo in words_weights: #Determining words and values for each topic
				wordInfo = str(wordInfo).strip()
				i = str(wordInfo).find('*')
				weightValue = wordInfo[:i]
				k = str(wordInfo).rfind('"')
				wordValue = wordInfo[i+2:k]
				if weightValue != "0.0001": #Evaluation of words with a weight above 0.0001 or your value
					total_weight += float(weightValue) 
					weights.append(weightValue) #Calculation total weight for each topic
					words.append(wordValue)
				else:
					break

			tWords = words #storage words list
			average_weight = total_weight/(len(weights)) #Calculation threshold weight value for each topic seperately
			wordCount = 0
			#Create a new word list based on average weight by looking at the weight of each word
			for weight in weights:
				if float(weight) >= average_weight:
					totalWords.append(tWords[wordCount])
					wordCount += 1
				else:
					break
			#Removing contents in words and weights lists for other topic
			words.clear()
			weights.clear()

		totalWords = list(set(totalWords)) #Obtaining unique total words 
		print("New word list is created!")

		#Updating previous sentence's tokens according to total words list and creating new list for this
		sentences = sentencesTokens
		iterative_texts = []
		for text in sentences:
			tokens = [i for i in text if i in totalWords]
			iterative_texts.append(tokens)

		print("New word vocabulary is created! New count: " + str(len(totalWords)))

		#Creating a new LDA model stage
		model_name = model_name + str(stage) + '-LDA'
		dictionary = corpora.Dictionary(iterative_texts)
		dictionary.save( model_name + '.dict')
		corpus = [dictionary.doc2bow(iter) for iter in iterative_texts]
		gensim.corpora.MmCorpus.serialize(model_name + '.mm', corpus)
		print("New corpus&dictionary is created!")
		
		start = time.time()
		ldamodel = LdaModel(corpus, num_topics = topic_no, id2word = dictionary, iterations = 100, passes = 10, alpha = 'asymmetric')
		ldamodel.save(str(model_name) + '.model')
		end = time.time()
		print(str(stage) + '-LDA model ise created! RunTime:' + str(end-start))