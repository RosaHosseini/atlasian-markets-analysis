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
    'Accept-Language': 'en-US,en;q=0.9',
    "cookie": 'atl_xid.xc=%7B%22value%22%3A%227f5f25db-85c4-4985-a047-d6372cf6e205%22%2C%22type%22%3A%22xc%22%2C%22createdAt%22%3A%222020-08-29T11%3A43%3A53.531Z%22%7D; seg_xid=d4f6494e-39ef-4149-8a27-0d8bad1ecc7b; _ga=GA1.2.2091943045.1605742566; _gid=GA1.2.1636037616.1605742566; optimizelyEndUserId=oeu1605742566605r0.7463449065117089; ajs_anonymous_id=%2296b1b3ce-936d-49f1-b7d7-4fa64a3d8266%22; atlCohort={"bucketAll":{"bucketedAtUTC":"2020-11-18T23:36:09.516Z","version":"2","index":46,"bucketId":0}}; atl_xid.ts=1605742569826; atl_xid.current=%5B%7B%22type%22%3A%22uid%22%2C%22value%22%3A%22d8d7c149f25b11e1ab68b544bc089490%22%2C%22createdAt%22%3A%222020-11-18T23%3A36%3A09.826Z%22%7D%5D; ajs_anonymous_id=%2296b1b3ce-936d-49f1-b7d7-4fa64a3d8266%22; atlUserHash=1393648548; _gcl_au=1.1.505229391.1605742570; _sio=96b1b3ce-936d-49f1-b7d7-4fa64a3d8266; _fbp=fb.1.1605742571655.757976353; OptanonAlertBoxClosed=2020-11-18T23:37:02.819Z; km_ai=CFz2rXEuhng%2BOX3aAg9W6Np6PRw%3D; _cs_c=1; _CT_RS_=Recording; WRUIDAWS=3042143626952764; atl_session=f4b55d37-4b77-4d36-8971-32fb679d9551; __insp_wid=1157084781; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9tYXJrZXRwbGFjZS5hdGxhc3NpYW4uY29tL3NlYXJjaD9jYXRlZ29yeT1UaW1lJTIwdHJhY2tpbmcmcHJvZHVjdD1qaXJh; __insp_targlpt=VGltZSB0cmFja2luZyBhcHBzIHwgQXRsYXNzaWFuIE1hcmtldHBsYWNl; __insp_norec_sess=true; km_vs=1; km_lv=x; ajs_group_id=null; __insp_slim=1605816479759; _cs_id=5f7e6469-4003-a5a1-e841-540a932c47d9.1605747690.2.1605816483.1605816359.1.1639911690769.Lax.0; _cs_s=2.1; kvcd=1605816484348; __CT_Data=gpv=7&ckp=tld&dm=atlassian.com&apv_45_www33=7&cpv_45_www33=7&rpv_45_www33=6; _gat=1; OptanonConsent=landingPath=NotLandingPage&datestamp=Thu+Nov+19+2020+23%3A39%3A52+GMT%2B0330+(Iran+Standard+Time)&version=4.3.3&EU=false&groups=0_144275%3A1%2C101%3A1%2C1%3A1%2C2%3A1%2C103%3A1%2C0_144389%3A1%2C105%3A1%2C3%3A1%2C0_145087%3A1%2C112%3A1%2C0_145849%3A1%2C4%3A1%2C113%3A1%2C0_146519%3A1%2C125%3A1%2C0_147366%3A1%2C126%3A1%2C0_149658%3A1%2C127%3A1%2C0_150360%3A1%2C128%3A1%2C0_150361%3A1%2C131%3A1%2C0_152586%3A1%2C134%3A1%2C0_177825%3A1%2C0_144574%3A1%2C0_145089%3A1%2C0_147243%3A1%2C0_147316%3A1%2C0_147317%3A1%2C0_147320%3A1%2C0_147327%3A1%2C0_150364%3A1%2C0_150452%3A1%2C0_151725%3A1%2C0_151744%3A1%2C0_151754%3A1%2C0_155093%3A1%2C0_152355%3A1%2C0_147367%3A1%2C0_162785%3A1%2C0_148475%3A1%2C0_154648%3A1%2C0_147315%3A1%2C0_154645%3A1%2C0_155091%3A1%2C0_142671%3A1%2C0_154646%3A1%2C0_155092%3A1%2C0_150368%3A1&AwaitingReconsent=false; _gat_p6572=1'
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
