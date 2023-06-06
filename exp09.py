def is_nearly_equal(a, b):
    # Check if the lengths of the strings differ by more than 1
    if abs(len(a) - len(b)) > 1:
        return False

    # Initialize counters for mutations
    mutation_count = 0
    i = 0
    j = 0

    # Traverse both strings
    while i < len(a) and j < len(b):
        # If characters are different, increment mutation count
        if a[i] != b[j]:
            mutation_count += 1

            # If more than one mutation, strings are not nearly equal
            if mutation_count > 1:
                return False

            # If lengths are different, move the longer string's pointer
            if len(a) > len(b):
                i += 1
            elif len(b) > len(a):
                j += 1
            else:
                # If lengths are equal, move both pointers
                i += 1
                j += 1
        else:
            # If characters are the same, move both pointers
            i += 1
            j += 1

    # If there are extra characters in either string, increment mutation count
    if i < len(a) or j < len(b):
        mutation_count += 1

    # Check if mutation count is at most 1
    return mutation_count <= 1


# Example usage
string1 = input("Enter string1 : ")
string2 = input("Enter string 2 : ")
result = is_nearly_equal(string1, string2)
print(result)
