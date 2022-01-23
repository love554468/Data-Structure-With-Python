
def num2_to_text(num: str) ->str:
    pass
x = 1000
str_x = str(x)
l = len(str_x)
x0, x1, x2, x3 = [int(i) for i in str_x]

text = ""
if l == 4:
    if (x == 1000):
        print("Một ngàn")
    else:
        if x1 == 0:
            text = "Một ngàn không trăm" + num2_to_text(str_x[2:])    
        else:
            text = "Một ngàn" + num3_to_text(str_x[1:])
        print(text)
elif l==3:
    if (x==100):
        print("Một trăm")
    else:
        if x1 == 0:
            text = "Một trăm lẻ "+ num1_to_text(str_x[3])
        else:
            text = "Một trăm " + num2_to_text(str_x[1:])
            print(text)
elif l == 2:
    if (x == 10)
