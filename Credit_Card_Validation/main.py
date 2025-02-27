#we are doing validation with LHUN algorithm
card_no = "5443019278471875"

numbers = list(card_no)
print(len(numbers))  #16

odd_sum = 0

for (index, value) in enumerate(numbers):    #reach index values of any giving list
    value = int(value)
    if index%2 == 1:
        odd_sum = odd_sum + value

even_sum = 0

for (index, value) in enumerate(numbers):
    value = int(value)
    if index % 2 == 0:
        new_value = value * 2
        if new_value >= 10:
            new_value = new_value // 10 + new_value % 10
        even_sum += new_value

print(even_sum)
print(odd_sum)

#If sum of even_sum and odd_sum mod 10 equal to 0 than it is valid

is_Valid = False

check_for_validation = (even_sum + odd_sum) % 10

if check_for_validation == 0:
    is_Valid = True
else:
    is_Valid = False

print(f"Is {card_no} card no valid: {is_Valid}")