
def ReversePolishEvel(arr):
	if len(arr) == 1:
		return arr[0]

	stack = [arr[0], arr[1]];
	for i in xrange(2, len(arr)):
		if arr[i] == "+":
			b = int(stack.pop())
			a = int(stack.pop())
			stack.append(a + b)
		elif arr[i] == "-":
			b = int(stack.pop())
			a = int(stack.pop())
			stack.append(a - b)
		elif arr[i] == "/":
			b = int(stack.pop())
			a = int(stack.pop())
			stack.append(a / b)
		elif arr[i] == "*":
			b = int(stack.pop())
			a = int(stack.pop())
			stack.append(a * b)
		else:
			stack.append(arr[i])
	return stack[0]

print ReversePolishEvel([4, "13", "5", "/", "+"])