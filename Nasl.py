

print('-----------------')


class Grandma:
    def about(self):
        print('I am Grandma')

    def about_myself(self):
        print('Actually, I am grandparent')


class Mother(Grandma):
    def about_myself(self):
        print('Really, I am mother')


class Child(Mother):
    def __init__(self):
        super().about()
        super().about_myself()


nick = Child()

print('-----------------')

