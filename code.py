import undetected_chromedriver as uc
from a_pandas_ex_css_selector_from_html import pd_add_css_selector_from_html
pd_add_css_selector_from_html()

import pandas as pd

if __name__ == "__main__":
    driver = uc.Chrome(
    )
    driver.get(r"https://testpages.herokuapp.com/styled/tag/table.html")
    df = pd.Q_selector_from_html(driver.page_source, parser="html.parser", ignore_tags=("html", "body"))
    print(df)
    
