# PDF2df
Web application for converting PDF to tabular data to aid in [Search4All](https://github.com/faizhalas/Search4All) processes.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)][share_link]
[![License](https://img.shields.io/github/license/faizhalas/library-tools?color=blue)](https://github.com/faizhalas/PDF2df/blob/main/LICENSE)

### How to use it?
**1.** Put your PDFs here.  We recommend reviewing the style of the submitted document; the technique is heavily dependent on style in common.

**2.** Fill **Remove certain text before 'your text'** if you want to delete words that appear before the word you input 

**3.** Fill **Remove certain text on your PDF** if you want to remove words that appear on the PDF.

**4.** Write the word separator followed by a semicolon (;). Keep in mind that specific words are case-sensitive. 
- An article, for example, has introduction, method, and result sections (written entirely in capital letters.). Then type the following into the text box:
```
INTRODUCTION; METHOD; RESULT
```

**5.** Click the convert button. Copy the content and paste it into your Google Sheet.















[share_link]:https://pdf2df.streamlit.app
