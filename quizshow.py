Q = {
    1: "What is colour of banana?  \nA) Blue\nB) Orange\nC) Yellow",
    2: "What is colour of orange?  \nA) Blue\nB) Orange\nC) Yellow",
    3: "What is colour of banana?  \nA) Blue\nB) Orange\nC) Yellow",
    4: "What is colour of orange?  \nA) Blue\nB) Orange\nC) Yellow",
    5: "What is colour of banana?  \nA) Blue\nB) Orange\nC) Yellow"

}

A = {
    1: "C",
    2: "B",
    3: "C",
    4: "B",
    5: "C",
}

correct_number = 0
for number in Q:
    print(Q[number])

    answer = str(input("Your choice is (A-B-C): "))
    if A[number] == answer.upper():
        print("Correct!!!")
        correct_number += 1
    else:
        print(f"Wrong!!! Answer is {A[number]}")

print(f"Your count of correct answer: {correct_number}")
