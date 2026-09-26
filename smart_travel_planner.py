"""A beginner-friendly console app for estimating a group's trip costs."""


def calculate_transportation_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_hotel_cost(cost_per_day, travel_days):
    return cost_per_day * travel_days


def calculate_food_cost(cost_per_traveler_per_day, traveler_count, travel_days):
    return cost_per_traveler_per_day * traveler_count * travel_days


def calculate_activity_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_total_trip_cost(transportation, hotel, food, activities):
    return transportation + hotel + food + activities


def calculate_cost_per_traveler(total_cost, traveler_count):
    return total_cost / traveler_count


def calculate_average_daily_cost(total_cost, travel_days):
    return total_cost / travel_days


def get_non_negative_cost(prompt):
    while True:
        try:
            cost = float(input(prompt))
            if cost < 0:
                print("Cost cannot be negative. Please try again.")
                continue
            return cost
        except ValueError:
            print("Please enter a valid number, such as 25 or 25.50.")


def get_positive_integer(prompt, item_name):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print(f"{item_name} must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number greater than zero.")


def get_required_text(prompt, item_name):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"{item_name} cannot be empty. Please try again.")


def main():
    print("=" * 42)
    print("          SMART TRAVEL PLANNER")
    print("=" * 42)

    traveler_name = get_required_text("Traveler name: ", "Traveler name")
    destination = get_required_text("Destination: ", "Destination")
    traveler_count = get_positive_integer("Number of travelers: ", "Number of travelers")
    travel_days = get_positive_integer("Number of travel days: ", "Number of travel days")

    print("\nEnter estimated costs in your chosen currency.")
    transportation_per_traveler = get_non_negative_cost(
        "Transportation cost per traveler: "
    )
    hotel_per_day = get_non_negative_cost("Hotel cost per day (for the group): ")
    food_per_traveler_per_day = get_non_negative_cost(
        "Food cost per traveler per day: "
    )
    activities_per_traveler = get_non_negative_cost(
        "Activity cost per traveler (for the whole trip): "
    )

    travel_information = {
        "traveler_name": traveler_name,
        "destination": destination,
        "traveler_count": traveler_count,
        "travel_days": travel_days,
        "transportation_per_traveler": transportation_per_traveler,
        "hotel_per_day": hotel_per_day,
        "food_per_traveler_per_day": food_per_traveler_per_day,
        "activities_per_traveler": activities_per_traveler,
    }

    transportation_total = calculate_transportation_cost(
        travel_information["transportation_per_traveler"],
        travel_information["traveler_count"],
    )
    hotel_total = calculate_hotel_cost(
        travel_information["hotel_per_day"], travel_information["travel_days"]
    )
    food_total = calculate_food_cost(
        travel_information["food_per_traveler_per_day"],
        travel_information["traveler_count"],
        travel_information["travel_days"],
    )
    activities_total = calculate_activity_cost(
        travel_information["activities_per_traveler"],
        travel_information["traveler_count"],
    )
    trip_total = calculate_total_trip_cost(
        transportation_total, hotel_total, food_total, activities_total
    )
    per_traveler_total = calculate_cost_per_traveler(
        trip_total, travel_information["traveler_count"]
    )
    average_daily_total = calculate_average_daily_cost(
        trip_total, travel_information["travel_days"]
    )

    print("\n" + "=" * 42)
    print("              TRIP SUMMARY")
    print("=" * 42)
    print(f"Traveler:             {travel_information['traveler_name']}")
    print(f"Destination:          {travel_information['destination']}")
    print(f"Travelers:            {travel_information['traveler_count']}")
    print(f"Travel days:          {travel_information['travel_days']}")
    print("-" * 42)
    print(f"Transportation:       {transportation_total:>12,.2f}")
    print(f"Hotel:                {hotel_total:>12,.2f}")
    print(f"Food:                 {food_total:>12,.2f}")
    print(f"Activities:           {activities_total:>12,.2f}")
    print("-" * 42)
    print(f"Overall trip cost:    {trip_total:>12,.2f}")
    print(f"Cost per traveler:    {per_traveler_total:>12,.2f}")
    print(f"Average daily cost:   {average_daily_total:>12,.2f}")
    print("=" * 42)
    print("All costs are shown in the currency you entered.")


if __name__ == "__main__":
    main()