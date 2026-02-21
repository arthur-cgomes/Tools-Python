# 🐍Tools Python

Everyday tools with Python!

> All scripts use only the Python standard library — no `pip install` required. Edit the hardcoded input variables at the top of each script, then run it with `python <script>.py`.

---

## 🗄️ SQL Tools

### 1. 🎲 Generate INSERTs (`generate_insert`)

#### Description

Reads a JSON file containing product information, generates SQL `INSERT` statements for each object in the JSON, and saves these statements to a `.sql` file.

#### Functionality

- Loads the content of a JSON file.
- Generates SQL `INSERT` statements for each object in the JSON.
- Empty strings in JSON are rendered as SQL `null`.
- Saves the SQL statements to `insert_products.sql`.

#### Requirements

- JSON file with product data (see `generate_insert/json/example_json_product.json`).

---

### 2. 🗑️ Generate DELETE (`generate_delete`)

#### Description

Generates a `DELETE FROM table WHERE id IN (...)` statement from a hardcoded list of IDs.

#### Functionality

- Receives a list of IDs and a table name as input.
- Generates a single `DELETE` statement with all IDs in the `IN` clause.
- Saves the result to `generate_delete.sql`.

---

### 3. 🔍 Generate SELECT (`generate_select`)

#### Description

Generates a `SELECT` statement from a hardcoded list of IDs, with optional column selection.

#### Functionality

- Receives a list of IDs, a table name, and a list of columns (use `['*']` for all).
- Generates a `SELECT` statement with all IDs in the `WHERE id IN (...)` clause.
- Saves the result to `generate_select.sql`.

---

### 4. ✂️ Split SQL Batch (`split_sql_batch`)

#### Description

Splits a large `.sql` file into smaller batch files, each containing a specified number of `INSERT` statements. Useful for running large imports in production without overloading the database.

#### Functionality

- Reads a `.sql` file.
- Splits it into batches of N statements.
- Saves each batch as `batch_1.sql`, `batch_2.sql`, etc.

#### Requirements

- A `.sql` file containing `INSERT INTO` statements.

---

### 5. 🔄 Convert INSERT to UPDATE (`turns_insert_into_update`)

#### Description

Transforms SQL `INSERT` statements into corresponding `UPDATE` statements. Extracts the table name, columns, and values from the `INSERT` statements, then generates `UPDATE` statements using `id` as the `WHERE` condition.

#### Functionality

- Extracts table name, columns, and values from the provided `INSERT` statements.
- Converts the `INSERT` statements into `UPDATE` statements, using the first column (`id`) in the `WHERE` clause.
- Saves the result to `transform-update.sql`.

#### Example

```sql
-- Input:
INSERT INTO customers (id, name, age) VALUES (1, 'John Doe', 30);

-- Output:
UPDATE customers SET name = 'John Doe', age = 30 WHERE id = 1;
```

---

### 6. 🗑️ Convert INSERT to DELETE (`turns_insert_into_delete`)

#### Description

Reads `INSERT` statements, extracts the value of the first column (`id`) from each, and generates the corresponding `DELETE` statements.

#### Functionality

- Parses one or more `INSERT` statements.
- Extracts the table name and the `id` (first column) from each statement.
- Generates one `DELETE FROM table WHERE id = <value>;` per row.
- Saves the result to `transform-delete.sql`.

---

## 📋 List & ID Tools

### 7. 🔍 Compare Lists (`compare_lists`)

#### Description

Compares two provided lists and generates a file containing the differences between them. Identifies elements present in one list but absent in the other.

#### Functionality

- Receives two lists as input.
- Compares the lists and identifies exclusive elements of each one.
- Generates detailed messages indicating the differences.
- Saves the result to `difference_output.txt`.

---

### 8. ✅ Format IDs (`format_ids`)

#### Description

Formats a list of IDs by adding single quotes and commas, ready for use in SQL `WHERE IN (...)` clauses.

#### Functionality

- Receives a newline-separated list of IDs as input.
- Formats the IDs by adding single quotes and commas.
- Ensures that the last item does not have a trailing comma.
- Saves the formatted list to `formatted_ids.txt`.

---

### 9. 📝 Format CSV Numbers (`format_list_number`)

#### Description

Reads a CSV file containing numbers and formats them with single quotes and commas, ready for use in SQL queries.

#### Functionality

- Reads a CSV file containing a list of numbers.
- Formats each number with single quotes and a comma, except the last.
- Saves the formatted list to `format_list_number.txt`.

#### Requirements

- A CSV file containing numbers in each row.

---

### 10. 🧹 Deduplicate List (`deduplicate_list`)

#### Description

Removes duplicate items from a list while preserving the original order, and generates a report showing which items were removed.

#### Functionality

- Receives a hardcoded list as input.
- Removes duplicates, preserving insertion order.
- Reports total items, unique items, and removed items.
- Saves the result with a summary to `deduplicate_list_output.txt`.

---

### 11. 🆔 Generate UUID List (`generate_uuid_list`)

#### Description

Generates N random UUIDs in the chosen format: one per line, or SQL-ready with single quotes and commas.

#### Functionality

- Generates the specified number of UUIDs (`uuid4`).
- Format type 1: one UUID per line.
- Format type 2: quoted and comma-separated, ready for use in `WHERE IN (...)`.
- Saves the result to `generate_uuid_list_output.txt`.

---

## 📊 CSV Tools

### 12. 🔁 CSV to JSON (`csv_to_json`)

#### Description

Converts a CSV file into a JSON file, producing a list of objects where each row becomes a dict with the CSV headers as keys.

#### Functionality

- Reads a CSV file using the first row as headers.
- Converts each row to a JSON object.
- Saves the result as a pretty-printed JSON array to `csv_to_json.json`.

#### Requirements

- A CSV file with a header row.

---

### 13. 🔎 Compare CSV Columns (`compare_csv_columns`)

#### Description

Compares two columns in a CSV file by header name and reports every row where the values differ. Useful for validating data imports or checking expected vs. actual values.

#### Functionality

- Reads a CSV file.
- Compares two specified columns row by row.
- Reports the row number and both values for each discrepancy.
- Saves the result to `compare_csv_columns_output.txt` (or a "no differences found" message if columns match).

#### Requirements

- A CSV file with a header row containing the two columns to compare.

---

## 🔤 String Tools

### 14. 🐍 CamelCase to snake_case (`camel_to_snake`)

#### Description

Converts a list of camelCase or PascalCase names to snake_case. Handles acronyms correctly (e.g., `HTMLParser` → `html_parser`).

#### Functionality

- Receives a multiline string with one name per line.
- Converts each name from camelCase or PascalCase to snake_case.
- Saves the converted names to `camel_to_snake_output.txt`.

---

### 15. 🗝️ Generate Random Passwords (`generate_password`)

#### Description

Generates random passwords based on user-specified criteria via an interactive prompt.

#### Functionality

- Users can choose from four password types:
  1. Numbers and letters
  2. Only letters
  3. Only numbers
  4. Numbers, letters, and symbols
- Allows users to specify the length and quantity of passwords.
- Outputs the generated passwords to the terminal.

---

## Requirements for All Scripts

- Python 3.x
- No external dependencies (standard library only)
