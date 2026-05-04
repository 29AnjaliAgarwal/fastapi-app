from fastapi import FastAPI
from src.auth.routes import auth_router
from src.books.routes import book_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from .errors import register_all_errors
from .middleware import register_middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix =f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description=description,
    version=version,
   
    contact={
        "name": "Anjali",
        "url": "https://github.com/29AnjaliAgarwal",
        "email": "anjali.ag0229@gmail.com",
    },
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        "fastapi-bookly-app-1037152109346.asia-south1.run.app",
        "localhost",
        "127.0.0.1",
       "*.run.app",
    ]
)
register_all_errors(app)

register_middleware(app)


app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"{version_prefix}/tags", tags=["tags"])
