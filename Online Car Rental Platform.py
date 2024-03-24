from datetime import datetime

class CarRental:
    def __init__(self, available_cars):
        self.available_cars = available_cars
        self.rental_records = {}

    def display_available_cars(self):
        print("Available cars:")
        for car, quantity in self.available_cars.items():
            print(f"{car}: {quantity}")

    def rent_car_hourly(self, car, num_cars):
        if car in self.available_cars and num_cars > 0 and num_cars <= self.available_cars[car]:
            current_time = datetime.now()
            self.rental_records[car] = {'num_cars': num_cars, 'time': current_time, 'rate': 10}
            self.available_cars[car] -= num_cars
            print(f"{num_cars} {car} car(s) rented hourly at {current_time}")
        else:
            print("Invalid request")

    def rent_car_daily(self, car, num_cars):
        if car in self.available_cars and num_cars > 0 and num_cars <= self.available_cars[car]:
            current_time = datetime.now()
            self.rental_records[car] = {'num_cars': num_cars, 'time': current_time, 'rate': 50}
            self.available_cars[car] -= num_cars
            print(f"{num_cars} {car} car(s) rented daily at {current_time}")
        else:
            print("Invalid request")

    def rent_car_weekly(self, car, num_cars):
        if car in self.available_cars and num_cars > 0 and num_cars <= self.available_cars[car]:
            current_time = datetime.now()
            self.rental_records[car] = {'num_cars': num_cars, 'time': current_time, 'rate': 200}
            self.available_cars[car] -= num_cars
            print(f"{num_cars} {car} car(s) rented weekly at {current_time}")
        else:
            print("Invalid request")

    def return_car(self, car):
        if car in self.rental_records:
            rental_info = self.rental_records[car]
            rented_time = rental_info['time']
            rental_period = (datetime.now() - rented_time).seconds / 3600  # Convert seconds to hours
            rate = rental_info['rate']
            total_cost = rental_period * rate * rental_info['num_cars']
            print(f"Total cost for returning {rental_info['num_cars']} {car} car(s) is ${total_cost}")
            del self.rental_records[car]
            self.available_cars[car] += rental_info['num_cars']
        else:
            print("Car not rented or already returned")




def main():
    available_cars = {'Toyota Camry': 10, 'Honda Accord': 8, 'BMW i7': 5}

    car_rental = CarRental(available_cars)

    while True:
        print("\n1. Display available cars")
        print("2. Rent a car hourly")
        print("3. Rent a car daily")
        print("4. Rent a car weekly")
        print("5. Return a car")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            car_rental.display_available_cars()
        elif choice in ['2', '3', '4']:
            car_type = input("Enter car type: ")
            num_cars = int(input("Enter number of cars: "))
            if choice == '2':
                car_rental.rent_car_hourly(car_type, num_cars)
            elif choice == '3':
                car_rental.rent_car_daily(car_type, num_cars)
            elif choice == '4':
                car_rental.rent_car_weekly(car_type, num_cars)
        elif choice == '5':
            car_type = input("Enter car type to return: ")
            car_rental.return_car(car_type)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
