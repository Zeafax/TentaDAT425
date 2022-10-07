def legal_status(age):
  if (age <18 ):
    return 'minor'
  elif (age <21 ):
    return 'adult'
  elif (age <30):
    return 'alcohol'
  elif (age <35):
    return 'senator'
  else:
    return 'president'

def legal_status(age):
  if age < 18:return 'minor'
  if age < 21:return 'adult'
  if age < 30:return 'alcohol'
  if age < 35:return 'senator'
  return 'president'

def legal_status(age):
  if age < 18:
    rtn_text = 'minor'
  elif age < 21:
    rtn_text = 'adult'
  elif age < 30:
    rtn_text = 'alcohol'
  elif age < 35:
    rtn_text = 'senator'
  else:
    rtn_text = 'president'
  return rtn_text

def duplicates(input_list):
  rtn_list = []
  for i in range(len(input_list)):
    if(input_list.count(input_list[i]) > 1):
      if ( input_list[i] not in rtn_list):
        rtn_list.append(input_list[i])
  return rtn_list

def duplicates(xs):
  rtn_list = []
  for i in xs:
    if xs.count(i) > 1 and i not in rtn_list:
      rtn_list.append(i)
  return rtn_list


class Doorlock:
  def __init__(self, pin):
    self.pin = pin
    self.isClosed = False
  
  def lock(self):
    if (self.isClosed):
      return False
    else:
      # self.isClosed -> False
      self.isClosed = True
      return True
  
  def unlock(self, pin):
    if (not self.isClosed):
      return False
    if (self.pin == pin):
      self.isClosed = False
      return True
    else:
      return False

  def set_pin(self, pin, new_pin):
    if (self.pin == pin):
      if (not self.isClosed):
        self.pin = new_pin
        return True
    return False

  def set_pin(self, pin, new_pin):
    if (self.isClose):
      return False
    if (self.pin == pin):
      self.pin = new_pin
      return True
    else:
      return False

class Doorlock:
  def __init__(self, pin):
    self.pin = pin
    self.isOpen = True
     
  def lock(self):
    if self.isOpen:
      self.isOpen = False
      return True
    else:
      return False
     
  def unlock(self, pin):
    if not self.isOpen:
      if self.pin == pin:
        self.isOpen = True
        return True
    return False
     
  def set_pin(self,pin,new_pin):
    if not self.isOpen: return False
    if self.pin != pin: return False
    self.pin = new_pin
    return True

def main():
  print(duplicates([]))
  
main()