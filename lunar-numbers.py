class LunarNumber:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, LunarNumber):
            self_str = str(self.value)
            other_str = str(other.value)
            max_digits = max(len(self_str), len(other_str))

            if max_digits == 1:
                return LunarNumber(max(self.value, other.value))
            else:
                self_str = self_str.rjust(max_digits, '0')
                other_str = other_str.rjust(max_digits, '0')

                column_answers = []

                for i in range(max_digits):
                    column_answers.append(str(max(int(self_str[i]), int(other_str[i]))))

                return LunarNumber(int(''.join(column_answers)))

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, LunarNumber):
            self_str = str(self.value)
            other_str = str(other.value)
            max_digits = max(len(self_str), len(other_str))

            if max_digits == 1:
                return LunarNumber(min(self.value, other.value))
            else:
                self_str = self_str.rjust(max_digits, '0')
                other_str = other_str.rjust(max_digits, '0')

                answer_rows = []

                for i in reversed(range(len(other_str))):
                    column_answers = []

                    for j in range(len(self_str)):
                        column_answers.append(str(min(int(self_str[j]), int(other_str[i]))))
                    
                    column_answer_str = ''.join(column_answers)
                    answer_rows.append(column_answer_str.ljust(len(column_answer_str) + (len(column_answer_str) - i - 1), '0'))
                
                answer_numbers = map(lambda x: LunarNumber(int(x)), answer_rows)

                return sum(answer_numbers, start=LunarNumber(0))

        return NotImplemented

l1 = LunarNumber(159)
l2 = LunarNumber(842)

print(f'15 + 23 = {(l1 + l2).value}')
print(f'5 * 8 = {(l1 * l2).value}')