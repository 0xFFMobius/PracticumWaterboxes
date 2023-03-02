# Practicum 1 (23S8W1) Progress Report
## Stability Review of Cooling Waterbox Settings in Steel Wire Rod Rolling Mill
NAME: Bryce Lakamp

GITHUB REPOSITORY LINK: https://github.com/0xFFMobius/PracticumWaterboxes

WEEK: 5

## Project Summary
Through a review of 18 months of historical data, it is desired to explore, understand and develop a model which can be used to optimize usage parameters for operational control of cooling waterboxes. Operators currently have full control of waterbox selection, flow rates and water distribution. They are only required to achieve the desired output temperatures at the end of the process within a tolerance. Best practices to achieve these temperatures have not been defined. An optimized model would ideally improve process stability, and lead to best practices. Small perturbations of the input parameters, would result in minimum disruption of the output parameters. 

Supervised regression models using time series averaged flow utilization and waterbox selection can be compared for both accuracy of prediction and stability. There are numerous input factors of both continuous and categorical types. The final output is is the product temperature. Predictability and stability of the output temperature is key to determining process set points. 

## Milestones
* ~~Generate Project Proposal~~ (Done)
* ~~Validate data availability~~ (Done)
* ~~Data retrieval and source merging~~ (Done)
  * Three sources merged together
* ~~Save merged data to local system~~ (Done)
* Initial cleaning
  * ~~Removal of physically impossible values~~ (Done)
  * ~~Removal of duplicate index values (coil ID) based on recording time~~ (Done)
  * ~~Determining combination of waterboxes used~~ (Done)
  * ~~Deduplication~~ (Done)
* ~~Data review~~ (Done)
  * ~~Outlier reviews~~ (Done)
* EDA 
  * ~~Descriptive statistics~~ (Done)
  * ~~One dimensional distribution, and compared by product size~~ (Done)
  * ~~Correlation determinations~~
  * ~~If subsetting necessary, which are most representative categorical values~~ (Done)
  * ~~Distributions~~ (Done)
  * ~~Correlations~~ (Done)
* ~~Feature selection for machine learning~~ (Done)
* ~~Linear regression~~ (Done)
  * ~~Train test separately~~ (Done)
  * ~~Overall review (all selection configurations)~~ (Done)
  * ~~Comparison to singular selection configurations~~ (Done)
  * ~~Assumptions of linear regression review~~ (Done)
* Applied SVM (SVR) to data sets
  * ~~Reviewed applicablity to non-linear regression data~~ (Done)
  * ~~Optimized hyper parameters using grid search~~ (Done)
  * ~~Reperformed multi tier comparison ~~ (Done)
    * ~~Narrowed down scope of inspection~~
* ~~Compared Non-linear to SVR based on coefficient of determination and mean square error for best models.~~ (Done)
  * ~~Determined best models given single and multiple size product schedules~~ (Done)
* ~~Correct training and testing callout, rerun models~~ (Done)
* ~~Generate method to evaluate optimized settings~~
  * ~~Generate and use predictive models for flow and pressure versus valve opening~~ (Done)
To Do:
* Create final visualization of optimial settings
* Code and comments clean up
* Generat final presentation