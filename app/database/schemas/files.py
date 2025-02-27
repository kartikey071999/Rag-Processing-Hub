import uuid

from app.commons.enums import PlatformEnum, StatusEnum, Module
from sqlmodel import SQLModel, Field, select
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.schemas.utils import compile_sql_or_scalar


class FilesBase(SQLModel):
    filename_without_extension: str = Field(
        description="The original filename uploaded without the file extension"
    )
    file_extension: str = Field(
        description="The extenion of the file like .pdf, .doc"
    )
    uploaded_file_last_modified: datetime | None = Field(
        default=None, description="The last updated date of the file"
    )
    owner: str | None = Field(default=None, description="The owner of the file")
    file_status: StatusEnum = Field(
        sa_column_kwargs={"default": StatusEnum.REQUESTED},
        description="The status of the file",
    )
    platform_status: PlatformEnum = Field(
        sa_column_kwargs={"default": None},
        description="The status of the file for config platform",
    )
    current_process: Module =  Field(
        sa_column_kwargs={"default": None},
        description="The status of the file for config platform",
    )
    file_status_last_modified: datetime | None = Field(
        default=None, description="Last modified date of the record"
    )
    file_location: str | None = Field(
        default=None, description="location of the file"
    )
    user_email: str | None = Field(
        default=None, description="user email of the user uploading file"
    )
    record_created_at: datetime | None = Field(
        description="This is column is updated automatically in db when a record is newly created"
    )
    failure_reason: str | None = Field(
        default=None,
        description="Consists of Failure Reason.",
    )


class Files(FilesBase, table=True):
    file_id: uuid.UUID | None = Field(
        default=None, primary_key=True, description="File id stored as UUID"
    )

    @classmethod
    @compile_sql_or_scalar
    async def find(cls, session: AsyncSession, compile_sql=False, *args, **kwargs):
        stmt = select(cls).filter(*args).filter_by(**kwargs)
        return stmt
