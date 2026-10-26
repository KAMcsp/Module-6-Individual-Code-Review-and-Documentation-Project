# Design Decisions

I renamed functions and variables so their purpose is clear without reading every line. `do_math_stuff` became `process_numbers` and `do_string_stuff` became `format_words_by_length`, because the new names describe what each function does. Variables like `list1`, `list2` and `x` became `numbers`, `fruits` and `word`, which describe what they hold instead of their type.

I replaced the loops with simpler Python features. The number loop became a list comprehension, which builds the list in one readable statement. The string loop became `" ".join(...)`, which removes the need to add a space after each word and then strip the last one. I also moved the values 2, 3 and the word-length limit into named constants so they are not hidden inside the logic.

These changes make the program easier to maintain. The docstrings explain each function's purpose, parameters and return value, and the constants mean a rule can be changed in one place. The program still produces the same output as the original.
