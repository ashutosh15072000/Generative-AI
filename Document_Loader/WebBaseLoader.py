from langchain_community.document_loaders import WebBaseLoader
url="https://www.flipkart.com/samsung-galaxy-s25-ultra-5g-titanium-whitesilver-256-gb/p/itm28d4275302a07?pid=MOBH8K8U56WRFZFR&lid=LSTMOBH8K8U56WRFZFRNVXGVH&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_bannerads_1_16.bannerAdCard.BANNERADS_Samsung%2BGalaxy%2BS25%2BUltra%2B5G_mobile-phones-store_Y3B2PF9GWBR5&fm=organic&iid=en_w5-F9jKijYPVw1ADY7D1Slm93Dgkp8VFRJLvkfhcquZkdUYHAKKETUIet5kma58AQDZjx1Gh4xSfnuagjAhqz_UFjCTyOHoHZs-Z5_PS_w0%3D&ppt=clp&ppn=mobile-phones-store&ssid=9ugbx8iky80000001743754551411"
loader=WebBaseLoader(url)
docs=loader.load()
print(docs)