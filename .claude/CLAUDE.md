# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A collection of standalone Python utility scripts for SQL and data formatting tasks. Each tool lives in its own directory and is run independently. No external dependencies — standard library only.

## Running the Tools

Each script is run directly with Python from its directory or from the repo root:

```sh
python compare_lists/compare_lists.py
python format_ids/format_ids.py
python format_list_number/format_list_number.py
python generate_insert/generate_insert.py
python generate_password/generate_password.py
python turns_insert_into_update/transform.py
```

Most scripts require editing hardcoded input variables directly in the file before running. Only `generate_password.py` is interactive (prompts user at runtime).

There are no tests, no build system, and no dependency installation needed.

## Architecture

All tools follow the same pattern:
1. Input comes from either a hardcoded variable (edit before running) or a file path variable
2. Processing is done by one or two pure functions
3. Output is written to a `.txt` or `.sql` file in the working directory

### Tools

| Tool | Input | Output |
|------|-------|--------|
| `compare_lists/` | Two hardcoded lists | `difference_output.txt` |
| `format_ids/` | Hardcoded newline-separated IDs string | `formatted_ids.txt` |
| `format_list_number/` | CSV filename variable | `format_list_number.txt` |
| `generate_insert/` | JSON file in `json/` subfolder | `insert_products.sql` |
| `generate_password/` | Interactive prompts | Console output |
| `turns_insert_into_update/` | Hardcoded INSERT statements string | `transform-update.sql` |

### Key behaviors to preserve

- `generate_insert.py`: empty strings in JSON are rendered as SQL `null`; all other strings are wrapped in single quotes
- `turns_insert_into_update/transform.py`: first column is always treated as `id` and used in the `WHERE` clause
- `format_ids.py` and `format_list_number.py`: output is formatted for SQL `WHERE IN (...)` clauses — quoted, comma-separated, no trailing comma

## Language

Comments and user-facing messages are written in Portuguese.
