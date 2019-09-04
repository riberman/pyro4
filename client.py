import Pyro4

flag = True
uri = input("URI Object? ").strip()
while(flag):
    tag = Pyro4.Proxy(uri)
    print(tag.get_tag())
    inputTxt = raw_input("Generate new?  Y/N \n")
    if(inputTxt == "y" or inputTxt == "Y"):
        flag = True
    else:
        if(inputTxt == "n" or inputTxt == "N"):
            flag = False
        else:
            print("No command!")
