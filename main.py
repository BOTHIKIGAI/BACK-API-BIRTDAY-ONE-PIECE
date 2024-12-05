"""
Main module for the BIRTHDAY ANIME API.

This module initializes the FastAPI application and includes the router for handling
requests related to anime episode release dates.
"""

from fastapi import FastAPI
from app.router.v1.author_router import AuthorRouter

app = FastAPI(
    title="BIRTHDAY ANIME",
    description="API for the consumption of episode release dates.")

app.include_router(AuthorRouter)
