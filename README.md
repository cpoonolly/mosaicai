# Setup

Essentially just need to run `docker compose up --build` from the root dir in order to spin up the service

App runs on port 80 and supports the following endpoints:
- Fetch all books. Ex: `GET http://localhost:80/book/?price_gt=199&price_lt=201&publication_time_gt=2021-01-01&publication_time_lt=2021-01-01&isbn=123`
- Fetch a single book. Ex: `GET http://localhost:80/book/{book_id}`
- Create a book. Ex: `POST http://localhost:80/book/` with ex `{"title": "Harry Potter","author": "JKR","ISBN": "123456","publication_time": "2020-01-01 00:00:00","genre": "Fantasy","price": 200.0,}` in the JSON body
- Update a book. Ex: `PATCH http://localhost:80/book/{book_id}` with ex `{"title": "Harry Potter","author": "JKR","ISBN": "123456","publication_time": "2020-01-01 00:00:00","genre": "Fantasy","price": 200.0,}` in the JSON body
- Delete a book. Ex: `PATCH http://localhost:80/book/{book_id}`

Of the many things I didn't get to, these are a few:
- Adding more correct json vaildation on all the models
- Better connecting pydantic and the ORM I choose for this session (Tortoise ORM)
- Not hardcoding db credentials
- etc.
