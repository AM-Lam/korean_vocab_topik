# Korean Vocabulary List Processor
This script manipulates a Korean vocabulary dataset into alphabetically ordered lists respectively using **Python Pandas**, focusing on combining vocabulary by elimating the words having multiple meanings and sorting by frequency.

The dataset is sourced from the TOPIK and Go databases provided by Julien Shim (https://github.com/julienshim/combined_korean_vocabulary_list).

## Table of Contents
- [Installation](#installation)  
- [Usage](#usage)  
- [Code Explanation](#explanation)  
- [Result Output](#output)  


<a name="installation"></a>

## Installation
To run this code, ensure you have the following packages installed:

```pip install pandas numpy```

<a name="usage"></a>

## Usage
1. Place the input file *combined_topik_go.tsv* in the *./output/* directory.
2. Run the script *main.py*. It will load the dataset and process it accordingly.

    ```python3 main.py```
3. A output file *newline_korean_dict.txt* is generated

<a name="explanation"></a>

## Code Explanation
- Imports:
    - **Python pandas** and **numpy** for data manipulation and analysis.
- Data Loading:
    - The script loads a **tsv**(tab-separated values) file containing Korean vocabulary.
- Processing:
    - Data Cleaning
        - A filter is applied to identify rows with Korean vocabulary that contaminated with 
        1. numbers(indicating multiple meanings)
        2. leading or trailing white spaces 
        4. special characters(~)
    - The result is stored in a new column called merged.
- Sorting:
    - The *DataFrame* is sorted by frequency in descending order for easier access to the most common words.
- Combining:
    - Group and extract the vocabularies from the table into lists to get the result.

<a name="output"></a>

## Result Output
The final output is a sorted list of Korean vocabulary with their hints, ready for further analysis or display.
```
하 ['하얀색', '하순', '하상하', '하나님', '하품이 나오다', '하나하나', '하반기', '하룻밤', '하필', '하숙집', '하도하도 기가 막혀서', '하느님', '하드웨어', '하하하하 웃다', '하긴', '하여튼', '하천', '하얗다', '하지만', '하루를 보내다', '하늘이 높다', '하나', '하다', '하다운동을 ', '하늘색', '하숙', '하숙비', '하양으로 색칠하다', '하차'] 

초 ['초등학생', '초록색', '초순', '초청장', '초보자', ...] 

저 ['저곳', '저런', '저울에 달다', '저녁때', ...] 

...
```

