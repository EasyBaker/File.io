with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

count = 0
for w in words:
    if len(w) >= 1:
        count += 1
print(count)

five_long = 0
for w in words:
    if len(w) == 5:
        five_long += 1
print(five_long)

seven_long = 0
for w in words:
    if len(w) > 7:
        seven_long += 1
print(seven_long)
    
characters = 0
for w in words:
    this_one = len(w)
    characters += this_one
print(characters)

no_e = 0
yes_e = 0
for w in words:
    if "e" in w:
        yes_e += 1
no_e = count - yes_e
print(no_e)

begin_and_end = 0
for w in words:
    if w[0] == w[-1]:
        begin_and_end += 1
print(begin_and_end)

three_a = 0
for w in words:
    this_one = 0
    for l in w:
        if "a" == l:
            this_one += 1
    if this_one == 3:
        three_a += 1
print(three_a)

for w in words:
    this_word = 0
    for l in w:
        if "q" == l:
            if "u" == l:
                this_word += 1
        break
print(this_word)
            
        
        

