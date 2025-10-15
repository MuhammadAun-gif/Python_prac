class Salesperson:

    def __init__(self, name, sales, profit, ad):
        self.name = name
        self.sales = sales
        self.profit = profit
        self.ad = ad

    def __str__(self):
        return "Name: {}, Sales: {}, Profit: {}, Ad: {}".format(self.name, self.sales, self.profit, self.ad)
    
S_p1 = Salesperson("Rajeev", 6000, 2000, 1000)

print(S_p1)


S_p2 = Salesperson("haider", 7000, 3000, 500)

print(S_p2)