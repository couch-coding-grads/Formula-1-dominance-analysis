# Formula 1 Dominance Analysis

This is project aims to allow a visual analysis of an F1 team's "dominance" or competitiveness. It achieves this by querying and manipulating large race results datasets across the years, calculating relative points scoring, and displaying this on a scatter plot with some additional statistics.

This is a project by Taha Majid and Paresh Dokka. The basic idea started with a simple linear R script that was written a few years ago for a Sports Economics essay analysing competitive balance in F1. It used points scored by a team in races to illustrate their dominance, and we've decided to build this idea in Python and flesh it out into a program to allow more custom visualisations, features, and an actual interface.

![old R script example output visualisation](docs/old%20R%20export%20percpoints.jpg)

# Development

## Usage & Design

The usage of the program is simple and straight forward- for a given range of years and team, the program will generate a viusalisation of the teams performance through the years. The data needed by the script is contained in `/data`- it is a full copy of the Ergast datasets up till the end of 2024.

We also wanted to create a more friendly (graphical) interface for the program- this is done via Gradio. We hope to adapt the regular analysis functions into a Gradio web UI, with a concept for the design given below.

![pic of gr interface concept 2](docs/gr%20interface%20concept%202.png)

## Features

This is the current map of features for the project:

- Data Manipulation
    - [x] Dataset Querying
    - [ ] Time-mapping variable
    - [ ] Input Validation
    - [ ] Identification system for Sprints, different point systems, anomalies

- Analysis
    - [ ] Point calculations
    - [ ] High quality visualisations
    - [ ] (Bonus) Any descriptive statistics

- Gradio Web Interface
    - [ ] Build UI Skeleton
    - [ ] Adapt Dominance Analysis function for Gradio version
    - [ ] Get fully fleshed plot window working
    - (Bonus) Additional validation elements for bug-free running/ QoL

- Further features
    - [ ] Constructors top standings variation plot (separate tab?)
    - [ ] Github installation and environment setup instructions (YAML file)
    - [ ] For fun: Laptime telemetry expansion

### For Developers
- For those interested, `/data` also has files to guide you, should you wish to use the data yourself.

## Considerations

- ErgastAPI is being deprecated and moving to [Jolpica F1](https://github.com/jolpica/jolpica-f1). The `/data` folder currently holds a physical/local copy of the Ergast datasets used for the analysis, which go up till the end of the 2024 season.

    To keep the datasets continuously up-to-date with future F1 seasons would require us to move to an API implementation. For now, we have opted not to focus on this. This is because our project naturally has to manipulate very large amounts of data, and we are unsure of rate limits for the API and what that will mean for how the program requests all of this data.

# Acknowledgments
- ErgastAPI for the incredibly thorough historical datasets