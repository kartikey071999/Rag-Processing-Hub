import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from commons import constants
from database.schemas import Files

# Create an asynchronous engine
engine = create_async_engine(constants.ASYNC_DB_URL, echo=True)

# Create a session factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables():
    """Asynchronously creates tables in the PostgreSQL database."""
    print("Tables registered in metadata:", SQLModel.metadata.tables.keys())
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def main():
    """Main function to initialize and create the table."""
    print("Creating tables in the database...")
    await create_tables()
    print("Tables created successfully!")


if __name__ == "__main__":
    asyncio.run(main())
