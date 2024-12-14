import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None: 
    browser = playwright.chromium.launch(headless=False) # Change to True for no browser
    context = browser.new_context() # Incognito mode
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/") # Go to the Tully's menu page


    extracted_items = []
    for title in page.query_selector_all("h3.foodmenu__menu-section-title"): # Loop through each menu section
        title_text = title.inner_text().strip() # Get the menu section title
        print(f"MENU SECTION: {title_text}") # Print the menu section title

    row = title.query_selector("~ *").query_selector("~ *") # Get the next sibling of the title
    for item in row.query_selector_all("div.foodmenu__menu-item"): # Loop through each menu item
        item_text = item.inner_text().strip()   # Get the menu item text
        extracted_item = extract_menu_item(title_text, item_text)   # Extract the menu item
        print(f"  MENU ITEM: {extracted_item.name}")  # Print the menu item name
        
        extracted_items.append(extracted_item.to_dict()) # Append the extracted item to the list

        df = pd.DataFrame(extracted_items)
        df.to_csv("cache/tullys_menu.csv", index=False)


        context.close()
        browser.close()



with sync_playwright() as playwright:
    tullyscraper(playwright)
