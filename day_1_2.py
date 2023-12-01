"""--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?"""

digit_names = {
    "one": "1", 
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8", 
    "nine": "9"}

def get_callibration_value(line: str) -> int: 
    nums = []
    for i, char in enumerate(line): 
        if char.isnumeric(): 
            nums.append(char)
        else: 
            substring = line[i:]
            found_digit_name = next((w for w in digit_names.keys() if substring.startswith(w)), None)
            if found_digit_name: 
                nums.append(digit_names[found_digit_name])

    first_num, last_num = nums[0], nums[-1]
    return int(first_num + last_num) 


if __name__ == "__main__": 
    with open("callibration_lines.txt", mode="r", encoding="utf-8") as file: 
        lines = file.readlines()
        callibration_values = [get_callibration_value(line) for line in lines]
        print(sum(callibration_values))