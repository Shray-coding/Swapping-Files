def swapFileData():
    with open("sampleText1.txt",'r') as a:
        data_a= a.read()
    print(data_a)
    with open("sampleText2.txt",'r') as b:
        data_b=b.read()
    with open("sampleText1.txt",'w') as a:
        a.write(data_b)
    with open("sampleText2.txt",'w') as b:
        b.write(data_a)

swapFileData()