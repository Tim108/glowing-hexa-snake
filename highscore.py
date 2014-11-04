#
fs = "scores.txt"

def get():
	f = open(fs, "r")
	scores = []
	for line in f:
		scores.append(line)
	f.close()
	return scores

def add(score):
	f = open(fs, "r+")
	scores = get()
	scores.append(str(score) + "\n")
	scores.sort(reverse=True, key=int)
	f.truncate()
	for i in range(10):
		if(i < len(scores)):
			a = str(scores[i])
			f.write(a)
	f.close()

