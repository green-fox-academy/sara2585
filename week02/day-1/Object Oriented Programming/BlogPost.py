class BlogPost():
    author_name = ""
    title = ""
    text = ""
    publication_date = ""

blog1 = BlogPost()
blog1.author_name = "John Doe"
blog1.title = "Lorem Ipsum"
blog1.text = "Lorem ipsum dolor sit amet"
blog1.publication_date = "2000.05.04"

blog2 = BlogPost()
blog2.author_name = "Tim Urban"
blog2.title = "Wait but why"
blog2.text = "A popular long-form, stick-figure-illustrated blog about almost everything"
blog2.publication_date = "2010.10.10"

blog3 = BlogPost()
blog3.author_name = "William Turton"
blog3.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
blog3.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
blog3.publication_date = "2017.03.28"

print(f"Author of blog1: {blog1.author_name}, title: {blog1.title}, text: {blog1.text}, publication_date: {blog1.publication_date}")
print(f"Author of blog2: {blog2.author_name}, title: {blog2.title}, text: {blog2.text}, publication_date: {blog2.publication_date}")
print(f"Author of blog3: {blog3.author_name}, title: {blog3.title}, text: {blog3.text}, publication_date: {blog3.publication_date}")



