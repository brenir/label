#ex.py

def label(wordSeq,tagList,t_tags,w_tags,t_tags):
	#init
	delta=[]
	psi=[]
	for i in range(len(wordSeq)):
		tempDelta = []
		tempPsi = []
		for tag in tagList:
			max = delta[i-1][0]*w_tags[wordSeq[i]+tag]*t_tags[tagList[0]+tag]
			argmax = 0
			for j in range(1:len(tagList)):
				value = delta[i-1][j]*w_tags[wordSeq[i]+tag]*t_tags[tagList[j]+tag]
				if value > max:
					max = value
					argmax = j
			tempDelta.append(max)
			tempPsi.append(argmax)	
			
		delta.append(tempDelta)
		delta.append(tempPsi)
	

def main():
	infile = open('dev.gb.conll06','r')
	words = {}
	tags = {}
	t_tags = {}
	w_tags = {}
	
	sentences = infile.read().split("\n\n")
	for sentence in sentences:
		brackets = sentence.split("\n")
		length = len(brackets)
		
		for i in range(length-1):
			
			w = brackets[i].split()[1]
			try:
				words[w] = words[w] + 1
			except KeyError:
				words[w] = 1
				
			t = brackets[i].split()[3]
			try:
				tags[t] = tags[t] + 1
			except KeyError:
				tags[t] = 1
			9o
			wt = w + "_" + t
			try:
				w_tags[wt]	= w_tags[wt] + 1
			except KeyError:
				w_tags[wt] = 1
				
			tt = t + "_" + brackets[i+1].split()[3]
			try:
				t_tags[tt] = t_tags[tt] + 1
			except KeyError:
				t_tags[tt] = 1
		
		w = brackets[length-1].split()[1]
		try:
			words[w] = words[w] + 1
		except KeyError:
			words[w] = 1
				
		t = brackets[length-1].split()[3]
		try:
			tags[t] = tags[t] + 1
		except KeyError:
			tags[t] = 1
			
		wt = w + "_" + t
		try:
			w_tags[wt]	= w_tags[wt] + 1
		except KeyError:
			w_tags[wt] = 1
	
	
		
		for k in t_tags:
			ks = k.split("_")[0]
			t_tags[k] = float(t_tags[k])/tags[ks]
			
		for k in w_tags:
			ks = k.split("_")[1]
			w_tags[k] = float(w_tags[k])/tags[ks]
			
		tagList = tags.keys()
			
		
		infile2 = open(' ','r')
		sentences = infile2.read().split("\n\n")	