class Pokemon:
	
	def __init__(self, name, strength, life):
		self.name = name
		self.strength = int(strength)
		self.life = int(life)
	
	def attack(self, other):
		other.life -= self.strength

picachu = Pokemon('Picachu', 48, 100)
puff = Pokemon('puff', 55, 100)
turno = 1

while ((picachu.life > 0) & (puff.life >0)):
	if turno == 1:
		picachu.attack(puff)
		turno = 0
	if turno == 0:
		puff.attack(picachu)
		turno = 1 

if picachu.life > 0:
	print("Picachu wins!")
	
else:
	print("Puff wins!")
