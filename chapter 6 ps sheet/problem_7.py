#Write a program to find out whether a given post is talking about “Harry” or not.
post = input("enter the post:")

if("Harry".lower() in post.lower()):
    print("this post is talking about harry")
else:
    print("this post is npt talking about harry")    