# map(fun,data)


# this program shuffles the words that are sent to it
from random import shuffle
def jumble(word):
    changer=list(word)
    shuffle(changer)
    return '-'.join(changer)


words=['lohit', 'Takuma', 'Endo']
 
 
changer=[]

for word in words:
    changer.append(jumble(word))

print(changer)


# using the map fucntion
# map(funtion,data)
print(list(map(jumble,words)))

# using comprehsions we can do

changer = [jumble(word) for word in words]

print(changer)
