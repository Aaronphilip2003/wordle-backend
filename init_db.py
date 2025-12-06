import asyncpg
import asyncio

async def init_db():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='wordle_db',
        host='localhost',
        port=5432
    )

    await conn.close()

if __name__ == "__main__":
    asyncio.run(init_db())
