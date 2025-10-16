def main():

    # Time
    print("Enter the time" , end = ": ")
    time = str(input())
    # Input validation for time
    while((len(time) < 4 or len(time) > 5)
          or not(time[0] in "1234567890")
          or not(time[1] in "1234567890:")
          or not(time[2] in ":")
          or not(time[-2] in "1234567890")
          or not(time[-1] in "1234567890")):
        print("Invalid time entered, please enter again" , end = ": ")
        time = str(input())
    

    # Clock type
    print("Choose the clock type: " , end = ": " )
    type = str(input())

    # Input validation for clock type
    while(len(type) != 2
          or not(type[0].isdigit)
          or not(type[1].isdigit)
          or int(type) != 12
          or int(type) != 24):
        print("Invalid clock type entered, please enter again" , end = ": ")
        type = str(input())


    # Character type
    print("Enter your preferred character" , end = ": ")
    character = str(input())

    # Input validation for clock type
    while(len(character) != 1
          or not(character[0] in "abcdeghkmnopqrsuvwxyz@$&*=")):
        print("Character not permitted! Try again" , end = ": ")
        character = str(input())


if __name__ == "__main__":
    main()