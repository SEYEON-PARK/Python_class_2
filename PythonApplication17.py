class Cat:
    def __init__(self, name, age):
        self.Name=name
        self.Age=age
    def __str__(self):
        return '(%s, %d)' %(self.Name, self.Age) #고양이 클래스 만들기

#프로그램 시작

missy=Cat('Missy', 3)
lucky=Cat("Lucky", 5)
print(missy)
print(lucky)