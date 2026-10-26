# Code Review

## Initial Review

Original output:

```
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```

### 1. Unclear names
`do_math_stuff`, `do_string_stuff`, `list1`, `list2`, `x` and `s` do not explain what they do or hold. This makes the code harder to understand.

### 2. No documentation
The functions have no docstrings, so the rules (doubling even numbers, tripling odd numbers, uppercasing words longer than five letters) are not explained anywhere.

### 3. Code that could be simplified
`do_math_stuff` uses a loop with `append()` that could be a list comprehension. `do_string_stuff` builds a string with `+=`, adds an extra space after every word and then uses `strip()` to remove it. This is longer and harder to maintain than needed.

## Final Review

**Did I address the three issues?** Yes.

1. **Unclear names:** Renamed functions to `process_numbers` and `format_words_by_length`, and variables to `numbers`, `words`, `fruits` and `word`, following PEP 8. I verified this by reading `main()` and confirming it is understandable on its own.
2. **No documentation:** Added a module docstring and PEP 257 docstrings to every function. I verified this by running `help()` on each function.
3. **Simplification:** Replaced the number loop with a list comprehension, replaced the string loop with `" ".join(...)`, and moved the numbers 2, 3 and the length limit into named constants. I verified this by running the program and comparing the output with the original.

**Are the names clear and descriptive?** Yes.

**Does each function have documentation?** Yes.

**Did the changes improve readability and maintainability?** Yes. The code is shorter and the rules are documented and easy to change.

**Does the program still produce the expected output?** Yes:

```
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```
