from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

from core.settings import settings


documents = SimpleDirectoryReader(settings.MEDIA_ROOT).load_data()

try:
    storage_context = StorageContext.from_defaults(settings.BASE_DIR / 'storage')
    index = load_index_from_storage(storage_context)
except ValueError:
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist()


query_engine = index.as_query_engine()
