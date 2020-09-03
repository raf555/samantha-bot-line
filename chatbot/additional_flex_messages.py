# to get image from a google drive link use:
# https://docs.google.com/uc?id=[id]


def whats_sop_kru(option):
    '''
    returns a carousel made of whatsop kru page images.
    the option argument should be either 1 or 2, 1 for the first half and 2 for the second part
    '''

    content = []

    if option == 1:
        # page 1 to 9
        urls_whatsop_kru = [
            'https://docs.google.com/uc?id=17MVEY6IiVahD3UcyfwUBxPPtevVAsp4X',
            'https://docs.google.com/uc?id=1H9TlGZK7tLkWMdQhaYpsUaOHkNJAUmU3',
            'https://docs.google.com/uc?id=1YK-hkXDJREcax8qeRxuVd9g0rGVb4RXP',
            'https://docs.google.com/uc?id=1ookWa_zH6v2Ycqmd9a-TtG_zyy5jq0TM',
            'https://docs.google.com/uc?id=159FHkRrjtuzNZUzCrsOabCTpkieYnCcS',
            'https://docs.google.com/uc?id=19lNO-k8okTlbKAPFkKs8HVDTVmgUmFai',
            'https://docs.google.com/uc?id=1jYK1YY2wcL4XYCLD_OUFQ8tuQocFt7zo',
            'https://docs.google.com/uc?id=11ssqsA09vH2P9XzzcyUFX3lSHxib1W54',
            'https://docs.google.com/uc?id=11ssqsA09vH2P9XzzcyUFX3lSHxib1W54'
        ]
    elif option == 2:
        # page 10 to 18
        urls_whatsop_kru = [
            'https://docs.google.com/uc?id=1-zx193hywcP_saIUrDgW5XmZFTqAv0uT',
            'https://docs.google.com/uc?id=1oQfdyHZtxuMFQGJOTegu-3PO3yhbb_zT',
            'https://docs.google.com/uc?id=1NZq7sZlgZ4v4SOQi3g4hps-ziAYQrad1',
            'https://docs.google.com/uc?id=1C2ywpYR7PgLOt23sg_gYxLBL9lQZ_5NW',
            'https://docs.google.com/uc?id=1smAoVEn_5rBPJF3ZiIsA8qGFEaiBa7pa',
            'https://docs.google.com/uc?id=1UiMjlS0TtNbQnqRPST95DpNh_pHu8Xfl',
            'https://docs.google.com/uc?id=1zXbFiWGgemXLnnFOZozSDDL_ikTAynV9',
            'https://docs.google.com/uc?id=1VdZojpUYGEOd_tzk3iB4INnRIb7W4By4',
            'https://docs.google.com/uc?id=14eNg0zyCCfyNpWYopq1Qlb0sw2owJqZZ',
            'https://docs.google.com/uc?id=1AD590n8j8yyku6aYtGQCVGB25OMRfN4C'
        ]

    for url in urls_whatsop_kru:
        content.append({
            "type": "bubble",
            "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "1:1.5",
                "aspectMode": "cover",
                "url": url
            }
        })

    carousel = {
        "type": "carousel",
        "contents": content
    }

    return carousel


def sukacita():
    content = []

    url = [
        'https://docs.google.com/uc?id=1NxBFgUD2wqOFUQtxmMBwFwyVn8iRNLoN',
        'https://docs.google.com/uc?id=1MnR1ZFlrJARivaLcorGcdqMT_4-AS8eG',
        'https://docs.google.com/uc?id=1I9lGdTCotzF92eyiz2U7UOW6c-ZAUBNg'
    ]

    for i in range(3):
        content.append({
            "type": "bubble",
            "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "url": url[i]
            }
        })

    carousel = {
        "type": "carousel",
        "contents": content
    }

    return carousel


def create_image_bubble(ratio, url):
    bubble = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "size": "full",
            "aspectRatio": ratio,
            "aspectMode": "cover",
            "url": url
        }
    }
    return bubble


def adhikarya():
    bubble = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "size": "full",
            "aspectRatio": "1:2",
            "aspectMode": "cover",
            "url": "https://docs.google.com/uc?id=16pYCPng607QvlNPj3V053ytw-bto7qZF"
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "spacing": "md",
            "contents": [{
                "type": "spacer",
                "size": "md"
            }, {
                "type": "button",
                "height": "sm",
                "action": {
                    "type": "uri",
                    "label": "Foto",
                    "uri": "https://drive.google.com/open?id=1Gi-7QspS8S8-USJyCk6lPhrDZjjHkGgo",
                },
                "style": "secondary",
                "color": "#F1F1F1",
                "flex": 2
            }, {
                "type": "button",
                "height": "sm",
                "action": {
                    "type": "uri",
                    "label": "Video",
                    "uri": "https://drive.google.com/open?id=1n0iAt1RULxpBLwyQj-LXxFu-t2_QIgbm",
                },
                "style": "secondary",
                "color": "#F1F1F1",
                "flex": 2
            }]
        }
    }

    return bubble