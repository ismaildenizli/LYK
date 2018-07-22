
from random import choice

def dice_roll():
	return choice(range(1,7))
def head_or_tail():
	return choice(["head","tail"])
def rock_paper_scissors():
	return choice(["rock","paper","scissors"])
print(dice_roll())
