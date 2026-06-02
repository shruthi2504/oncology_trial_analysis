\# Oncology Trial Analysis



\## Overview



This project performs a basic analysis of an oncology clinical trial dataset. The objective was to inspect the raw data, perform simple cleaning, define a trial success metric, and calculate success rates across different groups.






\## Data Profiling



The dataset was loaded into a pandas DataFrame and inspected for:



\* Missing values

\* Unique value counts

\* Duplicate trial identifiers

\* Recruitment status distribution



The profiling step was used to understand data completeness and identify potential data quality issues.





\## Data Cleaning



The following cleaning steps were performed:



\* Standardized column names

\* Converted recruitment status values to lowercase

\* Extracted numeric values from phase information

\* Converted date columns to datetime format

\* Created derived fields for analysis



\### Derived Fields



\* \*\*start\_year\*\*: Year extracted from the trial start date

\* \*\*duration\*\*: Number of days between start date and completion date





\## Success Definition



The dataset does not contain a direct measure of clinical success.



For this analysis, a trial was considered successful if:



\* Recruitment Status = \*\*Completed\*\*



All other statuses were treated as non-successful.



This metric should be interpreted as a trial completion metric rather than evidence of therapeutic or regulatory success.





\## Cohort Analysis



Success rates were calculated across the following dimensions:



\* Trial Phase

\* Indication

\* Start Year



Success Rate was calculated as:



Success Rate = Successful Trials / Total Trials





\## Limitations



Several limitations should be considered:



\* Trial completion does not necessarily indicate clinical success.

\* Regulatory outcomes are not available.

\* Clinical efficacy and safety results are not included in the dataset.

\* Some fields contain missing values.

\* Multi-valued indication and intervention fields were not further normalized.





\## Additional Data Needed



To define a more meaningful success metric, the following information would be useful:



\* Clinical efficacy outcomes

\* Safety outcomes

\* Endpoint achievement data

\* Regulatory approval status

\* Phase transition information





\## Repository Structure



```text

oncology-trial-analysis/

│

├── data/

│   └── raw\_data.xlsx

│

├── script.py

├── README.md

└── cleaned\_data.csv

```



\## Running the Code



Install dependencies:



```bash

pip install pandas openpyxl

```



Run the analysis:



```bash

python script.py

```



Output:



\* Data quality summary in the console

\* Success rate calculations

\* cleaned\_data.csv



