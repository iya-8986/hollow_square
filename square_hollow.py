#author_uy_thea
#date_october_3_2024
#section_bscpe_2-2

#create a function that will get the lenght of the square from the user
def get_length():
    while True:
        try:
            length = int(input(">> "))
        except:
            continue
        else:
            return length


print("Enter the side length of the square")
length = get_length()

#create the square layout
for i in range(length):
    for j in range(length):
        if i == 0 or i == (length-1) or j == 0 or j == (length-1):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    
    print()

#end of the program