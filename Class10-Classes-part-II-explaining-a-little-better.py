class Iphone: '''All iphones are different objects.
Your iphone is a different object. Mine is different one.
But all of them belong to iphone class.
All of them are iphones. Right? You get it. 
That's what class names are. '''


'''Now we will create its blueprint, 
suppose our Iphone class will have objects
having a camera, a color and screen.'''


def __init__(self, camera, color, screen):
    self.camera = camera
    self.color = color
    self.screen = screen
    '''init function is our blueprint. 
    Now, we have defined properties here.
    but what is self? Well, valid doubt.
    Now think of it, why do we create this blueprint?
    So that we can use it to create as many objects 
    of this class as we want. Right? 
    Suppose we use this blueprint of iphone class to create 
    your iphone object, then self is the object we create 
    at that time. The current object. So, your phone is 
    self. and self has these properties of blueprint. 

    Now, when my iphone is created using this blueprint, 
    self is the my phone and it has all the properties described.

    people often get confused, 
    why do we write self.camera = camera.
    Well, now that you know that self is 
    the iphone object being created using 
    blueprint. read it as this. Self.camera means 
    self will have a camera property which will be 
    equal to the value we assign to it 
    using this blueprint at the time of creation. similary, other properties work.  
    '''


'''Now that we have prepared our blueprint, let's create an iphone
YourPhone = Iphone ("30MP", "black", "6 inches")

wow, we have created our first object using this blueprint. 
Read it as this. We are creating a YourPhone object, 
which is an object of iphone class that means
it will have properties defined in the class blueprint.
at the time of creation, we can assign any value to 
properties. Like if we want, we can give it 23MP to camera or 40MP or 30MP.
set its color to any of our choice. We can set screen size to anything. '''

'''suppose we decide to manufacture humans. 


Class Human:

Now we will have to create a blueprint. 
def__init__(self, head, hands, legs, eyes, nose, etc):
    self.head = head
    self.hands = hands
    self.legs = legs
    self.eyes = eyes
    self.nose = nose
    self.etc = etc (all properties you can think of)

    "self" is the object we create using this blueprint.

    Now, see objects don't just have properties. They have behaviours too. 
    Think of behaviours as methods or function. 

    humans eat? right. 
    so, we declare a eat property
    def eat:
        print("nom nom nom eatin....")

    def walk():
        print("tak taka tak.. walking")

    similary we can define all behaviours like that.


Now that our blueprint is ready. 
We can simply create as many object as we want. 


Chandan = Human("smallest", "only 2", "2 is enough", "blind", "very big")


wow, we have manufactured a human named Chandan who has these properties.
here self is chandan. rest all properties has been given. 
This chandan will have the behaviours(methods/function) we have defined 
in Human class. '''

# I have written it in like 3-4 mins. Don't judge it like literature.
