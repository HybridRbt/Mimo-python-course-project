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

# Chapter 7
film1 = ["cyllos", 2016, 6.2]
film2 = ["12 Monkeys", 1995, 8]
film3 = ["zardos", 1974, 5.8]
film4 = ["life of brian", 1979, 9]
filmlist = [film1, film2, film3, film4]
for film in filmlist:
    if film[2] >= 9:
        print("Watch " + film[0])

# Chapter 9
film1 = ["Brazil", "Gilliam", 7.5]
film2 = ["Jaws", "Spielberg", 8]
film3 = ["Pi", "Aranovsky", 7.5]
film4 = ["Monty Python and the Holy Grail", "Gilliam", 8]

films = [film1, film2, film3, film4]
film_dict = {}
for i in range(len(films)):
    film_dict[films[i][0]] = films[i][1:3]
print(film_dict["Pi"])
