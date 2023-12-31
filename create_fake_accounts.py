from models import create_tables
from helpers import verify_signup
from queries import add_product_to_catalog, add_images_to_product, add_product_tags

##################################### users ##############################################
# possible to use any of these user details to log in, or create your own account

yuki = {
    "full_name": 'Yukine Masashi',
    "username": 'Yukiyuki_UwU',
    "password": 'BTSistheBest',
    "address": 'San Fransokyo 1234',
    "bio": "Hi i'm yuki, i'm 23 and i love crafting cute things. If you're into kawaii culture, unicorns, and love pink you're going to love my handcrafted goodies. Have a look at my shop, you won't regret it. Nyaaa :3",
    "avatar_url": '../static/images/yuki.jpg'
}

sam = {
    "full_name": 'Samantha Addams',
    "username": 'TheAddamsFamily',
    "password": 'sam.dams26',
    "address": 'The middle of nowhere 43',
    "bio": "Love relaxing at home with a good spell book, and deck of tarot cards. I'm a moon child and believe in the power of mysticism. Also love indulging into my more creepy fascinations every so often. If you like what you see, consider adding my store to your ghouly favorite list ",
    "avatar_url": '../static/images/sam.jpg'
}

alaska = {
    "full_name": 'Alaska Jones',
    "username": 'The.Lion.Queen',
    "password": 'RickIsA-Morty',
    "address": 'Brooklyntown 168',
    "bio": "Hey, welcome to my profile. I'm more of a collector of vintage items, than a creator. Though sometimes i enjoy making jewelry in my free time. I especially love crafting with gems and crystals. If you're into that sort of thing, you may want to keep an occasional eye on this profile ;)",
    "avatar_url": '../static/images/aska.jpg'
}


##################################### products ##############################################
# possible to edit, modify and update any of these products, or create your own

unicorn = {
    'title': 'Unicorn Plush Toy Handmade',
    'description': 'A soft sweet and cute friend to love and to hold at night when watching thriller movies',
    'price_in_cents': 542,
    'qty': 8,
    'vendor': yuki,
    'tags': ['unicorn', 'cute', 'sleep'],
    'images': ['https://media.istockphoto.com/id/1314268502/photo/unicorn-plush-toy-sitting-isolated-on-white-background.jpg?s=1024x1024&w=is&k=20&c=emALYMiNiQV6mogxErW-i6Vqrd579gkRdGpUd3CcJts=']*5
}

avocado_keychain = {
    'title': 'Cute Avocado Keychain Hanger',
    'description': "Not only are they fruity and healthy, now they'll also help you find your keys in the cutest manner possible. these advocado hangers are handmade from resin.",
    'price_in_cents': 129,
    'qty': 14,
    'vendor': yuki,
    'tags': ['avocado', 'cute', 'keychain'],
    'images': ['https://m.media-amazon.com/images/I/51grD6B2wlL._UL1024_.jpg']*3
}

cat_ears = {
    'title': 'Cat ears With Bell Cosplay Hair Accessory',
    'description': "Cats rule the world and now so can you! With these fluffy cotton cat eared hairbands you'll have all eyes on you",
    'price_in_cents': 581,
    'qty': 23,
    'vendor': yuki,
    'tags': ['cat', 'hair', 'cosplay'],
    'images': ['https://m.media-amazon.com/images/I/510gsYMmIVL._UL1000_.jpg']*3
}

earrings = {
    'title': 'Candy Earrings Cute and Funny Earing Gifts',
    'description': "These miniature food eaarings are not only cute to look at they were handcrafted using epoch resin and food coloring. These cute accessories look good enough to eat, and will make your style absolutely flavorful",
    'price_in_cents': 381,
    'qty': 5,
    'vendor': yuki,
    'tags': ['earrings', 'cute', 'candy', 'lolipop'],
    'images': ['https://i.ebayimg.com/images/g/2uUAAOSwQKlgctwU/s-l1600.jpg']*3
}

plush_bacpack = {
    'title': 'Bear Backpack Comfy Back To School',
    'description': "Oh my cuteness, is that a bear on your back? Not only is this soft cotton plushy bag un-dear-ably cute to look at, it's also spacious enough inside to carry your books and laptop with. ",
    'price_in_cents': 1793,
    'qty': 7,
    'vendor': yuki,
    'tags': ['bag', 'kawaii', 'pink'],
    'images': ['https://m.media-amazon.com/images/I/61x4z2-xurL._SL1200_.jpg']*4
}

