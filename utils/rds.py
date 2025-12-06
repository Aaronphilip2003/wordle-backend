import asyncpg
import random

async def get_random_word(db):
    query = "SELECT word FROM words ORDER BY RANDOM() LIMIT 1;"
    result = await db.fetchval(query)
    return result