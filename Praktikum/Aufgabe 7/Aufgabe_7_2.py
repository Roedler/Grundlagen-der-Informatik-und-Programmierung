import random, time

def simulate_dice_rolls(num_rolls):
    possible_products = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36]
    product_counts = {product: 0 for product in possible_products}
    for i in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        product = dice1 * dice2
        product_counts[product] += 1
    return product_counts

num_rolls = int(input("Enter the number of dice rolls: "))
start_time = time.time()
product_counts = simulate_dice_rolls(num_rolls)
total_time = time.time() - start_time
print("\nWürfelexperiment: Augenprodukt zweier Würfel")
print(f"Anzahl der Würfe zweier Würfel: {num_rolls}")
print("\nAugenprodukt    Anzahl    Häufigkeit [%]")
for product, count in sorted(product_counts.items()):
    frequency = (count / num_rolls) * 100
    print(f"{product:12} {count:8} {frequency:10.2f}")
print(f"\nDie Simulation (n = {num_rolls}) wurde von Lennart Novak durchgeführt und dauerte {total_time:.3f} Sekunden.")
