### Create A New Virtual Environment ###
[Command]
python3 -m venv venv


### Activate the virtual environment ###
[Command]
source venv/bin/activate


### Install requirements ###
pip3 install -r requirements.txt


### Run the crawler ###
``` First run ```
***Make sure you have to enable FEED_URI = "martindale_hrefs.csv" from settings.py file***
[Command]
scrapy crawl advocate


### Run the crawler ###
``` Secong run ```
***Make sure you have to enable FEED_URI = "FEED_URI = "martindale.csv"" from settings.py file***
[Command]
scrapy crawl advocate


### Lastly, Combined this file with Web Scrapping_Sample Records.xlsx ###
[Command]
python combined_data.py