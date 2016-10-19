
first_test = raw_input("Enter Sign To Convert: ")
sign_text = first_test.lower()
test_list = []
if len(sign_text) > 50:
    print "too long"
else:
    for items in sign_text:
        if items == items.isupper():
            test_list.append("000001000001")
        else:
            test_list.append(items)
for n,i in enumerate(test_list):
    if i == " ":
        test_list[n] = "000000"
    elif i == "a":
        test_list[n] = "100000"
    elif i == "b":
        test_list[n] = "110000"
    elif i == "c":
        test_list[n] = "100100"
    elif i == "d":
        test_list[n] = "100110"
    elif i == "e":
        test_list[n] = "100010"
    elif i == "f":
        test_list[n] = "110100"
    elif i == "g":
        test_list[n] = "110110"
    elif i =="h":
        test_list[n] = "110010"
    elif i == "i":
        test_list[n] = "010100"
    elif i == "j":
        test_list[n] = "010110"
    elif i =="k":
        test_list[n] = "101000"
    elif i == "l":
        test_list[n] = "111000"
    elif i =="m":
        test_list[n] = "101100"
    elif i =="n":
        test_list[n] = "101110"
    elif i == "o":
        test_list[n] = "101010"
    elif i =="p":
        test_list[n] = "111100"
    elif i =="q":
        test_list[n] = "111110"
    elif i =="r":
        test_list[n] = "111010"
    elif i =="s":
        test_list[n] = "011100"
    elif i =="t":
        test_list[n] = "011110"
    elif i =="u":
        test_list[n] = "101001"
    elif i =="v":
        test_list[n] = "111001"
    elif i == "w":
        test_list[n] = "010111"
    elif i == "x":
        test_list[n] = "101101"
    elif i == "y":
        test_list[n] = "101111"
    elif i == "z":
        test_list[n] = "101011"
final_answer =  "".join(test_list)

blank = "000001"
if first_test == sign_text.capitalize():
    print blank + final_answer
elif first_test == sign_text.upper():
    print blank + blank + final_answer
else:
    print final_answer
