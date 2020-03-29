#### Notes
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
- https://palletsprojects.com/p/jinja/

```bash
# port 5000 default
flask run
```

#### Rules
1. Keep the logic of your application separate from the layout/presentation of web pages.
- Use templates to achieve this separation between presentation and business logic.
- Rationale: hire a web designer to create a killer web site while you code the application logic in Python.

2. Separation of Concerns

A concern is a set of information that affects the code of a computer program. Ideally, concerns would be isolated from one another.
- Presentation layer: visual appearance of the site
- Business logic layer: the way that the site behaves in response to user actions
- Persistence layer: read/write/delete records to disk or database
- Configuration layer: how an application can be adjusted