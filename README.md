# Scraping logos

## Dependencies

### UV 
https://github.com/astral-sh/uv


### NU

https://www.nushell.sh/


## Config
Create a .env file with API_LOGO = "XXXXXX"

Two files, content.json and record.json.
content.json -> fill with a list of objects in this format


```json
    {'ISIN':'XXXXX', 'SYMBOL':'APPL', 'name':'APPLE', 'website': 'https://www.nestle.com'}
```

## Start
Go to the folder

`cd logo`

Initialize environment and dependencies

`uv sync`

Once the content.json config is filled, run this command to clean out duplicates

`nu clean_content.nu`

Run the script

`uv run main.py`
