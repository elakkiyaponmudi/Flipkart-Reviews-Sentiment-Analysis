**Flipkart Product Reviews Analysis and Recommendation System**

**Project Overview**

The goal of this project is to develop an automated system for collecting and analyzing product reviews from Flipkart. By leveraging web scraping techniques and sentiment analysis, the project aims to generate data-driven product recommendations. The project involves the following key tasks:

**Key Tasks**

**Web Scraping**: Extract product reviews from Flipkart, focusing on various product categories such as electronics, clothing, and home appliances.

**Data Cleaning and Structuring**: Process and structure the scraped data to ensure it is suitable for analysis.

**Sentiment Analysis**: Determine the overall customer sentiment (positive, negative, neutral) for each product based on the collected reviews.

**Product Recommendation**: Recommend top products in each category using the results of the sentiment analysis.

**Visualization and Reporting**: Create visual representations of the data and compile a comprehensive report detailing the analysis process, findings, and recommendations.

**Business Use Cases**

**E-commerce Platforms:** Enhance product recommendation engines by incorporating sentiment analysis of customer reviews.

**Market Research Firms:** Analyze consumer sentiment towards various products to inform business strategies.

**Retail Companies**: Monitor customer feedback to improve product offerings and customer satisfaction.

**Business Intelligence Tools**: Integrate with dashboards to provide real-time insights on product performance based on customer reviews.

**Approach**

**Data Collection**

**Tools Used**: Selenium

**Target Website**: Flipkart product pages (strictly live pages)

Products: Comparison of 5 mobile phones in the price range between Rs 20000 to 40000

**Data Cleaning and Structuring**

**Tools Used: Pandas**

**Preprocessing Steps**:

Remove HTML tags from review texts.

Convert ratings to a standard scale.

Tokenize and normalize review texts for sentiment analysis.

Sentiment Analysis

**Tools Used**: Autocorrect

**Output**: Sentiment Score (positive, negative, neutral) for each review

**Product Recommendation**

**Tools Used**: LangChain

**Methodology**: Generate product recommendations based on sentiment analysis results

**Visualization and Reporting**

**Tools Used**: Matplotlib, Seaborn, Power BI

**Output**: Visualizations (graphs, charts) depicting sentiment distribution and product recommendations, and a detailed report summarizing the approach, analysis, and recommendations.

**Results**

**Dataset**: Scraped reviews from Flipkart

**Sentiment Analysis**: Sentiment scores indicating the sentiment of each review

**Recommendations**: List of recommended products based on sentiment analysis

**Visualizations**: Graphs and charts depicting sentiment distribution and product recommendations

**Report**: Comprehensive report of the findings and recommendations

**Final Deployment in AWS using EC2**

**Prerequisites**
AWS Account
AWS CLI configured
EC2 Instance (Ubuntu)

**Conclusion**

This project provides a comprehensive approach to collecting and analyzing product reviews from Flipkart to generate data-driven product recommendations. By following the outlined steps, users can efficiently collect and process large volumes of data, apply sentiment analysis to understand customer opinions, and generate actionable insights and recommendations.
