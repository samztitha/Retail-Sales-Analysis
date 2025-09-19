# Part A – Python Basics

# 1. List of numbers: max, min, sum, avg
numbers = [20, 45, 23, 67, 90, 89, 5]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers)/len(numbers))

# 2. Word frequency counter
sentence = "Retail sales data analysis with Python and SQL"
word_freq = {}
for word in sentence.lower().split():
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word Frequencies:", word_freq)

# 3. Prime check function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))
