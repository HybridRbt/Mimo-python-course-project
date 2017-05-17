# Mimo python course project
# Chapter 1
# This is my filmography project
film1 = "12 Monkeys"
film2 = "Brazil"
film3 = "Zero Theorem"
print(film1)
print(film2)
print(film3)

# Chapter 2
film1 = ("12 Monkeys", 8.1, True)
film2 = ("Brazil", 8.0, False)
film3 = ("Zero Theorem", 6.1, True)
print(film1[0] + " has " + str(film1[1]) + " points")

# Chapter 3
film4 = ('''Monty Python\'s \
Life of Brian''', 7.2, True)
summary = film4[0] + \
":\nBrian is mistaken for Jesus"
print(summary)

q = 'What\'s the air speed \
velocity of an unladen swallow?'
word = q[-8:-1]
q = q.replace(word, "rabbit")
print(q)

# Chapeter 4
# modify chap 2 & 3, check git log
print(film1[1] > film2[1])
