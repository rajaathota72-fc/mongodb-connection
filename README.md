# MongoDB Extension for Streamlit

This repo consists of  Streamlit Mongodb connection  that provides a simple and convenient way to connect to a MongoDB database for streamlit apps. The connection is built as an extension to `ExperimentalBaseConnection`, allowing you to establish a connection to your MongoDB instance and perform CRUD operations with ease.

## Installation

To use the MongoDB extension for Streamlit, follow these steps:

1. Clone the GitHub repository or download the code:
   ```bash
   git clone https://github.com/rajaathota72-fc/mongodb-connection.git
   cd mongodb-connection
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt 
   ```

3. Replace the link for mongo_uri in .streamlit/secrets.toml 


## Usage

Once you have installed the libraries, you can use it in your Streamlit app as follows:

```python
import streamlit as st
from streamlit_mongodb.mongodb_connection import MongoDBConnection

# Initialize the MongoDB connection
mongo_secrets = st.secrets["mongodb"]
conn = MongoDBConnection("Name of connection",mongo_uri=mongo_secrets["mongo_uri"])

# Apply methods to interact with db

```

## Method Usage

### `find_document(db_name: str, collection_name: str, document_id: str)`

This method retrieves a single document from the specified MongoDB collection based on the given `document_id`.

#### Parameters:

- `db_name` (str): The name of the MongoDB database containing the desired collection.
- `collection_name` (str): The name of the MongoDB collection to search for the document.
- `document_id` (str): The unique identifier of the document to retrieve.

#### Example:

```python
# Assuming the MongoDB connection is already established in 'mongo' object
document_id = "unique_document_id_here"
result = mongo.find_document("my_database", "my_collection", document_id)
print(result)
```

### `insert_document(db_name: str, collection_name: str, document: dict)`

This method inserts a single document into the specified MongoDB collection.

#### Parameters:

- `db_name` (str): The name of the MongoDB database where the document should be inserted.
- `collection_name` (str): The name of the MongoDB collection to insert the document.
- `document` (dict): The document to be inserted, represented as a Python dictionary.

#### Example:

```python
# Assuming the MongoDB connection is already established in 'mongo' object
new_document = {
    "title": "New Document",
    "content": "This is a new document to be inserted."
}
mongo.insert_document("my_database", "my_collection", new_document)
```

### `update_document(db_name: str, collection_name: str, document_id: str, update_data: dict)`

This method updates a single document in the specified MongoDB collection that matches the given `document_id`.

#### Parameters:

- `db_name` (str): The name of the MongoDB database containing the collection to update.
- `collection_name` (str): The name of the MongoDB collection to update the document in.
- `document_id` (str): The unique identifier of the document to be updated.
- `update_data` (dict): The data that should be updated, represented as a Python dictionary.

#### Example:

```python
# Assuming the MongoDB connection is already established in 'mongo' object
document_id = "unique_document_id_here"
update_data = {
    "content": "This is an updated content."
}
mongo.update_document("my_database", "my_collection", document_id, update_data)
```

### `delete_document(db_name: str, collection_name: str, document_id: str)`

This method deletes a single document from the specified MongoDB collection that matches the given `document_id`.

#### Parameters:

- `db_name` (str): The name of the MongoDB database containing the collection to delete from.
- `collection_name` (str): The name of the MongoDB collection to delete the document from.
- `document_id` (str): The unique identifier of the document to be deleted.

#### Example:

```python
# Assuming the MongoDB connection is already established in 'mongo' object
document_id = "unique_document_id_here"
mongo.delete_document("my_database", "my_collection", document_id)
```

### `get_all_documents(db_name: str, collection_name: str) -> pd.DataFrame`

This method retrieves all documents from the specified MongoDB collection and returns them as a pandas DataFrame.

#### Parameters:

- `db_name` (str): The name of the MongoDB database containing the collection.
- `collection_name` (str): The name of the MongoDB collection to fetch all documents from.

#### Returns:

- `pd.DataFrame`: A pandas DataFrame containing all the documents from the specified collection.

#### Example:

```python
# Assuming the MongoDB connection is already established in 'mongo' object
df = mongo.get_all_documents("my_database", "my_collection")
print(df)
```

## Example App

For a complete example of using the MongoDB connection in a Streamlit app, check the `app.py` file in this repository.

## Contributions

We welcome contributions to improve this MongoDB extension. If you find any issues or have suggestions for enhancements, please feel free to open an issue or submit a pull request on the GitHub repository.

Happy Streamlit and MongoDB integration! 😊🚀
