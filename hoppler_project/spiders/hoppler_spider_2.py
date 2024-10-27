import scrapy
from datetime import datetime

class HopplerSpider(scrapy.Spider):
    name = "hoppler_spider"
    allowed_domains = ["www.hoppler.com.ph"]
    start_urls = [
        # Scrapping Some Location in Metro Manila in a Hoppler Website

        # Scrapping the Makati Location 
        "https://www.hoppler.com.ph/condominiums-for-sale/makati",
        "https://www.hoppler.com.ph/house-and-lots-for-sale/makati",
        "https://www.hoppler.com.ph/townhouses-for-sale/makati",
        "https://www.hoppler.com.ph/commercial-lots-for-sale/makati",
        "https://www.hoppler.com.ph/office-spaces-for-sale/makati",
        "https://www.hoppler.com.ph/warehouses-for-sale/makati",
        "https://www.hoppler.com.ph/buildings-for-sale/makati",
        "https://www.hoppler.com.ph/industrial-lots-for-sale/makati",
        "https://www.hoppler.com.ph/resorts-for-sale/makati",

        # Scrapping the Taguig Location 
        "https://www.hoppler.com.ph/condominiums-for-sale/taguig",
        "https://www.hoppler.com.ph/house-and-lots-for-sale/taguig",
        "https://www.hoppler.com.ph/townhouses-for-sale/taguig",
        "https://www.hoppler.com.ph/commercial-lots-for-sale/taguig",
        "https://www.hoppler.com.ph/office-spaces-for-sale/taguig",
        "https://www.hoppler.com.ph/warehouses-for-sale/taguig",
        "https://www.hoppler.com.ph/buildings-for-sale/taguig",
        "https://www.hoppler.com.ph/industrial-lots-for-sale/taguig",
        "https://www.hoppler.com.ph/resorts-for-sale/taguig",

        # Scrapping the Las Pinas Location 
        "https://www.hoppler.com.ph/condominiums-for-sale/las-pinas",
        "https://www.hoppler.com.ph/house-and-lots-for-sale/las-pinas",
        "https://www.hoppler.com.ph/townhouses-for-sale/las-pinas",
        "https://www.hoppler.com.ph/commercial-lots-for-sale/las-pinas",
        "https://www.hoppler.com.ph/office-spaces-for-sale/las-pinas",
        "https://www.hoppler.com.ph/warehouses-for-sale/las-pinas",
        "https://www.hoppler.com.ph/buildings-for-sale/las-pinas",
        "https://www.hoppler.com.ph/industrial-lots-for-sale/las-pinas",
        "https://www.hoppler.com.ph/resorts-for-sale/las-pinas",

        # Scrapping the Muntin Lupa Location 
        "https://www.hoppler.com.ph/condominiums-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/house-and-lots-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/townhouses-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/commercial-lots-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/office-spaces-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/warehouses-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/buildings-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/industrial-lots-for-sale/muntinlupa",
        "https://www.hoppler.com.ph/resorts-for-sale/muntinlupa",

        # Scrapping the Pasig Location 
        "https://www.hoppler.com.ph/condominiums-for-sale/pasig",
        "https://www.hoppler.com.ph/house-and-lots-for-sale/pasig",
        "https://www.hoppler.com.ph/townhouses-for-sale/pasig",
        "https://www.hoppler.com.ph/commercial-lots-for-sale/pasig",
        "https://www.hoppler.com.ph/office-spaces-for-sale/pasig",
        "https://www.hoppler.com.ph/warehouses-for-sale/pasig",
        "https://www.hoppler.com.ph/buildings-for-sale/pasig",
        "https://www.hoppler.com.ph/industrial-lots-for-sale/pasig",
        "https://www.hoppler.com.ph/resorts-for-sale/pasig"


    ]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'Metro_Manila_Hoppler.csv',

    }

  
    property_count = 0

    def parse(self, response):
        properties = response.css('.hi-results-page__results-column.mb-3.col-md-6.col-lg-6.col-xl-4')
        
        for property in properties:
            relative_url = property.css('.hi-type-title.hi-property-card__title::attr(href)').get()

            # Extract the property type and location
            property_type_location = property.css('.hi-property-card__type-loc::text').get()

            if relative_url is not None:
                yield response.follow(
                    relative_url,
                    callback=self.parse_property_page,
                    meta={'property_type_location': property_type_location}
                )

        next_page = response.css('ul.pagination li.page-item a.page-link[aria-label="Next"]::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_property_page(self, response):
       
        property_type_location = response.meta.get('property_type_location')

        values = response.xpath('//div[@class="hi-listing-page__key-stats__stat"]/text()').getall()
        cleaned_values = [value.strip() for value in values if value.strip()]

       
        numeric_values = [value for value in cleaned_values if value.isdigit()][:3]
        num_bedrooms, num_bathrooms, num_parking = (numeric_values + [None, None, None])[:3]

       
        area = next((value for value in cleaned_values if "sqm" in value), None)
        furnishing = next((value for value in cleaned_values if "Furnished" in value), None)

        
        self.property_count += 1

        
        current_date = datetime.now().strftime('%Y-%m-%d')

        yield {
            'property_type_location': property_type_location,
            'Property': response.css('.col-12.hi-type-caption.mt-1 span::text').get(),
            'price': response.css('.hi-listing-page__price::text').get(),
            'relative_url': response.url,
            'property_status': response.xpath('//div[div[@class="hi-listing-page__status-item__label" and text()="Status"]]/div[@class="hi-listing-page__status-item__data"]/text()').get(),
            'last_updated': response.xpath('//div[div[@class="hi-listing-page__status-item__label" and text()="Last Updated"]]/div[@class="hi-listing-page__status-item__data"]/text()').get(),
            'num_bedrooms': num_bedrooms,
            'num_bathrooms': num_bathrooms,
            'num_parking': num_parking,
            'area': area,
            'furnishing': furnishing,
            'counting': self.property_count,
            'scraped_date': current_date  
        }
