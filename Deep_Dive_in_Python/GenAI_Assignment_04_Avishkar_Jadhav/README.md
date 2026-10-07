# Assignment 4 - Python File Handling

This assignment demonstrates basic Python file handling operations including
reading, writing, appending, file modes, data extraction, and basic file
error handling.

## Project Files

- `file_handling_assignment.ipynb` - Contains solutions for all 7 tasks.
- `sales_data.txt` - Stores sales records used by the tasks.
- `product_info.txt` - Stores product information entered by the user.
- `discounted_sales.txt` - Stores discounted sales prices generated in Task 7.
- `README.md` - Project documentation.

## Tasks

### Task 1 - Write Sales Records to a File
Creates `sales_data.txt`, writes sales records to the file, and reads and
displays the contents.

### Task 2 - Read File in Different Ways
Demonstrates:
- `read()`
- `readline()`
- `readlines()`
- Converting file data into integers.

### Task 3 - Append New Sales
Appends new sales records to `sales_data.txt` and displays the updated file.

### Task 4 - Generate Summary Report
Reads the sales data and calculates:
- Total sales
- Highest sale
- Lowest sale
- Average sale

### Task 5 - Create Product Info File
Takes product names and prices from the user, writes them to
`product_info.txt`, and reads and displays the file.

### Task 6 - Read File Safely
Takes a filename from the user and checks whether the file exists using
`os.path.exists()` before reading it.

### Task 7 - Export Discounted Prices
Reads sales prices from `sales_data.txt`, applies a 10% discount, writes the
discounted prices to `discounted_sales.txt`, and displays the result.

## How to Run

1. Open the assignment folder in VS Code.
2. Open `file_handling_assignment.ipynb`.
3. Select the Python Jupyter kernel.
4. Run the notebook cells in order.
5. Make sure the required text files are present in the same project folder.

## Concepts Used

- `open()`
- Read mode (`r`)
- Write mode (`w`)
- Append mode (`a`)
- `read()`
- `readline()`
- `readlines()`
- `write()`
- `writelines()`
- `close()`
- `os.path.exists()`
- Basic file operations

## Restrictions Followed

- No pandas
- No CSV module
- No external libraries
- Python file handling operations are used directly.