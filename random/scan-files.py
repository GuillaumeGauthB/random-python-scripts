# A pretty useless script that compiles every txt files in the script's folder
# Was made because i was bored and wanted to check how long my notes were when all compiled, and i was too lazy to check it myself

from pathlib import Path

finalText = open(r"txtFinal.txt", "w")
finalText.write("")
finalText.close()

finalText = open(r"txtFinal.txt", "a")
currentDirectory = Path('.')

txt = list(currentDirectory.glob('*.txt'))

print(txt)

for x in txt:
	textToPrint = str(x)
	currentText = open(r"%s"%textToPrint, "rb")
	text = currentText.read().decode('utf-8', 'ignore')
	print(text)
	# This line causes errors for some reason, too braindead to fix it, rest of script works
	finalText.writelines(text)
	currentText.close()
	
finalText.close()
