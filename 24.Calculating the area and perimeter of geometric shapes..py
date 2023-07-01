class Shape:
    """
    Father class.
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.perimeter = 0

    # مساحت
    def calculate_area(self):
        """
        Area calculation function.
        :return:
        """
        pass

    # محیط
    def calculate_perimeter(self):
        """
        Perimeter calculation function.
        :return:
        """
        pass

    def show(self):
        """
        Information display function.
        :return:
        """
        info = ""
        for key, value in self.__dict__.items():
            if value > 0:
                info += f"{key}: {value:.2f}\n"
        print(info)

    def __str__(self):
        return self.__class__.__name__


# مستطیل
class Rectangle(Shape):
    """
    Rectangle class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # مساحت: طول * عرض
    def calculate_area(self):
        """
        Override the area calculation function.
        :return:
        """
        self.area = self.length * self.width

    # محیط: مجموع 4 ظلع
    def calculate_perimeter(self):
        """
        Override the perimeter calculation function.
        :return:
        """
        self.perimeter = 2 * (self.length + self.width)


# مربع
class Square(Shape):
    """
    Square Class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # مساحت: یک ظلع * خودش
    def calculate_area(self):
        """
        Override the area calculation function.
        :return:
        """
        self.area = self.length ** 2

    # محیط: مجموع 4 ظلع
    def calculate_perimeter(self):
        """
        Override the perimeter calculation function.
        :return:
        """
        self.perimeter = self.length * 4


# مثلث
class Triangle(Shape):
    """
    Triangle class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # مساحت: (قاعده * ارتفاع) تقسیم بر 2
    def calculate_area(self):
        """
        Override the area calculation function.
        :return:
        """
        self.area = (self.base * self.height) / 2

    # محیط: مجموع 3 ظلع
    def calculate_perimeter(self):
        """
        Override the perimeter calculation function.
        :return:
        """
        self.perimeter = self.base + self.side1 + self.side2


# لوزی
class Rhombus(Shape):
    """
    Rhombus class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # مساحت: (قطر بزرگ * قطر کوچک) تقسیم بر 2
    def calculate_area(self):
        """
        Override the area calculation function.
        :return:
        """
        self.area = (self.diameter1 * self.diameter2) / 2

    # محیط: مجموع 4 ظلع
    def calculate_perimeter(self):
        """
        Override the perimeter calculation function.
        :return:
        """
        self.perimeter = self.length * 4


# متوازی الاظلاع
class Parallelogram(Shape):
    """
    Parallelogram class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # مساحت: قاعده * ارتفاع
    def calculate_area(self):
        """
        Override the area calculation function.
        :return:
        """
        self.area = self.length * self.height

    # محیط: مجموع 4 ظلع
    def calculate_perimeter(self):
        """
        Override the perimeter calculation function.
        :return:
        """
        self.perimeter = (self.length + self.width) * 2


# ذوزنقه
class Trapezium(Shape):
    """
    Trapezium class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # مساحت: (قاعده بزرگ + قاعده کوچک) * ارتفاع, تقسیم بر 2
    def calculate_area(self):
        """
        Override the area calculation function.
        :return:
        """
        self.area = 1/2 * self.height * (self.top + self.base)

    # محیط: مجموع 4 ظلع
    def calculate_perimeter(self):
        """
        Override the perimeter calculation function.
        :return:
        """
        self.perimeter = self.top + self.base + self.side1 + self.side2


# دایره
class Circle(Shape):
    """
    Circle class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # مساحت: 3.14 * شعاع * شعاع
    def calculate_area(self):
        """
        Override the area calculation function.
        :return:
        """
        self.area = self.radius ** 2 * 3.14

    # محیط: 3.14 * قطر
    def calculate_perimeter(self):
        """
        Override the perimeter calculation function.
        :return:
        """
        self.perimeter = 2 * self.radius * 3.14


