## Final Output

The result is in `final.json`. This file includes the original questions with additional fields based on manual review. It represents the **final output**.


## Files

- `china 1.json`: Original question data organized by character.
- `china_character 1.json`: Background profile for each character.
- `save.jsonl`: Stores all progress and completed annotations as individual JSON lines.
- `final.json`: The final merged and reviewed dataset with 검수 기준 annotations applied.


## Scripts Overview

### anno_main.py
This script is an interactive annotation tool for reviewing question-answer pairs.

> - Loads character question data from `china 1.json`.
> - Allows manual review of each question:
>   - `검수 기준 1`: Is the correct answer truly correct? If yes, then `O`.
>   - `검수 기준 2`: Are any incorrect choices actually correct? If no, then `O`.
>   - `검수 기준 3`: Are any incorrect choices similar? If no, then `O`.
>     - For instance, in `X (1,3),(2,4)`
>       - 1, 3 are a pair of repeated answers. 
>       - 2, 4 are a pair of repeated answers. 
> - Input is handled via terminal with support for `SKIP` (skip current question) and `EXIT` (save and exit).
>   - Use these commands in `검수 기준 1`.  
> - Saves annotation results into `save.jsonl` (line-by-line JSON format).

### export_to_file.py
This script merge the annotation result (in `save.jsonl`) into the original question data.

> - Loads question data from `china 1.json`.
> - Loads annotations from `save.jsonl`.
> - Merge 검수 기준 (`검수 기준 1`, `검수 기준 2`, `검수 기준 3`) into the corresponding questions.
> - Outputs the final dataset with annotation results into `final.json`.


