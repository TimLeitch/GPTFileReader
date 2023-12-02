# File Explorer GUI with Tree View and Checkboxes

This is a simple Python tool for selecting files and reading in their contents. I was needing a way to feed ChatGPT a bunch of .py files contents and paths at once.So I wrote this simple tool to read them in, and shit out a single text document with with the full file path followed by the contents of the selected files. Allows you to have one file that contains the paths and contents of the files. Could be used as a crappy version of git, version control, sending someone a super nerdy email, but lets be real, I used it to send a bunch of files and their contents to Chat GPT to better understand a code base or project. 

## Usage

1. Select a base directory by clicking the "Select Path" button.
2. The tool will display a tree view of files and directories within the selected base directory.
3. Use the checkboxes to select the files you want to merge.
4. Click the "Merge Files" button to merge the selected files.
5. A success message will be displayed if the files are merged successfully. If no files are selected, a warning message will be shown.

## Requirements

- Python 3.2 or higher
- tkinter library

## Installation

1. Clone the repository: `git clone https://github.com/timleitch/repo.git`

## Running the Tool

1. Navigate to the project directory: `cd repo`
2. Run the tool: `python file_explorer_gui.py`

## License

This tool is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

This tool was developed by Tim Leitch and yes.. copilot did write this entire readme. And I am ok with that because I hate writting readme's.