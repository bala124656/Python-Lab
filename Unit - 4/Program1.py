try:
    with open("log.txt", "r") as file:
        count = 0

        for line in file:
            print(line.strip())

            if "ERROR" in line:
                count += 1

        print("Total ERROR messages:", count)

except FileNotFoundError:
    print("Error: log.txt file does not exist.")
