"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
 People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or
 they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to maintain this system
and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
"""

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'Dog':
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return "Sorry we don't have any cats."
        else:
            adopted = self.cats.pop(0)
            return adopted

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return "Sorry we don't have any dogs."
        else:
            adopted = self.dogs.pop(0)
            return adopted

    def dequeue_any(self):
        if len(self.cats) == 0:
            adopted = self.dogs.pop()
        else:
            adopted = self.cats.pop()
        return adopted

animal = AnimalShelter()
animal.enqueue("Cat1", 'Cat')
animal.enqueue("Cat2", 'Cat')
animal.enqueue("Dog1", 'Dog')
animal.enqueue("Cat3", 'Cat')
animal.enqueue("Cat4", 'Cat')
animal.enqueue("Dog2", 'Dog')
print(animal.enqueue("Cat5", 'Cat'))

print("_"*100)
print(animal.dequeue_cat())
print(animal.dequeue_dog())

print(animal.dequeue_any())