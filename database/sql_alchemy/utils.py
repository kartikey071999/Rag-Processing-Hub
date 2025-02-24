
from functools import wraps


def compile_sql_or_scalar(func):
    @wraps(func)
    async def wrapper(cls, session, compile_sql=False, *args, **kwargs):
        stmt = await func(cls, session, *args, **kwargs)

        if compile_sql:
            return stmt.compile(
                dialect=session.bind.dialect,  # Automatically detect the database dialect
                compile_kwargs={"literal_binds": True}
            )

        result = await session.execute(stmt)
        return result.scalars().first()  # Return only one object

    return wrapper
