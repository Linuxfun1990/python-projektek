
class Cup:
	color = None
	empty = True



	def __init__(self, color, empty):
		self.color = color
		self.empty = empty

class Empoloyee:
	def __init__(self, name, email, phone, address):
		self.name = name
		self.email = email
		self.phone = phone
		self.address = address

john = Empoloyee(
	"John",
	"john@gmail.com",
	"06707617628",
	"Budapest"
	)

tom = Empoloyee(
	"Tom",
	"tom@gmail.com",
	"06707617629",
	"Debrecen"
	)

print(john.name, john.email, john.phone,john.address)
print(tom.name,tom.email, tom.phone, tom.address)

		