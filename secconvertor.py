duration = float(input("enter the time in milliseconds: "))
day=(duration // (24 * 3600) )  # 1hr =3600 sec DAY
duration=duration %(24 * 3600)     # ONe day 24 hour      
hour= duration //3600                                     #MINUTE
duration %=3600
minutes =  duration//60                        #minute
duration %= 60

week=(day%365)//7         #week

month=(week//4)




print("minute %d" % minutes)
print("hour %d" % hour)
print("day %d" % day)
print("week %d"% week)
print("month %d"% month)