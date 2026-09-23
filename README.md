# 🐍 Text Analyzer — Python

**Text Analyzer** is a simple but practical Python application that reads a text file, analyzes its contents, and displays useful statistics.

This project was created as **Day 004** of my **365 Days of Code** challenge.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4d37b060-896b-4e62-9cd1-cf56cd1307aa" width="350" alt="Text Analyzer Preview">
</p>


---

## ✨ Features

- 📄 Read text from a `.txt` file
- 🔢 Count the total number of lines
- 🔤 Count the total number of words
- 🧩 Count unique words
- 🔠 Count characters
- ⌨️ Count characters without spaces
- 🏆 Find the most frequently used word
- 📊 Display the TOP 10 most common words
- 🔍 Search for a specific word
- 🔢 Show how many times a searched word appears
- 🔡 Ignore uppercase and lowercase differences
- 🧹 Handle punctuation while analyzing words
- 🌐 Work with UTF-8 text

---

## 🖥️ Example

Given the following `text.txt`:

```text
Programming is fun.
Python is a great programming language.
I love programming because programming helps me create new things.
Python is simple, powerful, and fun.
Every day I learn something new.
```

The program produces statistics similar to:

```text
==================================================
TEXT ANALYZER
==================================================

Reading file: text.txt

==================================================
              TEXT ANALYZER
==================================================

Lines: 5
Words: 32
Unique words: 25
Characters: 207
Characters without spaces: 177

Most common word: programming (4 times)

--------------------------------------------------
TOP 10 WORDS
--------------------------------------------------

1. programming        4
2. is                 3
3. python             2
4. fun                2
...
```

You can then enter a word:

```text
python
```

The program will display:

```text
'python' appears 2 time(s).
```

---

## 🧠 How It Works

The application follows several steps:

1. Reads the contents of `text.txt`.
2. Converts the text to lowercase.
3. Extracts words using regular expressions.
4. Stores word frequencies in a Python dictionary.
5. Calculates general text statistics.
6. Sorts words by their frequency.
7. Displays the ten most frequently used words.
8. Allows the user to search for a specific word.

---

## 📚 Concepts Practiced

This project demonstrates several important Python and programming concepts:

- Functions
- Dictionaries
- Lists
- Strings
- File handling
- Loops
- Conditions
- Exception handling
- Regular expressions
- Lambda expressions
- Sorting
- Basic algorithm analysis

---

## ⚙️ Technologies

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| `re` | Text processing with regular expressions |
| Dictionary | Word frequency storage |
| UTF-8 | Multilingual text support |
| Git | Version control |
| GitHub | Source code hosting |

No external Python libraries are required.

---

## 📁 Project Structure

```text
Day-004-Text-Analyzer/
│
├── main.py
├── text.txt
├── README.md
└── .gitignore
```

### `main.py`

Contains the main application logic and text analysis algorithms.

### `text.txt`

Contains the text that will be analyzed. You can replace its contents with your own text.

### `README.md`

Contains the project documentation.

### `.gitignore`

Prevents unnecessary Python and IDE files from being uploaded to GitHub.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mnerst1/Text-Analyzer-Python.git
```

### 2. Open the Project Directory

```bash
cd Text-Analyzer-Python
```

### 3. Check Python

Make sure Python 3 is installed:

```bash
python --version
```

### 4. Add Your Text

Open:

```text
text.txt
```

Replace its contents with any text you want to analyze.

### 5. Run the Program

```bash
python main.py
```

---

## 🔍 Word Frequency Algorithm

The application uses a Python dictionary to calculate word frequency.

For example:

```text
Python is great.
Python is simple.
Python is powerful.
```

will produce data similar to:

```python
{
    "python": 3,
    "is": 3,
    "great": 1,
    "simple": 1,
    "powerful": 1
}
```

Each word becomes a dictionary key, while the number of occurrences becomes its value.

---

## ⏱️ Algorithm Complexity

If `n` represents the total number of words, building the word-frequency dictionary takes approximately:

```text
O(n)
```

Dictionary lookup takes approximately:

```text
O(1)
```

on average.

If `k` represents the number of unique words, sorting the word-frequency table takes approximately:

```text
O(k log k)
```

This project provides a practical example of using data structures to efficiently process text.

---

## 🌐 UTF-8 Support

The file is opened using:

```python
encoding="utf-8"
```

This allows the analyzer to work with multilingual text, including:

- 🇬🇧 English
- 🇰🇿 Қазақша
- 🇷🇺 Русский
- and many other languages

---

## 🛠️ Future Improvements

Future versions could include:

- 📊 Word frequency charts
- 🖥️ Graphical user interface
- 📂 File selection
- 📝 Multiple-file analysis
- 🚫 Stop-word filtering
- 🔤 Average word length
- 📖 Reading-time estimation
- 📈 More detailed statistics
- 💾 Export results to JSON
- 📄 Export results to CSV
- 🌐 Web interface
- 🔌 REST API

---

## 🎯 365 Days of Code

This repository is part of my **365 Days of Code** challenge.

### Progress

| Day | Project | Technology |
|---|---|---|
| Day 001 | Password Generator | Python |
| Day 002 | Multilingual Calculator | C# / WPF |
| Day 003 | StudyFlow | Kotlin / Android |
| **Day 004** | **Text Analyzer** | **Python** |

The goal of this challenge is to improve my programming skills by building projects with different languages, frameworks, databases, APIs, algorithms, and development tools.

---

## 👨‍💻 Author

Developed by **Miras**.

Part of the **365 Days of Code** challenge.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

Feedback and suggestions are welcome.

---

## 📄 License

This project is intended for educational and personal use.
