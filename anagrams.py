def are_anagrams(str1, str2):
    # 1. Normalize strings (remove spaces and convert to lowercase)
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    
    # Anagrams must have the same length
    if len(s1) != len(s2):
        return False
        
    # 2. Check if the sorted lists of characters are identical
    # This is a simple, highly Pythonic way to check if character counts match.
    return sorted(s1) == sorted(s2)

# --- Example Usage ---
word_a = "Clint Eastwood"
word_b = "old west action"
word_c = "car"

print(f"'{word_a}' and '{word_b}' are anagrams: {are_anagrams(word_a, word_b)}") # True
print(f"'{word_a}' and '{word_c}' are anagrams: {are_anagrams(word_a, word_c)}") # False
