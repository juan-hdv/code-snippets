def calPoints(ops) -> int:
        """
        :type ops: List[str] - List of operations
        :rtype: int - Sum of scores after performing all operations
        """
        result = None
        numbers = []
        k = -1
        for op in ops:
                if op.isnumeric():
                        numbers.append(int(op))
                        k += 1
                elif op == "+":
                        numbers.append(numbers[k]+numbers[k-1])
                        k += 1
                elif op == "D":
                        numbers.append(numbers[k]*2)
                        k += 1
                elif op == "C":
                        numbers = numbers[:-1]
                        k -= 1
        result = sum(numbers)
        return result

if __name__ == '__main__':
        line = input()
        ops = line.strip().split()

        print(calPoints(ops))
