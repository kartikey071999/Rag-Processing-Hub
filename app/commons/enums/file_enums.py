from enum import Enum




class PlatformEnum(Enum):
    UPLOAD = "Uploaded"        # Initial upload is done
    PROCESS = "Processing"    # Any process (digitization, vectorization, etc.) is ongoing
    FAIL = "Failed"            # Any stage failed
    COMPLETE = "Completed"  # The file has gone through all processing steps successfully
    DELETE = "Deleted"  # File is deleted from storage


class Module(Enum):
    UPLOAD = "Uploading"
    DIGITIZATION = "Digitization"
    CHUNKING = "Chunking"
    EMBEDDING = "Embedding"
    VECTOR_DB = "VectorDB"
    RETRIEVAL = "Retrieval"
    VOICE_TO_TEXT = "VoiceToText"
    TEXT_TO_SPEECH = "TextToSpeech"



class StatusEnum(Enum):

    REQUESTED = "Requested"
    UPLOADED = "Uploaded"
    DIGITIZED = "Digitized"
    CHUNKED = "Chunked"
    VECTORIZED = "Vectorized"
    RETRIEVED = "Retrieved"
    VECTOR_STORE_INSERTED = "VectorStoreInserted"
    VOICE_TO_TEXT_COMPLETED = "VoiceToTextCompleted"