sailor_skirt = {
    'title': 'Sailor Skirt Plaid Pink Skirt Harajuku',
    'description': "short and sexy, or sweet and kawaii? This soft pastel colored skirt is made from stretchy soft materials, making for a comfortable fit for any occassion ",
    'price_in_cents': 3751,
    'qty': 32,
    'vendor': yuki,
    'tags': ['skirt', 'plaid', 'sexy'],
    'images': ['https://www.kawaiifashionshop.com/wp-content/uploads/2021/12/QRWR-Summer-Women-Skirts-2020-New-Korean-High-Waist-Plaid-Mini-Skirt-Women-School-Girls-Sexy-2.jpg_640x640-2-600x600.jpg']*4
}

cosplay_wig = {
    'title': 'Cosplay Purple Pink Wig Sakura Erza Raven',
    'description': "A gorgeously colored purple and pink wig for your cosplaying neeeds. made with synthetic hair, that can withstand heat up to 250 degrees. It's durable versatile and a great addition for any cosplayer to have",
    'price_in_cents': 2080,
    'qty': 16,
    'vendor': yuki,
    'tags': ['cosplay', 'purple', 'wig', 'pink'],
    'images': ['https://cdn.ezcosplay.com/media/catalog/product/cache/f9d46a5c18731e4d94b61c09112708db/3/0/3004648_1655893976_1.jpg']
}

harajuku_socks = {
    'title': 'Cute and Colorful Harajuku socks Printed',
    'description': "Ttired of waring borin' ol' socks? M too, that's why i made thee handknitted harajuku socks with various cute and funny designs to pick from. your boring sock days are over.",
    'price_in_cents': 211,
    'qty': 32,
    'vendor': yuki,
    'tags': ['socks', 'comfy', 'funny'],
    'images': ['https://thekawaiishoppu.com/cdn/shop/products/harajuku-colorful-socks-one-size-eu-35-39-fashion-the-kawaii-shoppu-0.jpg?v=1657950515']*4
}

totoro = {
    'title': 'Totoro Toy Plush Gifts',
    'description': "Who doesn't love a Miyazaki film. Now you can be reminded of your cuddly favorite character wherever you go with this Totoro toy figurine.",
    'price_in_cents': 262,
    'qty': 42,
    'vendor': yuki,
    'tags': ['totoro', 'cute'],
    'images': ['https://m.media-amazon.com/images/I/61FxGdCCyQL._SL1024_.jpg']*4
}

garter_belt = {
    'title': 'Sexy Garter Belt Harness Set',
    'description': "For the wilder days. Made from faux leather, the materials are stretchy, comfortable and form-fitting",
    'price_in_cents': 1546,
    'qty': 22,
    'vendor': sam,
    'tags': ['sexy', 'garter', 'harness'],
    'images': ['https://m.media-amazon.com/images/I/61lPrzWv3RL._UL1200_.jpg']*3
}

spiked_boots = {
    'title': 'Spiky Goth Boots Platform',
    'description': "Don't these gorgeous boots just make you want to try putting them in someone's face? I'm not saying they were made to kick people with, but ... i mean with all that spiky goodness they make it tempting tho",
    'price_in_cents': 9800,
    'qty': 45,
    'vendor': sam,
    'tags': ['boots', 'spikes', 'comfy'],
    'images': ['https://i.pinimg.com/564x/19/c8/1b/19c81bbafd5afabdfef7392509c3cb0b.jpg']*4
}

choker = {
    'title': 'Cute Choker',
    'description': "What can i say i got my days when i'm suddenly into cute stuff. if you love the sweet kitten or the sexy cougar look, try on one of my leather chokers.",
    'price_in_cents': 3670,
    'qty': 17,
    'vendor': sam,
    'tags': ['choker', 'cute', 'necklace'],
    'images': ['https://m.media-amazon.com/images/I/51jYvQ5mgsL._AC_UX569_.jpg']*3
}

shades = {
    'title': 'Slim Shadies Sexy Black Shades',
    'description': "All true vampires need protection from the sun in every way possible. Try on one of my self-made chiller designs",
    'price_in_cents': 4570,
    'qty': 13,
    'vendor': sam,
    'tags': ['shades', 'sunglasses'],
    'images': ['https://ae01.alicdn.com/kf/H811b7725e14748008de142fc640b05c7R.jpg', 'https://ae01.alicdn.com/kf/H268493ea62e6417b8aa77bce187b7d7dv.jpg', 'https://ae01.alicdn.com/kf/Ha9df103c95f94846b2777e459e05b1baq.jpg']
}

skull = {
    'title': 'Skull Set Decor Home',
    'description': "You can never have enough skulls laying around your house.",
    'price_in_cents': 3740,
    'qty': 5,
    'vendor': sam,
    'tags': [],
    'images': ['https://ae01.alicdn.com/kf/Hf79f45f50866438ba71f0065dfa9ec7eX.jpg', 'https://ae01.alicdn.com/kf/H8ef8c778de9b487fb8801d34b031d425W.jpg', 'https://ae01.alicdn.com/kf/Haa7f180b0eb747efb097215c20f12ec2C.jpg']
}

