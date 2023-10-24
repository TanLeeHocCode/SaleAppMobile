def read_catesgory():
    return [{
            'id': 1,
            'name': "Iphone"},
        {
            'id': 2,
            'name': "Ipad"},
        {
            'id': 3,
            'name': "Sam sung"},
        {
            'id': 4,
            'name': "Canon"},
    ]

def read_products(kw):
    products= [{
            'name': "Iphone 13",
            'price': "17.300.000",
            'image':"https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-13_2_.png"
    },
        {
            'name': "Ipad 4.5 Pro",
            'price': "12.630.000",
            'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/x/_/x_mmas.png"
        },
        {
            'name': "Zplit 3",
            'price': "11.530.000",
            'image': "https://didongmoi.com.vn/upload/images/product/samsung/samsung-galaxy-z-flip5-gia-re-2.jpg"
        },
        {
            'name': "Zplit 3",
            'price': "11.530.000",
            'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/m/a/may-anh-canon-powershot-g7-x-mark-iii-1.png"
        },

    ]
    if kw:
        products = [p for p in products if p['name'].find(kw)>=0]

    return products



