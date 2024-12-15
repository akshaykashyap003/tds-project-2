# TDS Project: Automated Data Analysis Tool

## Overview
This project is a Python-based tool designed to automate data analysis, generate insights using AI, and provide visualizations for datasets. It integrates OpenAI's GPT models via a proxy API and simplifies the process of analyzing and summarizing datasets. The tool detects encoding, handles CSV files, and creates comprehensive reports in Markdown format, complete with visualizations.

## Features
1. **Encoding Detection**: Automatically detects the encoding of CSV files to ensure proper data loading.
2. **Data Analysis**:
   - Extracts key statistics from datasets.
   - Identifies missing values and their distribution.
3. **AI Integration**:
   - Utilizes OpenAI's GPT model to provide insights and suggestions for further analysis and visualization.
4. **Visualizations**:
   - Generates bar charts to visualize missing values across dataset columns.
5. **Markdown Reporting**:
   - Creates a detailed `README.md` file summarizing the analysis.
   - Includes insights, summary statistics, and visualization links.

## Installation

### Prerequisites
- Python 3.x
- Libraries: `pandas`, `matplotlib`, `requests`, `chardet`, `openai`
- A valid OpenAI API proxy token

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your OpenAI API proxy token is configured in the script.
   - Replace the placeholder `AIPROXY_TOKEN` with your actual token in the script.

## Usage

### Running the Tool
To analyze a dataset, run the script from the command line:
```bash
python autolysis.py <path_to_dataset.csv>
```
Replace `<path_to_dataset.csv>` with the path to your dataset file.

### Output
1. **Markdown Report**:
   - The script generates a `README.md` file summarizing the dataset analysis.
2. **Visualization**:
   - A bar chart (`missing_values.png`) depicting missing value distribution is saved in the working directory.

### Example Output
- **Markdown Report (`README.md`)**: Contains dataset overview, data types, summary statistics, missing values analysis, AI-generated insights, and links to visualizations.
- **Visualization (`missing_values.png`)**: Shows missing values per column.

## Project Structure
```
|-- autolysis.py            # Main script
|-- requirements.txt        # List of dependencies
|-- README.md               # Generated report (output)
|-- missing_values.png      # Generated visualization (output)
```

## Key Components
- **Step 1**: Load the API proxy token for OpenAI integration.
- **Step 2**: Detect encoding of the CSV file to handle diverse datasets.
- **Step 3**: Perform basic data analysis to generate column summaries, data types, and missing values.
- **Step 4**: Interact with the OpenAI GPT model to extract insights and suggestions.
- **Step 5**: Generate visualizations for better understanding of missing values.
- **Step 6**: Create a comprehensive Markdown report.

## Dependencies
The following libraries are required to run the project:
- `pandas`
- `matplotlib`
- `requests`
- `chardet`
- `openai`

Install them using:
```bash
pip install -r requirements.txt
```

## Future Improvements
- Expand visualization options to include histograms, scatter plots, and correlation heatmaps.
- Add support for more data formats (e.g., Excel, JSON).
- Provide an interactive user interface for selecting analysis options.
- Include a logging mechanism for better debugging and tracking.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

## Acknowledgments
Special thanks to OpenAI for their powerful GPT models and to the Python community for the amazing libraries used in this project.

## Problem Statment 
https://github.com/sanand0/tools-in-data-science-public/blob/tds-2024-t3/project-2-automated-analysis.md
