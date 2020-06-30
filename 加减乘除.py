class Count:
    num1 = int(input("请输入数字1:"))
    num2 = int(input("请输入数字2:"))

    def add(self):
        add = self.num1 + self.num2
        return add

    def subtract(self):
        subtract = self.num1 - self.num2
        return subtract

    def product(self):
        product = self.num1 * self.num2
        return product

    def division(self):
        division = self.num1 / self.num2
        return division


count = Count()
print(f"加法结果：{count.add()}")
print(f"减法结果：{count.subtract()}")
print(f"除法结果：{count.division()}")
print(f"乘法结果：{count.product()}")
