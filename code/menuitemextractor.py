if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    price =price.replace (",", "") # remove comma
    price = price.replace ("$", "") # remove dollar sign
    return float(price)

def clean_scraped_text(scraped_text: str) -> list[str]:
    items = scraped_text.split("\n") # split the text into lines
    cleaned = []
    for item in items:
        if item in ['GS',"V","S","P"]: # skip these items
            continue
        if item.startswith("NEW"): # skip these items
            continue
        if len(item.strip()) == 0: # skip empty lines
            continue

        cleaned.append(item)
    
    return cleaned

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    cleaned_items = clean_scraped_text(scraped_text)
    item = MenuItem(category=title, name="", price=0.0, description="")
    item.name = cleaned_items[0]
    item.price = clean_price(cleaned_items[1])
    if len(cleaned_items) > 2:
        item.description = cleaned_items[2]
    else:
        item.description = "No description available."
    return item



if __name__=='__main__':
    test_items = []
    title = "test"
    for scraped_text in test_items:
        item = extract_menu_item(title, scraped_text)
        print(item)