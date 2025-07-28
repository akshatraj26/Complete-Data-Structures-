"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
 People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or
 they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to maintain this system
and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
"""

class  Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class AnimalShelter:
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()


    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next

    def __str__(self):
        dogs = [str(dog.value) for dog in self.dogs]
        cats = [str(cat.value) for cat in self.cats]


    def enqueue(self, animal, type):
        new_animal = Node(value=animal)
        if type == "Cat":
            if self.cats.head is None:
                self.cats.head = new_animal
                self.cats.tail = new_animal
            else:
                new_animal.next = None
                self.cats.tail.next = new_animal
                self.cats.tail = new_animal
                return f"Now we have a new {type} in our animal shelter."
        else:
            if self.dogs.head is None:
                self.dogs.head = new_animal
                self.dogs.tail = new_animal
            else:
                new_animal.next = None
                self.dogs.tail.next = new_animal
                self.dogs.tail = new_animal

    def dequeue_cat(self):
        if self.cats.head is None:
            return "There is no cat in the animal shelter."
        else:
            adopted = self.cats.head.value
            self.cats.head = self.cats.head.next
            return adopted

    def dequeue_dog(self):
        if self.dogs.head is None:
            return "There is no dog in the animal shelter."
        else:
            adopted = self.dogs.head.value
            self.dogs.head = self.dogs.head.next
            return adopted

    def dequeue_any(self):
        if self.cats.head is None:
            adopted = self.dequeue_dog()
            return adopted
        else:
            adopted = self.dequeue_cat()
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


