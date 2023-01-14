# Effects of Waterbox utilization
In completion of the requirements for M.S. Data Science, Data Engineering emphasis I present a review of waterbox utilization, and use of machine learning to generate recommendations for future manufacturing set up.

# Background
Steel mills use waterboxes to control product temperatures during manufacturing.
<details><summary>Steel Mill Characteristics</summary>
I currently work at a steel mill which produces steel wire rod. The product is sold in 5000 lb packages, in a coils configuration. Rod diameters range from 7/32" to 3/4" diameter. Multiple grades (chemistries) are produced to meet a variety of end use applications. 
</details>
<details>
<summary> What is a Waterbox?</summary>
A waterbox is component used to cool wire rod during manufacture. After hot steel rod is rolled to final size, it is cooled to a target temperature to assist in meeting final mechanical properties. The rod flows through a waterbox at high speed, and is subjected to a continuous flow of water at pressure. 
</details>
<details>
<summary>How are Waterboxes used?</summary>
At the subject steel mill, there are five waterboxes which may be used in multiple configurations to achieve final temperature. There are multiple settings for each waterbox which can be adjusted to affect the product. This includes flow rates and pressures. There are three different bore diameters in the cooling nozzles which also affect the relationship between the water flow rate and pressure. For each box there are three zones which can be turned on and off, further changing the water's contact length to the product. 
</details>

# Research Problem
To achieve desired final temperatures, operators can set values for many factors affecting the waterbox performance. The selection of these parameter values is currently a judgement call by the operators. By using machine learning on historical data, I want to develop a model which can set guildline values for the operators to use in future practices. 

# Available data
A data historian is currently used at the Rod mill which captures 3k+ signals from sensors at a poll rate of 16 ms. For the waterboxes, water flow rates, pressures and resulting surface temperatures are all recorded. Several categorical variables representing product descriptors are also available including grades, diameters, and desired final temperature. 

Millisecond data for continuous variables have been aggregated using industrial tools and saved to a SQL database. Aggregation frequency is grouped to each coil produced. 

This data has been sanitized of confidential information.

# 
