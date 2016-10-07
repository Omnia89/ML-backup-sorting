# ML-backup-sorting
A simple python library for extract the data from a MoneyLover backup and make them human-readable.

### Introduction

Some time ago I started to need some money-tracker app for my expence. Among the many options
I chose MoneyLover (found it [here](https://play.google.com/store/apps/details?id=com.bookmark.money), and some of the code [here](https://www.livecoding.tv/help-14/profile/)).

Great app, I love it! BUT... I want to export the expence I made and display in a better way on my PC, but the default export tool isn't what you could expect, it extracts only few information, too few!

So I ended up doing a tool by myself, a simple python code that reads from the backup of the app data.

### How to use it

- Download the `MoneyLover_backup_extractor.py` file
- Download the backup file `.mlx` from the app: `Settings` -> `Restore backup` -> `Tap one` -> `Share`
- Open the `moneylover_parser` file with the python IDLE and use it like in the example>

```python

extractor = moneylover_parser('C:/Downloads/backup.mlx')

#for extract all tables, even 'currencies'
extractor.extractAll() #you can specify the destination path as parameter, if not it create a /extracted_mxl/ folder

#for only a specified table
extractor.extractTable('categories') #specify the table name
```
