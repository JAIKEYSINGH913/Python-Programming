# Q17.
# Create a program to remove duplicate product IDs from a list using sets.

productids = [101, 102, 101, 103, 102, 104]

# list to a set so it will automatically delete duplicates
uniqueids_set = set(productids)
uniqueidslist = list(uniqueids_set)

print(f"Original List: {productids}")
print(f"List Without Duplicates: {uniqueidslist}")
