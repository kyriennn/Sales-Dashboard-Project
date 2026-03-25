import random

def generate_target():
    return (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
                        #    generating random number function
numtarget = generate_target()

while True:
    try:
        numguess = input("Enter a 4 digit number: ")
        if len(numguess) != 4 or not numguess.isdigit():     # check if input is 4 digits and all numbers
            print("Invalid input, try again.")
            continue

        digitsguess = [int(i) for i in str(numguess)]    # replace each digit in input into a list of integers

        A = 0   # correct digit and correct position
        B = 0   # correct digit but wrong position

        matched_target = [False] * 4     # in A or B
        matched_guess = [False] * 4         # in A only

        for i in range(4):
            if digitsguess[i] == numtarget[i]:      # if same position and same digit
                A += 1
                matched_guess[i] = True
                matched_target[i] = True

        for i in range(4):
            if not matched_guess[i]:   # if not same position
                for j in range(4):
                    if not matched_target[j] and digitsguess[i] == numtarget[j]:  #if not same position but digit is in number
                        B += 1                                     # aka if not False and digitsguess[i] == numtarget[j] aka if True and digitsguess[i] == numtarget[j]
                        matched_guess[i] = True
                        matched_target[j] = True
                        break                                     # break to avoid double counting
            
        print(f"{A}A{B}B")
                
        if A == 4:                     # if all 4 digits are correct
            print("You win!")
            break
        else:
            continue
        
        

    except ValueError:
        print("Invalid input, try again.")
        continue
    except IndexError:
        print("Invalid input, try again")
        continue
