# Burmese-Tools

**burmese-tools** is a Python library that mainly designed for transformation between unicode and zawgyi burmese lanuage script. Moreover, it also support syllable tokenization for burmese unicode and parital syllable tokenization for burmese zawgyi.

## Features
- Zawgyi to Unicode Conversion: Convert Zawgyi-encoded text to Unicode.
- Unicode to Zawgyi Conversion: Transform Unicode text back to Zawgyi.
- Unicode Syllable Tokenization: Tokenize Burmese Unicode text into syllables with customizable splitting.
- Partial Zawgyi Syllable Tokenization: Tokenize Burmese Zawgyi text into syllables.


## Installation
You can install this library from PyPI:
```python
pip install burmese-tools
```

## Usage

### Importing the Library
```python
from burmese_tools import tools
```


### Convert Zawgyi to Unicode
```python
text_zawgyi = "ကႏၲာရ"
converted_text = tools.zaw2uni(text_zawgyi)
print(converted_text)  # Output: ကန္တာရ
```

### Convert Unicode to Zawgyi
```python
text_unicode = "ကန္တာရ"
converted_text = tools.uni2zaw(text_unicode)
print(converted_text)  # Output: ကႏၲာ႐
```

### Tokenize Unicode Text into Syllables
The uni_syllable function is a utility to tokenize Unicode text into syllable tokens, allowing for flexible splitting methods.

**Features**
- Tokenizes Unicode text into syllables.
- Provides two types of splitting:
    - Type 1: Splits `ဂန္ဓာရ` into `['ဂ', 'န္ဓာ', 'ရ']`. (default)
    - Type 2: Splits `ဂန္ဓာရ` into `['ဂန္', 'ဓာ', 'ရ']`.
- Supports an optional transform to replace `္` with ` ်` (applies only when type=2) d
    - default = True

```python
text = "ကန္တာရ"
tokens = tools.uni_syllable(text, type=1)
print(tokens)  # Output: ['က', 'န္တာ', 'ရ']
```

```python
text = "ကန္တာရ"
tokens = tools.uni_syllable(text, type=2)
print(tokens)  # Output: ['ကန်', 'တာ', 'ရ']
```

```python
text = "ကန္တာရ"
tokens = tools.uni_syllable(text, type=2, transform=False)
print(tokens)  # Output: ['ကန္', 'တာ', 'ရ']
```

### Tokenize Zawgyi Text into Partial Syllables
```python
text = "ကႏၲာရ"
tokens = tools.zaw_partial_syllable(text)
print(tokens)  # Output: ['က', 'ႏၲာ', 'ရ']  in unicode ['က', 'န္တာ', 'ရ'] 
```

## Contributing
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch for your feature/bug fix.
- Make your changes and test thoroughly.
- Submit a pull request.


## License
This library is licensed under the MIT License. Feel free to use, modify, and distribute it.


# Acknowledgments

This library was developed to simplify Burmese text processing for developers and linguists. Special thanks to [**Sa Phyo Thu Thet**](https://github.com/SaPhyoThuHtet), from Simbolo  for his valuable guidance, kindness, and support in teaching me. His mentorship has been instrumental in shaping my understanding and skills in NLP. Most importantly, I have referred and inspired by Sa Phyo Thu Thet's [Myanmar-nlp-tool](https://github.com/SaPhyoThuHtet/myanmar-nlp-tool) as one of the cornerstones to complete this project.
Contributions and feedback from the community are also highly appreciated.
