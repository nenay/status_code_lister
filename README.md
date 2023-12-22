# status_code_lister

## Overview
This Python script is designed to check the status codes of a list of URLs and provide feedback on their availability. Additionally, it can generate an output file that organizes URLs based on their HTTP status codes.

## Features
Input: Takes a text file as input, containing a list of URLs.
Output: Displays the URL and its corresponding HTTP status code on the console.
Optional Output File: With the -o flag, the script generates an output file that groups URLs by their status codes.

## Usage
Basic Usage
```
python status_code_lister.py -i your_file_with_urls.txt
```
Output File Generation
```
python status_code_lister.py -i your_file_with_urls.txt -o output.txt

Example Output File
The generated output file will have sections for each HTTP status code, listing URLs with that status:
```
Status code 200:
https://example.com/page1
https://example.com/page2

Status code 404:
https://example.com/not_found
```
## Dependencies
requests library
### Requirements
Python 3.x
