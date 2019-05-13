from BlogPost import BlogPost
class Blog():
    def __init__(self):
        self.blogs = []
        blog1 = BlogPost()
        blog1.author_name = "John Doe"
        blog1.title = "Lorem Ipsum"
        blog1.text = "Lorem ipsum dolor sit amet"
        blog1.publication_date = "2000.05.04"
        self.blogs.append(blog1)

        blog2 = BlogPost()
        blog2.author_name = "Tim Urban"
        blog2.title = "Wait but why"
        blog2.text = "A popular long-form, stick-figure-illustrated blog about almost everything"
        blog2.publication_date = "2010.10.10"
        self.blogs.append(blog2)

        blog3 = BlogPost()
        blog3.author_name = "William Turton"
        blog3.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
        blog3.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
        blog3.publication_date = "2017.03.28"
        self.blogs.append(blog3)

    def delete(self, n):
        self.blogs.pop(n)
        return self.blogs

    def update(self, n, BlogPost):
        self.blogs[n] = BlogPost
        return self.blogs

blog = Blog()
print(blog.blogs)
blog.delete(1)
print(blog.blogs)

blogpost = BlogPost()
blogpost.author_name = "sara"
blogpost.title = "sara test"
blogpost.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
blogpost.publication_date = "2017.03.28"

blog.update(0,blogpost)
print(blog.blogs)