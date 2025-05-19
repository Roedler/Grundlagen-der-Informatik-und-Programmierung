import random
import time

max_factor = int(input("Enter the maximum factor (n): "))
num_questions = int(input("Enter the number of questions: "))

print("\nMultiplication Quiz")
print("========================")
print(f"Multiplication in the range 1 to {max_factor}.")
print(f"Number of questions: {num_questions}\n")

start_time = time.time()
results = []

for i in range(num_questions):
    factor1 = random.randint(1, max_factor)
    factor2 = random.randint(1, max_factor)
    correct_answer = factor1 * factor2

    while True:
        user_answer = int(input(f"{factor1} * {factor2} = "))

        if user_answer == correct_answer:
            elapsed_time = time.time() - start_time
            results.append(f"solved after {elapsed_time:.2f} s: {factor1} * {factor2} = {correct_answer}")
            break
        else:
            print("Error - please try again:")
            elapsed_time = time.time() - start_time
            results.append(f"solved after {elapsed_time:.2f} s: {factor1} * {factor2} = {user_answer} - Error!")

end_time = time.time()
total_time = (end_time - start_time) / 60

print(f"\nEnd! You solved the questions in approx. {total_time:.2f} minutes.")

with open("Multi_Quiz.txt", "w") as file:
    file.write(f"Multiplication Quiz (range 1 to {max_factor}).\n")
    file.write(f"Number of questions: {num_questions}\n")
    for result in results:
        file.write(f"{result}\n")
    file.write(f"The quiz took {total_time:.2f} minutes.\n")

print("The multiplication quiz was completed by Lennart Novak.")
