# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

i = 0

while i < len(myF) :
    print(f"#{str(i +1).zfill(2)}: {myF[i]}")
    i += 1

else : print("The list is done !")