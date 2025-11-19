# ======================================================
#   Takaful Commission Calculator (GitHub Version)
#   Supports: NIL (Non Investment-Linked) & ILP
#   Author: Megat Hazwan
# ======================================================

def get_commission_rate(plan_type, year):
    """
    Returns commission rate based on plan type and year.
    """

    rates_NIL = {
        1: 0.350,
        2: 0.250,
        3: 0.150,
        4: 0.150,
        5: 0.100,
        6: 0.100,
    }

    rates_ILP = {
        1: 0.200,
        2: 0.200,
        3: 0.135,
        4: 0.185,
        5: 0.150,
        6: 0.150,
    }

    if plan_type == "NIL":
        return rates_NIL.get(year, None)
    elif plan_type == "ILP":
        return rates_ILP.get(year, None)
    else:
        return None


def main():
    print("\n=== Takaful Commission Calculator (GitHub Version) ===")
    print("Plan Types: NIL (Non Investment-Linked) | ILP (Investment-Linked)")

    while True:
        plan = input("Enter Plan Type (NIL/ILP): ").upper()

        if plan not in ["NIL", "ILP"]:
            print("❌ Invalid plan type. Please enter NIL or ILP only.")
            continue

        try:
            premium = float(input("Enter Annual Contribution (RM): "))
            year = int(input("Enter Commission Year (1-6): "))
        except ValueError:
            print("❌ Invalid input. Numbers only.")
            continue

        rate = get_commission_rate(plan, year)

        if rate is None:
            print("❌ Invalid year. Must be between 1–6.")
            continue

        commission = premium * rate

        print("\n===== Commission Result =====")
        print(f"Plan Type           : {plan}")
        print(f"Annual Contribution : RM {premium:.2f}")
        print(f"Year                : {year}")
        print(f"Commission Rate     : {rate * 100:.1f}%")
        print(f"Commission Earned   : RM {commission:.2f}")

        again = input("\nCalculate again? (y/n): ").lower()
        if again != "y":
            print("Thank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
