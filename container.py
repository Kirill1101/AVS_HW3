class Container:
    def __init__(self):
        self.store = []


    def Write(self, ostream):
        ostream.write("Container contains {} elements.\n".format(len(self.store)))
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        pass

    def Shift(self):
        sum = 0
        for plant in self.store:
            sum += plant.Quotient()
        average = sum / len(self.store)

        k = len(self.store)
        new_store = []
        index = 0
        for plant in self.store:
            num = plant.Quotient()
            if (num > average):
                new_store.append(plant)
        for plant in new_store:
            self.store.remove(plant)
            self.store.append(plant)

        return average
