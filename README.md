# BookBot

BookBot is a Python tool that retrieves books from the Gutenberg Library. It provides insights into the word count and the frequency of each lowercase character in the text. The program displays the results in an easy-to-read format.

## Example Output

=========== BOOKBOT ============
Analyzing book found at `books/frankenstein.txt`...

----------- Word Count ----------
Total words found: **75,767**

--------- Character Count -------
- **e**: 44,538
- **t**: 29,493
- **a**: 25,894
- **o**: 24,494
- **i**: 23,927
- **n**: 23,643
- **s**: 20,360
- **r**: 20,079
- **h**: 19,176
- **d**: 16,318
- **l**: 12,306
- **m**: 10,206
- **u**: 10,111
- **c**: 9,011
- **f**: 8,451
- **y**: 7,756
- **w**: 7,450
- **p**: 5,952
- **g**: 5,795
- **b**: 4,868
- **v**: 3,737
- **k**: 1,661
- **x**: 691
- **j**: 497
- **q**: 325
- **z**: 235
- **æ**: 28
- **â**: 8
- **ê**: 7
- **ë**: 2
- **ô**: 1

============= END ===============

## HOW TO RUN:
To analyze a specific book, use the following command:

```bash
python3 main.py books/frankenstein.txt