goth_skirt = {
    'title': 'Goth ailor Skirt Cute Harajuku',
    'description': "Most goth gals have an inner 'cutesy' side. With these black and pink skirts, you won't have to decide between your two personalitiess anymore. Unleash your inner baby monster.",
    'price_in_cents': 2045,
    'qty': 58,
    'vendor': sam,
    'tags': ['kawaii', 'cute', 'skirt', 'comfy'],
    'images': ['https://ae01.alicdn.com/kf/H2fe8f6a3232340e1a36f7ea5d7f0617bE.jpg', 'https://ae01.alicdn.com/kf/H70755b14366a41c49acbeb9a91ee6548y.jpg', 'https://ae01.alicdn.com/kf/Hcf0fc10510954c75a48223fd012110a4l.jpg', 'https://ae01.alicdn.com/kf/H33905f3ee94e4acf83cabb798765f7c3b.jpg']
}

scented_candles = {
    'title': 'Scented Candles Halloween Autumn Relaxing',
    'description': "These candles come in 3 scented variations: Pumpkin Spice, Autumn Night, and Smokey Musk. If you're as into halloween season ass i am, these candles will be sure to bring the spooky spirits in",
    'price_in_cents': 300,
    'qty': 60,
    'vendor': sam,
    'tags': ['relax', 'candles', 'sleep'],
    'images': ['https://ae01.alicdn.com/kf/Hd0261bf77e134a0098d0d7995af3a6b1c.jpg?width=750&height=1275&hash=2025', 'https://ae01.alicdn.com/kf/H28ca80cd5555403f918363dd5a3d6de2u.jpg?width=750&height=1275&hash=2025', 'https://ae01.alicdn.com/kf/H241948339e5e41d9af523a5a6d89c5e7O.jpg?width=750&height=1274&hash=2024', 'https://ae01.alicdn.com/kf/H241948339e5e41d9af523a5a6d89c5e7O.jpg?width=750&height=1274&hash=2024', 'https://ae01.alicdn.com/kf/Hd89fcbd72b8f41cc898146ee8f210eb9D.jpg?width=750&height=1275&hash=2025']
}

bath_bomb = {
    'title': 'Glitter Bath Bomb',
    'description': "Creates a beautiful glittery explosion and relseases relaxing aromas. I use these to wind down after a stressfull week",
    'price_in_cents': 600,
    'qty': 50,
    'vendor': alaska,
    'tags': ['relax', 'bath', 'pink'],
    'images': ['https://ae01.alicdn.com/kf/H56325c2497da4e6f9f956661f51dc288b.jpg', 'https://ae01.alicdn.com/kf/Hfaf1d9919a0047af8d181ec004888e0ag.jpg', 'https://ae01.alicdn.com/kf/H06dc40fc03404d68a4fb9b056efec9f9N.jpg']
}

crystal_gem = {
    'title': 'Crystal Gems Jewelry',
    'description': "They say Gems and Crystal have magical healing powers. If your interrested to know which gem to choose based on your birthsign, contact me. These are great as gifts to loved ones",
    'price_in_cents': 1560,
    'qty': 20,
    'vendor': alaska,
    'tags': ['necklace', 'crystals', 'handmade'],
    'images': ['https://ae01.alicdn.com/kf/H36ba6a1e2c4f4014a12a5737c612fdc56.jpg', 'https://ae01.alicdn.com/kf/H18d1de464f1340889ef62e6b3a3392baw.jpg', 'https://ae01.alicdn.com/kf/H33df8a92ed0149f29beed69904d3d3baZ.jpg']
}

bracelet = {
    'title': 'Hand made Silver Bracelet',
    'description': "Made of sterling silver, and all natural products",
    'price_in_cents': 2500,
    'qty': 15,
    'vendor': alaska,
    'tags': ['jewelry'],
    'images': ['https://ae01.alicdn.com/kf/Ha494879551ec40669a7023b91cbc53015.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/H46e6cce9ec77425a8b9ee4e43dabd347L.jpg?width=800&height=800&hash=1600', 'https://ae01.alicdn.com/kf/Ha97c111c0a434b87ae7252d7d055a953y.jpg?width=500&height=500&hash=1000', 'https://ae01.alicdn.com/kf/H681ee31baa004ec8bb2295da2cdee588l.jpg?width=800&height=800&hash=1600']
}

