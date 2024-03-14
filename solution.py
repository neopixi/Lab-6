class Building:
    def __init__(self, area, cost_per_square_meter, number_of_residents):
        self.area = area
        self.cost_per_square_meter = cost_per_square_meter
        self.number_of_residents = number_of_residents
    
    def total_cost(self):
        return self.area * self.cost_per_square_meter
    
    def cost_to_residents_ratio(self):
        return self.total_cost() / self.number_of_residents

class CountryBuilding(Building):
    def __init__(self, area, cost_per_square_meter, number_of_residents, has_cow):
        super().__init__(area, cost_per_square_meter, number_of_residents)
        self.cow = has_cow
    
    def cow_status(self):
        return "Has cow :)" if self.cow else "No cow :("

class CityBuilding(Building):
    def __init__(self, area, cost_per_square_meter, number_of_residents, number_of_floors):
        super().__init__(area, cost_per_square_meter, number_of_residents)
        self.number_of_floors = number_of_floors
    
    def average_residents_per_floor(self):
        return self.number_of_residents / self.number_of_floors

building = Building(100, 1200, 50)
country_building = CountryBuilding(200, 1000, 40, True)
city_building = CityBuilding(500, 1500, 200, 10)

print(building.total_cost())
print(building.cost_to_residents_ratio())
print(country_building.cow_status())
print(city_building.average_residents_per_floor())
print(city_building.total_cost())
print(city_building.cost_to_residents_ratio())
print(country_building.total_cost())
print(country_building.cost_to_residents_ratio())