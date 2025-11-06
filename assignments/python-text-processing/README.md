```markdown
# 📘 Assignment: Python Text Processing

## 🎯 Objective

Learn how to read and write files, manipulate and analyze strings, and build small command-line tools for processing text data in Python.

## 📝 Tasks

### 🛠️ Core: Text Processing CLI

#### Description
Create a command-line Python program that accepts a text file as input and performs common text-processing operations such as counting words/lines/characters, finding the most frequent words, and performing a find-and-replace. The program should be well-structured, include input validation, and handle file-related errors gracefully.

#### Requirements
Completed program should:

- Accept a path to a text file as input and validate that the file exists and is readable.
- Provide at least the following operations selected via command-line flags: count (words/lines/chars), top (N most frequent words), find-and-replace, and extract (e.g., email addresses or URLs).
- Print clear, human-readable output to the terminal and, when requested, write results to an output file.
- Handle edge cases: empty files, non-text input, and invalid command-line arguments.
- Include a brief usage message and exit codes for failure modes.

Example usage:

```bash
# Count words in a file
python3 starter-code.py --input sample.txt --count words

# Show top 10 most common words and write to results.txt
python3 starter-code.py --input sample.txt --top 10 --output results.txt

# Replace 'foo' with 'bar' in-place (or write to a new file)
python3 starter-code.py --input sample.txt --replace foo bar --inplace
```

### 🛠️ Optional Enhancements

#### Description
Add one or more enhancements to increase usability or robustness.

#### Suggested enhancements

- Add regular-expression based search/replace support.
- Support multiple input files or recursive directory processing.
- Provide interactive prompts or a small menu mode for users who prefer not to use flags.
- Add basic unit tests for core processing functions and include a small sample dataset.

### 📄 Deliverables

- `starter-code.py` (a starter script is provided; students may modify or replace it).
- `README.md` (this file) with run instructions.
- Optional sample input files or additional helper scripts.

### ✅ How to run (example)

```bash
# from the assignment directory
python3 starter-code.py --input ../data-analysis/data.csv --count words
```

### 💡 Grading notes (teacher-facing)

- Correctness of file I/O and string processing
- Robustness (error handling and validation)
- Code clarity and use of functions
- At least one optional enhancement implemented for full marks

``` 
