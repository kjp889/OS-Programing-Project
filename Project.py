# Names:  Danielle Hemmings, 
#         Tyandra Taylor, 
#         Chadwick Hewitt, 
#         Stephan Scott, 
#         Kyle Parris (1804904)
#OS Programming Project

import datetime

class Customer:
  def __init__(cus, cusNum, arrivalTime, entryTime, shoppingTime, waitTime, exitTime):
    cus.cusNum = cusNum
    cus.arrivalTime = arrivalTime
    cus.entryTime = entryTime
    cus.shoppingTime = shoppingTime
    cus.waitTime = waitTime
    cus.exitTime = exitTime
    
  def __str__(cus):
    return f"{cus.cusNum} - {cus.arrivalTime} - {cus.entryTime} - {cus.shoppingTime} - {cus.waitTime} - {cus.exitTime}"
  
#cus1 = Customer(1, 2, 3, 4)
#print(cus1)

inLine = []
outLine = []
doorIn = []
doorOut = []


