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

# Chapter 4
# modify chap 2 & 3, check git log
print(film1[1] > film2[1])

# Chapter 6
f1 = ["Brazil", 1985, 7.5]
f2 = ["12 Monkeys", 1995, 8]
f3 = ["The Zero Theorem", 2013, 6.1]
f4 = ["Life of Brian", 1979, 9]

filmography = [f1, f2, f3, f4]
difference = filmography[0][2] - filmography[1][2]

if difference == 0:
    print("They're equally good")
elif difference < 0:
    print(filmography[1][0] + " is better")
else:
    print(filmography[1][0] + " isn't as good")
    
