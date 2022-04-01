import random
import json

global scoreJoueur
scoreJoueur = 0

def write_json(new_data, filename='JSON/rochePapierCiseauxLeaderboard.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["joueurs"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def RochePapierCiseaux():
	# Set le score glabalement et demander au joueur ce qu'il veut jouer
	global scoreJoueur
	print ('Choisissez votre main : ')
	reponseJoueur = input()
	testRandomRPC = random.randint(0,2)

	# Si le joueur a une reponse possible...
	if reponseJoueur.casefold() in optionsBotRPC:
		# S'il a la mm main que l'ordinateur, print le message
		if (reponseJoueur.casefold()).__eq__(optionsBotRPC[testRandomRPC].casefold()):
			print("Vous avez tous les deux choisis la meme main")
		# S'il gagne, print le message et augmenter le score
		elif reponseJoueur.casefold() == "papier" and testRandomRPC == 0 or reponseJoueur.casefold() == "ciseaux" and testRandomRPC == 1 or reponseJoueur.casefold() == "roche" and testRandomRPC == 2:
			print ("Vous avez gagné!")
			scoreJoueur += 1
		# S'il perd, print le message et diminuer le score
		else:
			print ("Vous avez perdu...")
			scoreJoueur -= 1
		# Offrir au joueur de recommencer a jouer, ou de quitter le jeu
		RejouerRPC()
	# Sinon... recommencer le choix
	else :
		print("Cette réponse n'est pas acceptée")
		RochePapierCiseaux()

def RejouerRPC():
	# Offrir de recommencer
	print('Rejouer? (y/n)')
	rejouer = input();
	# S'il desire recommencer, le faire recommencer
	if rejouer == "y":
		RochePapierCiseaux();
	# S'il ne veut pas...
	elif rejouer == "n":
		# Demander si le joueur veut sauvegarder son score
		print('Désirez vous sauvegarder votre score? (y/n)')
		sauvegarderScore = input();
		# S'il veut, lui demander son nom, mettre a jour le fichier json et faire apparaitre le LEADERBOARD
		if sauvegarderScore == "y":
			print ('Veuillez inscrire votre nom')
			nomJoueur = input()
			valeursNouvelles = {"nom":nomJoueur, "score": scoreJoueur}
			write_json(valeursNouvelles)
			print('LEADERBOARD')
			item = json.load(open("JSON/rochePapierCiseauxLeaderboard.json"))
			for i in item['joueurs']:
				print(i)
		# S'il ne veut pas, le faire partir
		elif sauvegarderScore == "n":
			print('Bonne journée!')
		# Si la reponse n'est pas valable, lui dire et faire recommencer le choix
		else:
			print('Réponse non valable.')
			RejouerRPC()
	# Si la reponse n'est pas valable, lui dire et faire recommencer le choix
	else:
		print("Réponse non valable.")
		RejouerRPC()

# Commencer la partie
print('Bienvenue dans une partie de roche papier ciseaux or whatevs')
optionsBotRPC = ["roche", "papier", "ciseaux"]
RochePapierCiseaux()
