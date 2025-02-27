import logging

from fastapi import HTTPException
from sqlalchemy.future import select

import asyncio
import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.database.schemas import Files
from app.commons.enums import PlatformEnum, StatusEnum, Module
from app import constants
import logging


class FileStatusRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_file_status_record(self, file_status_record: Files) -> bool:
        """
        Inserts a record in the FileStatus table.

        :param file_status_record: Files object.
        :return: True if successful.
        """
        async with self.session.begin():
            self.session.add(file_status_record)
        return True

    async def get_by_file_by_file_id(self, file_id: uuid.UUID, check_deleted: bool = True) -> Files:
        """
        Fetches a record from FileStatus based on File ID.

        :param file_id: UUID of the file.
        :param check_deleted: Whether to check if the file is marked as deleted.
        :return: Files object.
        :raises HTTPException: If file is not found or deleted (when `check_deleted=True`).
        """
        logging.info(f"Getting file with file id: {file_id}")
        query = select(Files).filter_by(file_id=str(file_id))
        result = await self.session.execute(query)
        file_record = result.scalar_one_or_none()

        if file_record is None:
            raise HTTPException(status_code=404, detail="File not found")

        if check_deleted and file_record.platform_status == PlatformEnum.DELETE:
            raise HTTPException(status_code=400, detail="File is deleted")

        return file_record


async def main():
    """Main function to test FileStatusRepository"""

    # Create an asynchronous engine
    engine = create_async_engine(constants.ASYNC_DB_URL, echo=True)

    # Create a session factory
    async_session_local = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session_local() as session:
        repository = FileStatusRepository(session)

        # Create a new file record
        file_id = uuid.uuid4()
        new_file = Files(
            filename_without_extension = "firsttest",
            file_extension = "kyg",
            file_id=file_id,
            uploaded_file_last_modified = datetime.utcnow(),
            file_status = StatusEnum.REQUESTED,
            current_process = Module.UPLOAD,
            file_status_last_modified = datetime.utcnow(),
            created_at=datetime.utcnow(),
            platform_status=PlatformEnum.UPLOAD ,

        )

        print(f"Inserting file with ID: {file_id}")
        await repository.create_file_status_record(new_file)

        # Retrieve the inserted file
        try:
            retrieved_file = await repository.get_by_file_by_file_id(file_id)
            print(f"Retrieved File: {retrieved_file.file_id}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
