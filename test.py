# import time
# import sys

# # Printing
# print("This is a regular print statement")

# while True:
    



# # Reprinting (overwriting) using carriage return
# for i in range(5):
#     sys.stdout.write("\rReprinting line {}.".format(i))
#     sys.stdout.flush()  # Flush the output buffer to ensure it's displayed immediately
#     time.sleep(1)  # Simulate some work being done

# # Add a new line after reprints
# print("\nFinished reprinting.")

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)