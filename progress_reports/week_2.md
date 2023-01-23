# Practicum 1 (23S8W1) Progress Report
## Stability Review of Cooling Waterbox Settings in Steel Wire Rod Rolling Mill
NAME: Bryce Lakamp

GITHUB REPOSITORY LINK: https://github.com/0xFFMobius/PracticumWaterboxes

WEEK: 2

## Project Summary
Through a review of 18 months of historical data, it is desired to explore, understand and develop a model which can be used to optimize usage parameters for operational control of cooling waterboxes. Operators currently have full control of waterbox selection, flow rates and water distribution. They are only required to achieve the desired output temperatures at the end of the process within a tolerance. Best practices to achieve these temperatures have not been defined. An optimized model would ideally improve process stability, and lead to best practices. Small perturbations of the input parameters, would result in minimum disruption of the output parameters. 

Supervised regression models using time series averaged flow utilization and waterbox selection can be compared for both accuracy of prediction and stability. There are numerous input factors of both continuous and categorical types. The final output is is the product temperature. Predictability and stability of the output temperature is key to determining process set points. 

## Milestones
* ~~Generate Project Proposal~~ (Done)
* ~~Validate data availability~~ (Done)
* ~~Data retrieval and source merging~~ (Done)
  * Three sources merged together
* ~~Save merged data to local system~~ (Done)
To Do:
* Data review
* Data cleaning
* Deduplication
* EDA
* If subsetting necessary, which are most representative categorical values
* Distributions
* Correlations
* Feature selection for machine learning
* Additional exploration as needed
* Self teach SVM refresh applicable to regression
* Self teach decision trees & applicability to regression
* Model development
  * Hyper parameter optimization
* Visualizations
* Generation of final presentation