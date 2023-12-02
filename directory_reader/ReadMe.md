# File Explorer GUI with Tree View and Checkboxes

This is a simple Python tool that provides a graphical user interface (GUI) for selecting files and reading in their contents. I was needing a way to feed ChatGPT a bunch of pyfiles I was working on at once, and did not want to work it up using their actual API. So I wrote this simple tool to read them in, and provide a GPT with the paths and the contents of the files to help it with understanding complex problems and code bases. 

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
2. Install the required dependencies: `pip install -r requirements.txt`

## Running the Tool

1. Navigate to the project directory: `cd repo`
2. Run the tool: `python file_explorer_gui.py`

## License

This tool is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

This tool was developed by Tim Leitch and yes.. copilot did write this entire readme. And I am ok with that because I hate writting readme's.