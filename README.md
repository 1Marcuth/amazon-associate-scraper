# Amazon Affiliate - Scraper Tool

## Quickstart

### Creating Affiliate URL:

```py
from amazon_affiliate import AmazonAffiliate

def main():
    amazon_affiliate = AmazonAffiliate(
        cookies_file_path = "path/to/amazon_cookies.json", # Path to Amazon site cookies
        origin_url = "https://www.amazon.com.br/", # Amazon root URL in your country
        webdriver_file_path = "path/to/webdriver.exe", # Path to browser webdriver
        headless = True # If the browser will appear
    )

    # Create an affiliate URL like: https://amzn.to/3qAp1rZ
    affiliate_url = amazon_affiliate.create_affiliate_url("https://www.amazon.com.br/Introdu%C3%A7%C3%A3o-Programa%C3%A7%C3%A3o-com-Python-Algoritmos/dp/8575227181/?_encoding=UTF8&pd_rd_w=cLgOh&content-id=amzn1.sym.142cf30d-cd8e-4f67-a147-740799e27bf0&pf_rd_p=142cf30d-cd8e-4f67-a147-740799e27bf0&pf_rd_r=Q5SHBAZH69HSPBRR2MGS&pd_rd_wg=98FtW&pd_rd_r=ffa375c6-01c9-4e9c-9f87-2aef974a89af&ref_=pd_gw_ci_mcx_mr_hp_atf_m") 

    print(affiliate_url)

if __name__ == "__main__":
    main()
```