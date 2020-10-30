import pickle
import random
for m in range(1, 13, 1):
	for d in range(1, 32, 1):
		ukw = []
		auswahl = []
		for i in range(0, 259, 1):
			auswahl.append(i)
			ukw.append(260)
		while len(auswahl) != 0:
			e = random.choice(auswahl)
			i = random.choice(auswahl)
			auswahl.pop(auswahl.index(e))
			if auswahl.count(i) != 0:
				auswahl.pop(auswahl.index(i))
			ukw[i] = e
			ukw[e] = i
		with open("plugboards/" + str(m) + "/" + str(d) + ".pkl", "wb") as f:
			pickle.dump(ukw, f, pickle.HIGHEST_PROTOCOL)
