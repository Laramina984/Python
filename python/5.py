class Circle:   
    def int (self, center, radius):
        self.center = center
        self.radius = radius
class point:
    def int (self,n1,n2):
        self.n1 = n1
        self.n2 = n2

def point_in_circle(circle, point):
    dist_squared = (point.n1 - circle.center.n1) ** 2 + (point.n2 - circle.center.n2) ** 2
    return dist_squared <= circle.radius ** 2

center_point = point(150,100)
circle = Circle(center_point,75)



   