while True:
    li = []

    print("Choose the shape you want:\n1 = Rectangle\n2 = Square\n3 = Triangle"
          "\n4 = Rhombus\n5 = Parallelogram\n6 = Trapezium\n7 = Circle\n8 = EXIT")

    ipt = float(input("\tEnter: "))

    if ipt == 1:
        print("\n", "-" * 40, "\nRectangle")
        length = float(input("Enter the value of length: "))
        width = float(input("Enter the value of width: "))
        print("\n", "-" * 40)

        li.append(length)
        li.append(width)

        r = Rectangle(length=li[0], width=li[1])
        r.calculate_area()
        r.calculate_perimeter()
        print(r)
        r.show()
        print("-" * 40)

    elif ipt == 2:
        print("\n", "-" * 40, "\nSquare")
        length = float(input("Enter the value of length: "))
        print("\n", "-" * 40)

        li.append(length)

        s = Square(length=li[0])
        s.calculate_area()
        s.calculate_perimeter()
        print(s)
        s.show()
        print("-" * 40)

    elif ipt == 3:
        print("\n", "-" * 40, "\nTriangle")
        base = float(input("Enter the value of base: "))
        height = float(input("Enter the value of height: "))
        side1 = float(input("Enter the value of side1: "))
        side2 = float(input("Enter the value of side2: "))
        print("\n", "-" * 40)

        li.append(base)
        li.append(height)
        li.append(side1)
        li.append(side2)

        t = Triangle(base=li[0], height=li[1], side1=li[2], side2=li[3])
        t.calculate_area()
        t.calculate_perimeter()
        print(t)
        t.show()
        print("-" * 40)

    elif ipt == 4:
        print("\n", "-" * 40, "\nRhombus")
        diameter1 = float(input("Enter the value of diameter1: "))
        diameter2 = float(input("Enter the value of diameter2: "))
        length = float(input("Enter the value of length: "))
        print("\n", "-" * 40)

        li.append(diameter1)
        li.append(diameter2)
        li.append(length)

        m = Rhombus(diameter1=li[0], diameter2=li[1], length=li[2])
        m.calculate_area()
        m.calculate_perimeter()
        print(m)
        m.show()
        print("-" * 40)

    elif ipt == 5:
        print("\n", "-" * 40, "\nParallelogram")
        length = float(input("Enter the value of length: "))
        height = float(input("Enter the value of height: "))
        width = float(input("Enter the value of width: "))
        print("\n", "-" * 40)

        li.append(length)
        li.append(height)
        li.append(width)

        p = Parallelogram(length=li[0], height=li[1], width=li[2])
        p.calculate_area()
        p.calculate_perimeter()
        print(p)
        p.show()
        print("-" * 40)

    elif ipt == 6:
        print("\n", "-" * 40, "\nTrapezium")
        height = float(input("Enter the value of height: "))
        base = float(input("Enter the value of base: "))
        top = float(input("Enter the value of top: "))
        side1 = float(input("Enter the value of side1: "))
        side2 = float(input("Enter the value of side2: "))
        print("\n", "-" * 40)

        li.append(height)
        li.append(base)
        li.append(top)
        li.append(side1)
        li.append(side2)

        z = Trapezium(height=li[0], base=li[1], top=li[2], side1=li[3], side2=li[4])
        z.calculate_area()
        z.calculate_perimeter()
        print(z)
        z.show()
        print("-" * 40)

    elif ipt == 7:
        print("\n", "-" * 40, "\nCircle")
        radius = float(input("Enter the value of radius: "))
        print("\n", "-" * 40)

        li.append(radius)

        c = Circle(radius=li[0])
        c.calculate_area()
        c.calculate_perimeter()
        print(c)
        c.show()
        print("-" * 40)

    elif ipt == 8:
        print("\n", "-" * 17, "END!", "-" * 17)
        break

    else:
        print("\n", "-" * 40, "\nWrong value!\nPlease try again...", "\n\n", "-" * 40)
