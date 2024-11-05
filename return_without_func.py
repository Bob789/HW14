#solution 1.a
def ascending_my(a: int, b: int) -> None:
    if a < b:
        print(a," ",b)
    else:
        print(b," ",a)


ascending_my(99, -2)

#solution 1.b
print(" solution b")
def details_my(word: str) -> None:
    a = len(word) // 2
    print(f" {word[0:1]} {word[a-1:a]} {word[-1]}")

details_my("AI is the best")

#solution 1.c
print(" solution c")
def bool_say(bo: bool) -> None:
    if(bo):
        print(True)
    else:
        print(False)

bool_say(True)
bool_say(False)

#solution 1.d
print(" solution d")
def zugi_print(list_even_odd: list[int]) -> None:
    for even in list_even_odd:
        if 0 == even % 2:
            print(f" {even} is even ")
        else:
            print(f" {even} is odd ")

zugi_print([5, 3, 2, 10, 15, 14, 14])

#solution 1.e
print(" solution e")
def statistics_my(list_score: list[int]) -> None:
    print(f" max: {max(list_score)}")
    print(f" min: {min(list_score)}")
    print(f" count score: {len(list_score)}")
    print(f" average: {sum(list_score) / len(list_score)}")

statistics_my([87, 100, 55, 76, 88, 92 ,66])

SENTINEL = int(-99)
list_grade = []
while True:
    input_grade = int(input("Enter score, -99 to exit : "))
    if SENTINEL == input_grade:
        break
    else:
        if 0 > input_grade > 100:
            continue
        else:
            list_grade.append(input_grade)

statistics_my(list_grade)

