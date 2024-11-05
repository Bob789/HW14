#2.a
from pickletools import long1

print(" solution a: ")
def avg_my(num1: int, num2: int) -> float:

    return (num1+num2)/2

avg1 = avg_my(90, 99)
print(avg1)

#2.b
print()
print(" solution b: ")
def my_headline(word: str) -> str:

    return word.upper()+"!"

headline = str("python has concurred the world")
head1 = my_headline(headline)
print(head1)
print(head1)

#2.c
print()
print(" solution c: ")
def concat_list(list1: [int], list2: [int], list3: [int]) -> list [int]:
    ''' Create one list from tree !!!! '''
    return list1 + list2 + list3

l1 = [1, 2]
l2 = [3, 4, 5, 6]
l3 = [7, 8, 9]
res_con = concat_list(l1, l2, l3)
print(f" the full list : {res_con}")
print(f" the length: {len(res_con)}")