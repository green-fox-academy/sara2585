class PostIt():
    background_color = ""
    text = ""
    text_color = ""

post1 = PostIt()
post1.background_color = "Orange"
post1.text = "Idea 1"
post1.text_color = "blue"

post2 = PostIt()
post2.background_color = "pink"
post2.text = "Awesome"
post2.text_color = "black"

post3 = PostIt()
post3.background_color = "yellow"
post3.text = "Superb!"
post3.text_color = "green"

print(f"The backcolor of post1:  {post1.background_color}, The text of post1: {post1.text}, The text color of post1: {post1.text_color}" )
print(f"The backcolor of post2:  {post2.background_color}, The text of post2: {post2.text}, The text color of post2: {post2.text_color}" )
print(f"The backcolor of post3:  {post3.background_color}, The text of post3: {post3.text}, The text color of post3: {post3.text_color}" )

