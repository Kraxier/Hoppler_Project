# Metro Manila Property Data Extraction


## Project Overview:
Automating the process of collecting property information from Hoppler, a popular real estate platform in the Philippines, specifically targeting listings within Metro Manila, including Makati, Taguig, Muntinlupa, Pasig, and Las Piñas City, to extract data such as property name, price, URL, area size, number of bedrooms, bathrooms, parking spaces, property status, and the date of data extraction.

## Set Up Instructions 
1. Clone or Download this repository
2. Open Powershell 
3. Navigate to the repository directory in PowerShell
4. Activate the VENV $ .\hoppler_venv\Scripts\Activate
5. Install the Scrapy Libraries $pip install -r requirements.txt
6. Run the Projects $ scrapy crawl <your_project_name>

## Usage

1. Market Pricing Analysis
Goal: Understand average property prices in each city and observe price trends. Calculating the average,median and range of prices per city and property type
2. Size vs Price Analysis 
Goal: Analyzing the price per square meter and its variations across cities
    * Divide property prices by area size to obtain price per square meter.
    * Compare these ratios across different cities and neighborhoods.
    * Graph the price per square meter to identify cities or areas where prices may be over- or under-valued.

3. Feature-Based Analysis
Goal: Identify how various features (bedrooms, bathrooms, parking) affect property prices.
4. Time-Based Analysis
Goal: Examine how property listings and prices change over time.
5. Location-Specific Demand Analysis
Goal: Identify high-demand areas based on availability and pricing trends

## Future Improvements 
1. Proper Cleaning the Data 
    removing this part: "â€¢"
    Implementing Pipelines and Item 
2. Scrapping the Hoppler Broker Agents and Contact Details 
3. Scrapping the Images ( Optionals)
4. Implementing the The Rate of Scrapping it to not Overload the Websites