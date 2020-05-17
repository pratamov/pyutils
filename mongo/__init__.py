from os import getenv
from commons import get_logger

def import_directory(data_path, clean = False):
    log_level = getenv("LOG_LEVEL", "INFO")
    logger = get_logger("pyutils.mongo.import_directory", log_level)
    client = MongoClient(getenv("MONGO_URL"))
    database = client[getenv("MONGO_DB")]
    if clean:
        for collection in database.list_collection_names(include_system_collections=False):
            col = database[collection]
            col.drop()
            logger.warning("Drop collection {}".format(collection))

    for filename in listdir(data_path):
        if filename.endswith(".json"):
            data = loads(open("{}/{}".format(data_path, filename), "r").read())
            col = self.database[filename[:-5]]
            for record in data:
                try:
                    self.logger.info("Insert collection {}".format(filename[:-5]))
                    col.insert_one(record)
                except Exception as e:
                    self.logger.error("Insert collection {} : {}".format(filename[:-5], str(e)))
