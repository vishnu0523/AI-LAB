generate_blog :-
    open('blog.html', write, S),
    write(S, '<html><head><title>My Prolog Blog</title></head><body>'),
    write(S, '<h1>Welcome to My Blog</h1><p>Prolog-generated HTML.</p>'),
    write(S, '<a href="https://www.wordpress.org">Visit WordPress</a>'),
    write(S, '</body></html>'),
    close(S),
    write('Blog created: Open "blog.html".\n').
