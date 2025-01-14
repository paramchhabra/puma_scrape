import requests
from rich import print
import json


def create_session():
    with open('essentials.json', 'r') as f:
        data = json.load(f)
        cookies = data['cookies']  
        headers = data['headers']
        f.close()
    

    proxy = "http://bab9fae56e593e516aac:ff79e32368110bf2@gw.dataimpulse.com:823"
    proxies = {"http":proxy, "https":proxy}

    session = requests.Session()
    session.headers.update(headers)
    session.cookies.update(cookies)
    session.proxies.update(proxies)

    return session

def generate_data(id,count,session):
    json_data = {
        'operationName': 'PDP',
        'query': 'query PDP($id: ID!) {\n  product(id: $id) {\n    ...mandatoryMasterFields\n    description\n    primaryCategoryId\n    productDivision\n    brand\n    sizeChartId\n    promotions(page: ProductDetailsPage) {\n      id\n      calloutMessage\n      __typename\n    }\n    promotion {\n      id\n      calloutMessage\n      __typename\n    }\n    configureID {\n      enabled\n      productID\n      __typename\n    }\n    productStory {\n      longDescription\n      careInstructions\n      productKeywords\n      __typename\n    }\n    productVideos\n    verticalProductVideos\n    promotionExclusion\n    exploreMoreCTALabel\n    showExploreCollectionCTA\n    exploreMoreCTATargetCategoryID\n    brand\n    orderable\n    badge\n    ...sizes\n    fitOptions {\n      label\n      masterProduct {\n        id\n        name\n        variations {\n          id\n          colorValue\n          orderable\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    variations {\n      ...pdpMandatoryVariantFields\n      isFinalSale\n      returnRuleID\n      promotionExclusion\n      specialMessage\n      ean\n      validUntil\n      isAppExclusive\n      badges {\n        id\n        label\n        __typename\n      }\n      percentageDiscountBadge\n      salePrice\n      productPrice {\n        price\n        salePrice\n        promotionPrice\n        isSalePriceElapsed\n        __typename\n      }\n      styleNumber\n      materialComposition\n      displayOutOfStock {\n        soldout\n        soldoutWithRecommender\n        comingsoon\n        backsoon\n        presale\n        displayValue\n        validTo\n        __typename\n      }\n      orderable\n      modelMeasurementText\n      manufacturerInfo {\n        manufacturerAddress {\n          label\n          content\n          __typename\n        }\n        countryOfOrigin {\n          label\n          content\n          __typename\n        }\n        __typename\n      }\n      myCustomizer {\n        enabled\n        iframeID\n        startPoint\n        __typename\n      }\n      configureID {\n        enabled\n        productID\n        __typename\n      }\n      taxDisplayMsg\n      promotions(page: ProductDetailsPage) {\n        id\n        calloutMessage\n        __typename\n      }\n      appOnlyDateTimeFrom\n      appOnlyDateTimeTo\n      __typename\n    }\n    __typename\n  }\n}\nfragment mandatoryMasterFields on Product {\n  name\n  id\n  header\n  subHeader\n  orderableColorCount\n  displayOutOfStock {\n    soldout\n    soldoutWithRecommender\n    comingsoon\n    backsoon\n    presale\n    displayValue\n    __typename\n  }\n  colors {\n    name\n    value\n    image {\n      href\n      verticalImageHref\n      alt\n      __typename\n    }\n    __typename\n  }\n  image {\n    href\n    verticalImageHref\n    alt\n    __typename\n  }\n  showExploreCollectionCTA\n  __typename\n}\nfragment sizes on Product {\n  productMeasurements {\n    metric\n    imperial\n    __typename\n  }\n  __typename\n}\nfragment pdpMandatoryVariantFields on Variant {\n  id\n  masterId\n  variantId\n  name\n  header\n  subHeader\n  price\n  colorValue\n  colorName\n  ean\n  preview\n  images {\n    alt\n    href\n    verticalImageHref\n    __typename\n  }\n  __typename\n}',
        'variables': {
            'id': id,
        },
    }

    response = session.post('https://in.puma.com/api/graphql', json=json_data)

    name = response.json()['data']['product']['name']
    price =  response.json()['data']['product']['variations'][0]['salePrice']
    return f"{count}. {name}, {price}"
    



