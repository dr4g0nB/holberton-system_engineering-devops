# Shell, I/O Redirections and filters
### Learning Objectives
### Shell, I/O Redirection
- What do the commands head, tail, find, wc, sort, uniq, grep, tr do
- How to redirect standard output to a file
- How to get standard input from a file instead of the keyboard
- How to send the output from one program to the input of another program
- How to combine commands and filters with redirections

#### Special Characters
- What are special characters
- Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them

#### Other Man Pages
- How to display a line of text
- How to concatenate files and print on the standard output
- How to reverse a string
- How to remove sections from each line of files
- What is the /etc/passwd file and what is its format
- What is the /etc/shadow file and what is its format

### :file_folder: Tasks
Directory | Language
----- | -----
0 | prints “Hello, World”, followed by a new line to the standard output
1 | displays a confused smiley "(Ôo)'
2 | display the content of the /etc/passwd file
3 | Display the content of /etc/passwd and /etc/hosts
3 | Display the last 10 lines of /etc/passwd
3 | Display the first 10 lines of /etc/passwd
3 | displays the third line of the file iacta.
3 | script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
3 | script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
9 | duplicates the last line of the file iacta
10 | eletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders
11 | counts the number of directories and sub-directories in the current directory
12 | displays the 10 newest files in the current directory
13 | takes a list of words as input and prints only words that appear exactly once
14 | Display lines containing the pattern “root” from the file /etc/passwd
15 | Display the number of lines that contain the pattern “bin” in the file /etc/passwd
16 | isplay lines containing the pattern “root” and 3 lines after them in the file /etc/passwd
17 | Display all the lines in the file /etc/passwd that do not contain the pattern “bin”
18 | Display all lines of the file /etc/ssh/sshd_config starting with a letter
19 | Replace all characters A and c from input to Z and e respectively
20 | removes all letters c and C from input
21 | cript that reverse its input
22 | script that displays all users and their home directories, sorted by users
