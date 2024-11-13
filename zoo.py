class Zoo:
    def get_ticket_price(self, age):
        if age <= 0:
            return "Not available age"
        elif 0 < age <= 12 :
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 < age <= 60:
            return 150
        elif age >= 60:
            return 100
        
if __name__ == "__main__":
    zoo = Zoo()
    print(zoo.get_ticket_price(0))
    print(zoo.get_ticket_price(4))
    print(zoo.get_ticket_price(20))
    print(zoo.get_ticket_price(30))
    print(zoo.get_ticket_price(80))