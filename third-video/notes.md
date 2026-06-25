# Path Parameters in FastAPI

## 01:28 — Introduction to Path Parameters

- Path parameters are variables that are part of the URL path.
- FastAPI captures values from the URL and passes them into a function as arguments.
- Type hints provide automatic validation for path parameter values.

## 02:52 — Single Post Endpoint

- Create a route with a path parameter such as `{post_id}`.
- Include `post_id` as a function parameter with a type hint like `int`.
- FastAPI validates the input automatically.

## 07:01 — Error Handling and HTTP Exceptions

- When a post is not found, raise an `HTTPException` instead of returning an error dictionary.
- Use `HTTPException` and `status` from FastAPI for clear, standard error responses.

## 11:39 — Automatic Documentation

- FastAPI automatically generates docs for the new route.
- The documentation can be tested in the browser.
- Path parameters like post ID are validated as integers.

## 13:13 — Single Post Template

- Create a `post.html` template that extends `layout.html`.
- Display the author's image, post metadata, title, and content.

## 21:40 — API vs Browser Error Responses

- Handle browser requests with an HTML error page.
- Return JSON error messages for API requests.
- Use the request path prefix `/api` to distinguish API routes.

## 23:46 — Starlette Exceptions and JSON Responses

- Import `JSONResponse` and `HTTPException` from Starlette to handle validation and exceptions.
- Manually return JSON responses for error cases.
- Handle Starlette's 404 errors cleanly.

## 25:36 — Non-Existent Routes Handling

- Add an exception handler for Starlette HTTP exceptions.
- Return a JSON response with status and message for API paths.
- Provide a friendly HTML error page for browser requests.

## 31:31 — Validation Error Handling

- Add a separate handler for request validation errors.
- Return status `422` and error details for API responses.
- Return a simple error message for HTML responses.

## 36:00 — Summary

- Path parameters let you access specific resources through URLs.
- FastAPI helps handle errors for both API and browser routes.
