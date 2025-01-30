secret_Word="Dog"
guess=""
guess_limit=3
outof_guess=False
count_guess=0
while guess!=secret_Word and not(outof_guess):
    if count_guess<guess_limit:
       guess=input("Enter your guess:")
       count_guess+=1
    else:
      outof_guess=True

if outof_guess:
    print("Out of guess.You Lose!")
else:
    print("You Win")

