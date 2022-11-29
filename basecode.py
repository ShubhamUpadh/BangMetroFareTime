def fxStationsFare(stn):
    StFr = {
        0: 10, 1: 10, 2: 15, 3: 15, 4: 18, 5: 20, 6: 22,
        7: 25, 8: 28, 9: 30, 10: 30, 11: 35, 12: 35, 13: 38, 14: 40,
        15: 42, 16: 45, 17: 45, 18: 50,
        19: 50, 20: 52, 21: 55, 22: 58, 23: 60, 24: 60,

    }

    return StFr.get(stn, 60)


for _ in range(5):
    n = input("How many stations?  ")
    print(f"Fare = {fxStationsFare(int(n))}")
