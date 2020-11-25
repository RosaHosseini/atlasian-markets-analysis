BASE_URL = "https://marketplace.atlassian.com/"

MARKET_PLACE_URL = "https://7lvr1jktdf-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%3B%20JS%20Helper%20(2.28.0)&x-algolia-application-id=7LVR1JKTDF&x-algolia-api-key=3ef48f0fc67ee7e9c5a9dbbf6b45908c"
MARKET_PLACE_HEADER = {
    'Connection': 'keep-alive',
    'accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://marketplace.atlassian.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://marketplace.atlassian.com/',
    'Accept-Language': 'en-US,en;q=0.9'
}

MARKET_PLACE_PARAMS = lambda page_number: {
    "requests": [
        {
            "indexName": "marketplace_plugins_prod",
            "params": f"query=&hitsPerPage=250&page={page_number}&attributesToRetrieve=%5B%22_highlightResult%22%2C%22addonId%22%2C%22addonKey%22%2C%22releaseDate%22%2C%22name%22%2C%22tagLine%22%2C%22categories%22%2C%22deployments%22%2C%22documentType%22%2C%22logo%22%2C%22vendor%22%2C%22distribution%22%2C%22version%22%2C%22ratings%22%2C%22marketingLabels%22%5D&facets=%5B%22version.supported%22%2C%22version.paid%22%2C%22version.stable%22%2C%22vendor.isAtlassian%22%2C%22vendor.isTopVendor%22%2C%22version.canonicalVersion%22%2C%22version.latestOfHosting%22%2C%22version.compatibilities.applicationKey%22%2C%22version.compatibilities.hosting%22%2C%22categories%22%2C%22marketingLabels%22%2C%22deployments%22%2C%22version.marketplaceType%22%2C%22hidden%22%5D&tagFilters=&facetFilters=%5B%22version.canonicalVersion%3Atrue%22%2C%5B%22categories%3ATime%20tracking%22%5D%2C%5B%22version.compatibilities.applicationKey%3Ajira%22%5D%2C%5B%22hidden%3AnotHidden%22%5D%5D"
        },
    ]
}

MARKET_URL = f"https://marketplace.atlassian.com/apps/"

MARKET_PLACE_PATH = "market_place.csv"

PRICE_URL = lambda host, addon_name: \
    f"https://marketplace.atlassian.com/rest/2/addons/{addon_name}/pricing/{host}/live?countryCode=NL"

REVIEW_URL = lambda add_on, host: \
    f"https://marketplace.atlassian.com/rest/1.0/plugins/{add_on}/reviews?offset=0&limit=5&hosting={host}"

# ------- colors ----------
blue = '#0081FF'
green = '#09B66D'
orange = '#FF8A48'
red = '#FF3D57'
teal_dark = '#004345'
teal_light = '#19979c'
