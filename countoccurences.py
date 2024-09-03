
# Function to count the occurrences of each element in an array
def count_occurrences(arr):
    # Initialize an empty dictionary to store counts
    count_dict = {}
    
    # Iterate through the array
    for num in arr:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # If the number is not in the dictionary, add it with count 1
        else:
            count_dict[num] = 1
    
    print(count_dict)

    # Print the results
    for num, count in count_dict.items():
        print(f"{num} occurs {count} time(s)")

# Example usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 2, 3, 1, 2, 4, 5, 1]
    count_occurrences(array)
