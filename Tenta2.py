def calculate_loan():
  property_price = int(input("property price: "))
  loan_size = int(input("loan size: ".ljust(16)))
  interest_rate = float(input("interest rate: ".ljust(16)))

  if float(loan_size/property_price) >= 0.7:
    amortization_rate = 0.02
  elif float(loan_size/property_price) >= 0.5:
    amortization_rate = 0.01
  else:
    amortization_rate = 0

  amortization = property_price*amortization_rate/12
  interest = interest_rate*loan_size/(100*12)
  total = amortization +interest

  print("per month")
  print("-"*13)
  print("amortization:",amortization)
  print("interest:".ljust(13),interest)
  print("total:".ljust(13),total)


def code_words(text,dictionary):
  text_list = text.split()
  for i in range(len(text_list)):
    if (text_list[i] in dictionary.keys()):
      text_list[i] = dictionary.get(text_list[i])
  #return " ".join(text_list)
  rtn_text = ""
  for word in text_list:
    rtn_text+=word +" "
  return rtn_text.strip()

d = {"happiness": "cake", "homework": "date"}
print("you have your happiness")
print(code_words("you have your happiness", d))


class Robot:
  def __init__(self):
    self.directions = ['NORTH','EAST','SOUTH','WEST']
    self.direction = 'NORTH'
    self.xPos = 0
    self.yPos = 0
  
  def turnLeft(self):
    self.direction = self.directions[(self.directions.index(self.direction)-1)%4]
  
  def forward(self, n):
    if (self.direction == 'NORTH'):
      self.yPos += n
    elif (self.direction == 'SOUTH'):
      self.yPos -= n
    elif (self.direction == 'EAST'):
      self.xPos += n
    elif (self.direction == 'WEST'):
      self.xPos -= n

class Robot:
  def __init__(self):
    self.directions = ["NORTH","EAST","SOUTH","WEST"]
    self.direction = 'NORTH'
    self.xPos = 0
    self.yPos = 0
  def turnLeft(self):
    self.direction = self.directions[(self.directions.index(self.direction)-1)%4]
  def forward(self, n):
    match self.direction:
      case 'NORTH':
        self.yPos += n
      case 'SOUTH':
        self.yPos -= n
      case 'EAST':
        self.xPos += n
      case 'WEST':
        self.xPos -= n


#calculate_loan()
r = Robot()
r.turnLeft()
r.forward(10)
print(r.xPos,r.yPos, r.direction)