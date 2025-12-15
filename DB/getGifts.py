import sqlite3

con = sqlite3.connect("./DB/childrensData.db")
cur = con.cursor()

cur.execute("SELECT DISTINCT last_year_gift FROM history;")

history:list = cur.fetchall()

strHistory = str(history).replace("(", "")
strHistory = strHistory.replace(")", "")
strHistory = strHistory.replace("[", "")
strHistory = strHistory.replace("]", "")
strHistory = strHistory.replace(",,", ",")
strHistory = strHistory.replace("'", "")

history = strHistory.split(",")

cur.execute("SELECT wishlist_items FROM wishlist;")

wishlists:list = cur.fetchall()

formatedWishlist:list = []

for wish in wishlists:
    wish = str(wishlists)
    wish = wish.replace("'", "")
    wish = wish.replace("(", "")
    wish = wish.replace(")", "")
    wish = wish.replace("[", "")
    wish = wish.replace("]", "")
    gifts:list = wish.split(",")
    for gift in gifts:
        if not (gift in formatedWishlist) and gift != "":
            formatedWishlist.append(gift)

for index, gift in enumerate(formatedWishlist):
    if gift in history:
        formatedWishlist.pop(index)

giftList = history + formatedWishlist

print(giftList)

# cur.execute("CREATE TABLE IF NOT EXISTS gifts (gift, age_limit, category);")

# for gift in giftList:
#     print("\n" + gift)
#     while True:
#         try:
#             ageLimit = int(input("enter age limit $ "))
#             break
#         except:
#             print("not a valid number\n")
#     category = input("enter category $ ")
#     con.execute("INSERT INTO gifts (gift, age_limit, category) VALUES (?, ?, ?)", [gift, ageLimit, category])
    
# con.commit()

# cur.execute("SELECT * FROM gifts;")

# print(cur.fetchall())