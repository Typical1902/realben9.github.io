calctype = input("Which type of calculation will you use? (1 : Generic, 2 : Circle, 3 : Binary, DEFAULT : Generic) : ")
if calctype == "2":
  pi = 3.1415926535897932384626
  operation=input("What value of the circle do you know? (1 : Radius, 2 : Area, 3 : Circumference, 4 : Diameter, 5 : Surface Area, DEFAULT : Radius) : ")
  if operation=="2":
    area = float(input("Enter the circle area : "))
    radius = (area / pi) ** 0.5
    circumference = 2 * pi * radius
    diameter = 2 * radius
    surfacearea = 4 * pi * radius * radius
    print("The circle radius is", radius, "!")
    print("The circle circumference is", circumference, "!")
    print("The circle diameter is", diameter, "!")
    print("The circle surface area is", surfacearea, "!")
  elif operation=="3":
    circumference = float(input("Enter the circle circumference : "))
    radius = circumference / pi / 2
    area = (pi * radius) * radius
    diameter = 2 * radius
    surfacearea = 4 * pi * radius * radius
    print("The circle radius is", radius, "!")
    print("The circle area is", area, "!")
    print("The circle diameter is", diameter, "!")
    print("The circle surface area is", surfacearea, "!")
  elif operation=="4":
    diameter  = float(input("Enter the circle diameter : "))
    radius = diameter / 2
    area = (pi * radius) * radius
    circumference = pi * diameter
    surfacearea = 4 * pi * radius * radius
    print("The circle radius is", radius, "!")
    print("The circle area is", area, "!")
    print("The circle circumference is", circumference, "!")
    print("The circle surface area is", surfacearea, "!")
  elif operation=="5":
    surfacearea = float(input("Enter the circle surface area : "))
    radius = (surfacearea / 4 / pi) ** 0.5
    circumference = 2 * pi * radius
    diameter = 2 * radius
    surfacearea = 4 * pi * radius * radius
    print("The circle radius is", radius, "!")
    print("The circle circumference is", circumference, "!")
    print("The circle diameter is", diameter, "!")
    print("The circle area is", area, "!")
  else:
    radius = float(input("Enter the circle radius : "))
    area = pi * radius * radius
    circumference = 2 * pi * radius
    diameter = 2 * radius
    surfacearea = 4 * pi * radius * radius
    print("The circle area is", area, "!")
    print("The circle circumference is", circumference, "!")
    print("The circle diameter is", diameter, "!")
    print("The circle surface area is", surfacearea, "!")
  arccalc=input("Do you know the arc angle/length? (0 : No, 1 : Angle, 2 : Length, DEFAULT : No) : ")
  if arccalc=="1":
    arcangle  = input("Enter the circle arc angle : ")
    arclength = float(arcangle) * pi / 180 * radius
    print("The circle arc length is", arclength, "!")
  elif arccalc=="2":
    arclength  = input("Enter the circle arc length : ")
    arcangle = float(arclength) * 180 / pi / radius
    print("The circle arc angle is", arcangle, "!")
elif calctype == "3":
  operation = input("What operation will you use? (1 : Conversion, 2 : Operation, DEFAULT : Conversion) : ")
  if operation == "2":
    print("Operation")
  else:
    format = input("What format is this number? (1 : Decimal, 2 : Binary, 3 : Hexadecimal, DEFAULT : Decimal) : ")
    if format == "2":
      print("Binary")
    elif format == "3":
      print("Hexadecimal")
    else:
      decnum = int(input("Enter a decimal integer : "))
      dec2hex1div = decnum // 16
      dec2hex1mod = decnum % 16
      dec2hex2div = dec2hex1div // 16
      dec2hex2mod = dec2hex1div % 16
      if dec2hex1mod == 10:
        dec2hex1mod = "A"
      elif dec2hex1mod == 11:
        dec2hex1mod = "B"
      elif dec2hex1mod == 12:
        dec2hex1mod = "C"
      elif dec2hex1mod == 13:
        dec2hex1mod = "D"
      elif dec2hex1mod == 14:
        dec2hex1mod = "E"
      elif dec2hex1mod == 15:
        dec2hex1mod = "F"
      if dec2hex2mod == 10:
        dec2hex2mod = "A"
      elif dec2hex2mod == 11:
        dec2hex2mod = "B"
      elif dec2hex2mod == 12:
        dec2hex2mod = "C"
      elif dec2hex2mod == 13:
        dec2hex2mod = "D"
      elif dec2hex2mod == 14:
        dec2hex2mod = "E"
      elif dec2hex2mod == 15:
        dec2hex2mod = "F"
      hexnum = str(dec2hex2mod) + str(dec2hex1mod)
      dec2bin1div = decnum // 2
      dec2bin1mod = decnum % 2
      dec2bin2div = dec2bin1div // 2
      dec2bin2mod = dec2bin1div % 2
      dec2bin3div = dec2bin2div // 2
      dec2bin3mod = dec2bin2div % 2
      dec2bin4div = dec2bin3div // 2
      dec2bin4mod = dec2bin3div % 2
      dec2bin5div = dec2bin4div // 2
      dec2bin5mod = dec2bin4div % 2
      dec2bin6div = dec2bin5div // 2
      dec2bin6mod = dec2bin5div % 2
      dec2bin7div = dec2bin6div // 2
      dec2bin7mod = dec2bin6div % 2
      dec2bin8div = dec2bin7div // 2
      dec2bin8mod = dec2bin7div % 2
      decnummod = decnum % 256
      print("Decimal :", decnum)
      print("Decimal (Overflow) :", decnummod)
      print("Hexadecimal :", hexnum)
      print("Binary : " + str(dec2bin8mod) + str(dec2bin7mod) + str(dec2bin6mod) + str(dec2bin5mod) + str(dec2bin4mod) + str(dec2bin3mod) + str(dec2bin2mod) + str(dec2bin1mod))
else:
  operation=input("What operation will you use? (1 : [+], 2 : [-], 3 : [*], 4 : [/], 5 : Exponent [**], DEFAULT : [+]) : ")
  if operation=="2":
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))
    answer=num1-num2
    print("The answer is", answer, "!")
  elif operation=="3":
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))
    answer=num1*num2
    print("The answer is", answer, "!")
  elif operation=="4":
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))
    answer=num1/num2
    answerdiv=num1//num2
    answermod=num1%num2
    print("The answer is", answer, "(", answerdiv, "r", answermod, ")!")
  elif operation=="5":
    num1=float(input("Enter a number : "))
    num2=float(input("Enter the power to give that number : "))
    answer=num1**num2
    print("The answer is", answer, "!")
  else:
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))
    answer=num1+num2
    print("The answer is", answer, "!")
