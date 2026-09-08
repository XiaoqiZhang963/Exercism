class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        digits = ''.join(self.card_num.split())

        if len(digits) <= 1:
            return False
        
        if not digits.isdigit():
            return False
            
        numbers = [int(digit) for digit in reversed(digits)]
       
        for index, value in enumerate(numbers):
            if index%2 > 0:
                value *= 2
                if value > 9:
                    value -= 9
                numbers[index] = value

        return sum(numbers)%10 == 0
                
