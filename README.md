# Cinema Network Analysis

## Topic
This project explores the world of cinema, focusing on directors and their inspirations. It investigates the relationships and influences among US film directors based on their favorite films. \
Accompanied Medium article:\
[Network of Influence: How America’s Top Directors Inspire (and Connect) Each Other](https://medium.com/@yuri.ivaschenko/network-of-influence-how-americas-top-directors-inspire-and-connect-each-other-bbc02a6a6159)

## Data
The analysis is based on a survey conducted by the British Film Institute (BFI) as part of their Sight & Sound poll. Specifically, it uses data from the 2012 "Greatest Films of All Time" directors' poll, focusing on the votes of US directors.

## Research Question
What insights can be gained about movie inspirations and the roles of US directors within a network, based on their common favorite films? This project aims to reveal patterns and connections in the cinematic inspirations among US directors.

## Repository Structure & Usage
- `data/`: Contains the dataset used for analysis, including `US_Directors_favourite_movies.xls`.
- `images/`: Contains visual assets and output images.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and visualization, including `Movie_directors_network_US.ipynb`.
- `src/`: Source code modules and utilities for data processing and analysis.
- `requirements.txt`: Lists the Python dependencies required to run the project.
- `README.md`: This file, providing an overview of the project.

To use this repository:
1. Prepare a Python virtual environment.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the Jupyter notebooks in the `notebooks/` directory to explore the analysis.

## Prepare Virtual Environment
To set up the virtual environment, run the following commands:

```bash
python -m venv virt_env
virt_env\Scripts\activate  # On macOS/Linux use: source virt_env/bin/activate
pip install -r requirements.txt
```

## Contribution
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository to your own GitHub account.
2. Create a new branch for your analysis or bugfix:
   `git checkout -b your-branch-name`
3. Make your changes and commit them with clear, descriptive messages:
   `git commit -m "Brief description of your changes"`
4. Push your branch to your fork:
   `git push origin your-branch-name`
5. Open a pull request (PR) from your branch to the "main",
   and clearly describe the purpose and scope of your contribution.

Please ensure your code follows the existing style and includes appropriate tests where applicable.

---

This project aims to provide insights into the cinematic inspirations of US directors and foster further research and collaboration in the field of film studies.