cacti_plant = {
    'title': 'Small Cacti Plant',
    'description': "I started growing these late last summer, and oh' my how they've bloomed. I have about 15 of them now in the house. I'm very proud of how well they've grown. Included in the packlage will be a guide on how to take further care of your cactus baby",
    'price_in_cents': 300,
    'qty': 12,
    'vendor': alaska,
    'tags': ['plant', 'botanic', 'cacti', 'garden', 'cute'],
    'images': ['https://ae01.alicdn.com/kf/HTB1udsOXxD1gK0jSZFyq6AiOVXau.jpg', 'https://ae01.alicdn.com/kf/Hba8013795e6d444f9105285d83932bdeU.jpg', 'https://ae01.alicdn.com/kf/HTB1UbwIXq67gK0jSZFHq6y9jVXa8.jpg', 'https://ae01.alicdn.com/kf/H42cd2add7e514b18991c0d2bae99e283Q.jpg']
}

jewelry = {
    'title': 'Costum Made Jewelry',
    'description': "In my free time i combine gems and metals to create one of a kind jewelry pieces. If you'd like me to make one for you just send me your custom measurements along with a description of what you're looking for and i can make you an offer",
    'price_in_cents': 1750,
    'qty': 100,
    'vendor': alaska,
    'tags': ['jewelry'],
    'images': ['https://ae01.alicdn.com/kf/H31b289e56e534a77bb7a2195aa79f13ez.jpg', 'https://ae01.alicdn.com/kf/H63a96460ce8742aea12356686e1e6981b.jpg', 'https://ae01.alicdn.com/kf/H8a728a548c9e4bc69936ffbdd06084870.jpg', 'https://ae01.alicdn.com/kf/Hb2ab0d7868e540f78a408eb3a74d1ef6T.jpg', 'https://ae01.alicdn.com/kf/H32bd46fb8da64ad0b8ef0aac84f8ec4bt.jpg']
}

phonecase = {
    'title': 'Pretty Phonecase',
    'description': "In a crafty mood again. I made a batch of 20 phonecases all with cute different designs. See any you like? Or have an idea for a phone case of your own, just shoot me a message",
    'price_in_cents': 345,
    'qty': 18,
    'vendor': alaska,
    'tags': ['phonecase', 'cute', 'crafts'],
    'images': ['https://ae01.alicdn.com/kf/HTB1HNbnBkCWBuNjy0Faq6xUlXXaM.jpg', 'https://ae01.alicdn.com/kf/HTB1QF6UBhGYBuNjy0Fnq6x5lpXa6.jpg', 'https://ae01.alicdn.com/kf/HTB1f5AwjHsrBKNjSZFpq6AXhFXah.jpg', 'https://ae01.alicdn.com/kf/HTB1yxfnBkCWBuNjy0Faq6xUlXXab.jpg?width=1080&height=1618&hash=2698']
}

make_up_brush = {
    'title': 'Magical Girl Make Up Brush Set',
    'description': "Not your average make up brush sets. These come in different designs from mermaid, to unicorn, to fairies, you name it!",
    'price_in_cents': 750,
    'qty': 4,
    'vendor': alaska,
    'tags': ['unicorn', 'cute', 'magic'],
    'images': ['https://ae01.alicdn.com/kf/H7d6554c930b54b73b2c66685c7cefb25o.jpg?width=1920&height=1920&hash=3840', 'https://ae01.alicdn.com/kf/H7892ca1040ad46da824202f13e105a9eb.jpg?width=1920&height=1920&hash=3840', 'https://ae01.alicdn.com/kf/H18ddcdb04acf41819eb3605cb723188aN.jpg?width=1920&height=1920&hash=3840', 'https://ae01.alicdn.com/kf/H745f3374fcac423591a450590df8a3bc8.jpg?width=1920&height=1920&hash=3840']
}

##################################### functions ##############################################
yuki_products = [unicorn, avocado_keychain, cat_ears, earrings,
                 plush_bacpack, sailor_skirt, cosplay_wig, harajuku_socks, totoro]
sam_products = [garter_belt, spiked_boots, choker,
                shades, skull, goth_skirt, scented_candles]
alaska_products = [bath_bomb, crystal_gem, bracelet,
                   cacti_plant, jewelry, phonecase, make_up_brush]

betsy_users = [yuki, sam, alaska]
user_products = [yuki_products, sam_products, alaska_products]


def create_users(users):
    for user in users:
        verify_signup(user_name=user['username'], full_name=user['full_name'], address=user['address'],
                      bio=user['bio'], avatar_url=user['avatar_url'], password=user['password'])


def create_products(product_list):
    for products in product_list:
        for product in products:
            prod_id = add_product_to_catalog(product)
            if prod_id:
                tag_list = product['tags']
                add_product_tags(prod_id, tag_list)
                image_list = product['images']
                add_images_to_product(prod_id, image_list)


def create_fake_db_accounts():
    '''creates 3 users with around 10 products each 
    for testing site functionality with'''
    create_tables()
    create_users(betsy_users)
    create_products(user_products)
