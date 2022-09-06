# SVG File Generator

> Updated 9/5/2022 by Nick Steele

This is a generator for creating many SVG files with different text. Files will be generated from a template SVG, and will be output to a folder. Optionally, they may be zipped into one file for emailing.

## Usage

**Requires python >3.2.** I intend to create a command-line interface. For now though, just set input and output files in the python file directly. Use as follows:

```shell
cd <root-dir>
python ./gen.py
```

# Example

Start with an input CSV and a template. The first row of the input CSV must be a 'variable name', i.e. a string to be replaced in the template with that column’s data. See CSV and template examples below.

| ![](/blob/docs/csv-example.png)     | ![](/blob/docs/template-example.png) |
| ----------------------------------- | ------------------------------------ |
| Example CSV file                    | Corresponding template file          |

The template will be replaced with the text in the column of the text to replace. For example:

| ![](/blob/docs/output-example-1.png) | ![](/blob/docs/output-example-5.png) |
| ![](/blob/docs/output-example-3.png) | ![](/blob/docs/output-example-4.png) |

# Handy Tips
- Make sure the text to be replaced is aligned/justified correctly (the `$FIRSTNAME` example above had the text object formatted with justification to the center)
- Don’t use anything in the variable name that might make it also exist elsewhere in the file. A common choice is to choose a name and make it unique via a dollar sign (like above), enclosing dollar signs (`$FIRSTNAME$`), or double enclosed curly braces (`{{FIRSTNAME}}`).
- This will automatically zip all output files if you specify a file name for the variable `ZIP_FILE`
- This will also create a simple checklist including all generated files if you specify a file name for the variable `CHECKLIST_FILE`
