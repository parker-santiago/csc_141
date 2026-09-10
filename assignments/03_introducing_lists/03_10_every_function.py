groceries = ["milk", "eggs", "bread", "butter", "cheese"]

# len function
print(f"I need to buy {len(groceries)} items from the store.")

# indexing & printing
print(f"\nThe first item on my list is {groceries[0]}.")
print(f"The last item on my list is {groceries[-1]}.")


print(f"\n{groceries[0].title()} is the most important item on my list.")
print(f"We had some earlier but then i SPILLED THE {groceries[0].upper()} ALL OVER THE DAMN FLOOR. I need to buy more.")


print(f"\nAlright, just picked up some {groceries.pop(0)}, only {len(groceries)} more to go")