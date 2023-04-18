class Myclass:
    '''A simple class'''
    name = 'other name'
    age = 23
def main():
    '''This is a simple main function'''
    me = Myclass()
    me.name = 'Muktadir Ahmed'
    me.age = 26
    print(f"name: {me.name}\nage: {me.age}")
if __name__ =="__main___":
    main()
main() 
print(main.__doc__)     