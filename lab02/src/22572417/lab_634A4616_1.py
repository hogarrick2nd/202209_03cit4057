def answer(value):
    ret = ""
    # START: 
    if ( value != 10  ) :
        ret = ("The number is not 10")
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    value = float(input("Enter a number: "))
    print( answer(value) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!