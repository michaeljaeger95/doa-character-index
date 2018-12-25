# Dumbing of Age - Character statistics

This script collects statistics for the archive page of dumbingofage.com

For each character listed in list.txt _and pair of characters_, counts results as listed on http://www.dumbingofage.com/tag/<name>+<name>/ in a Pandas Series and a DataFrame. For now, these are merely printed to the console.

I don't plan to continue working on this but encourage further development, especially visualization. 

### Preliminary results

If you don't actually want to run the script (it can take a while), here are results dated Dez. 25th 2018:

* single characters:

| character  | app. |
| ---------- | ---- |
| joyce      | 1024 |
| walky      | 671  |
| dorothy    | 618  |
| billie     | 596  |
| amber      | 423  |
| sal        | 386  |
| danny      | 369  |
| becky      | 349  |
| sarah      | 345  |
| ruth       | 308  |
| ethan      | 307  |
| dina       | 289  |
| joe        | 283  |
| mike       | 194  |
| amazi-girl | 168  |
| leslie     | 121  |
| carla      | 117  |
| jacob      | 109  |
| roz        | 103  |
| marcie     | 71   |
| malaya     | 58   |
| lucy       | 21   |

* pairs:

|            | joyce | walky | dorothy | billie | amber | sal  | danny | becky | sarah | ruth | ethan | dina | joe  | mike | amazi-girl | leslie | carla | jacob | roz  | marcie | malaya | lucy |
| ---------- | ----- | ----- | ------- | ------ | ----- | ---- | ----- | ----- | ----- | ---- | ----- | ---- | ---- | ---- | ---------- | ------ | ----- | ----- | ---- | ------ | ------ | ---- |
| joyce      | -     | 311   | 337     | 205    | 55    | 100  | 33    | 240   | 248   | 46   | 129   | 115  | 142  | 92   | 20         | 46     | 21    | 70    | 56   | 7      | 7      | 0    |
| walky      | -     | -     | 341     | 159    | 68    | 84   | 27    | 74    | 44    | 29   | 59    | 56   | 76   | 97   | 19         | 45     | 9     | 7     | 36   | 6      | 2      | 4    |
| dorothy    | -     | -     | -       | 94     | 52    | 32   | 58    | 54    | 63    | 31   | 49    | 40   | 85   | 28   | 29         | 47     | 9     | 17    | 55   | 0      | 3      | 0    |
| billie     | -     | -     | -       | -      | 30    | 92   | 28    | 44    | 76    | 227  | 11    | 46   | 5    | 42   | 10         | 1      | 26    | 7     | 19   | 7      | 3      | 17   |
| amber      | -     | -     | -       | -      | -     | 60   | 119   | 21    | 27    | 33   | 106   | 73   | 26   | 28   | 20         | 0      | 9     | 6     | 2    | 5      | 2      | 0    |
| sal        | -     | -     | -       | -      | -     | -    | 61    | 16    | 13    | 16   | 36    | 13   | 5    | 28   | 46         | 4      | 38    | 0     | 2    | 65     | 42     | 1    |
| danny      | -     | -     | -       | -      | -     | -    | -     | 15    | 15    | 7    | 75    | 27   | 90   | 8    | 42         | 0      | 1     | 3     | 4    | 3      | 2      | 0    |
| becky      | -     | -     | -       | -      | -     | -    | -     | -     | 54    | 12   | 24    | 110  | 12   | 20   | 11         | 19     | 2     | 20    | 7    | 0      | 0      | 0    |
| sarah      | -     | -     | -       | -      | -     | -    | -     | -     | -     | 21   | 22    | 70   | 35   | 11   | 9          | 0      | 2     | 53    | 11   | 0      | 2      | 0    |
| ruth       | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | 8     | 26   | 4    | 4    | 2          | 0      | 32    | 3     | 5    | 1      | 1      | 1    |
| ethan      | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | 48   | 6    | 62   | 8          | 0      | 7     | 13    | 1    | 4      | 1      | 0    |
| dina       | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | 3    | 20   | 6          | 3      | 8     | 9     | 6    | 0      | 0      | 0    |
| joe        | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | 16   | 3          | 47     | 2     | 24    | 37   | 2      | 4      | 0    |
| mike       | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | 2          | 2      | 4     | 1     | 1    | 0      | 0      | 0    |
| amazi-girl | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | 3      | 9     | 5     | 2    | 14     | 6      | 0    |
| leslie     | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | -      | 0     | 0     | 43   | 2      | 0      | 0    |
| carla      | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | -      | -     | 1     | 1    | 20     | 23     | 0    |
| jacob      | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | -      | -     | -     | 3    | 0      | 0      | 0    |
| roz        | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | -      | -     | -     | -    | 0      | 0      | 0    |
| marcie     | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | -      | -     | -     | -    | -      | 35     | 2    |
| malaya     | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | -      | -     | -     | -    | -      | -      | 3    |
| lucy       | -     | -     | -       | -      | -     | -    | -     | -     | -     | -    | -     | -    | -    | -    | -          | -      | -     | -     | -    | -      | -      | -    |
