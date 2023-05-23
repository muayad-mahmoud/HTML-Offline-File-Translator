

# HTML Translator

This is a simple Python project for translating HTML files stored locally on your PC. The project allows users to translate specific HTML tags to a target language.

## Installation

To install the dependencies for the project, run the following command:

```sh
pip install -r requirements.txt
```

## Usage

To use the HTML Translator, follow these steps:

1. Open the `translate.py` file in a text editor.


```python
# Specify the path to the directory containing the HTML files
directory = "/path/to/directory"
```

3. In the same function, specify the HTML tags you want to translate:

```python
# Specify the HTML tags to translate
elements = soup.find_all(["h1", "p",....etc])
```

4. In the same function, specify the target language for the translation:

```python
# Specify the language code for the translation
translator = GoogleTranslator(source='Source Language', target='Target Language')
```

5. Save the `translate.py` file.

6. Open a terminal or command prompt and navigate to the directory containing the `translate.py` file.

7. Run the following command to translate the HTML files:

```sh
python translate.py
```


## Acknowledgements

This projectwas developed as part of an assessment for a company and is a simplified version of a full-fledged HTML translation tool.
