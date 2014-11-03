
f = "scores.txt"

def get():
	open(f, "r")
	scores = []
	for i in range(10):
		scores[i] = f.readLine()
	f.close()

def add(score):
	open(f, "w")
	scores = get()
	scores.append(str(score))
	scores.sort(reverse=True)
	for i in range(10):
		f.write(str(score) + "\n")
	f.close()

