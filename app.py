import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_mongodb.mongodb_connection import MongoDBConnection
def main():
    # Set page config and title
    st.set_page_config(page_title="Streamlit MongoDB Connection", page_icon="🚀")
    st.markdown("<h2 style='text-align:center;background-color:#262730;border-radius: 10px;padding: 10px;'>Streamlit hackathon - MongoDB connection</h2>",unsafe_allow_html=True)

    # Set options
    option = option_menu("",["About - MongoDB connection","Example - Note taking app"] , icons=["database-add","terminal"], default_index=1,orientation='horizontal',styles={"nav-link-selected": {"background-color": "#67A6AA"}})

    if option == "About - MongoDB connection":
        content = """
## About MongoDB Streamlit Connection

The MongoDB Streamlit Extension is a convenient tool that allows you to seamlessly integrate your Streamlit apps with MongoDB databases. This extension provides a set of methods to establish connections, perform CRUD operations, and retrieve data from MongoDB collections right from your Streamlit app.

## Features

- **Easy Connection Setup**: Connect to your MongoDB instance with just a few lines of code. The extension takes care of the connection details, so you can focus on building your app.

- **Retrieve Data**: Fetch individual documents or get all the documents from a MongoDB collection and display them in your Streamlit app effortlessly.

- **Insert, Update, Delete**: Perform CRUD operations by inserting new documents, updating existing ones, or deleting specific documents using simple method calls.

## Getting Started

To get started with the Streamlit MongoDB  Connection, follow the installation steps provided in the [documentation](https://github.com/rajaathota72-fc/mongodb-connection/blob/main/README.md).

## Example

Here's a quick example of implementation presented in Example - Note taking app. 

## Contributions

We welcome contributions from the community to improve this extension. If you encounter any issues, have suggestions for enhancements, or want to contribute to the project, please visit our GitHub repository and get involved.

Happy Streamlit and MongoDB integration! 🚀📊

---

*Note: The MongoDB Streamlit Extension is not affiliated with MongoDB Inc. It is an independent project created by the community to simplify MongoDB integration with Streamlit apps.*
        """
        st.markdown(content)

    if option == "Example - Note taking app":
        # Read secrets from secrets.toml
        mongo_secrets = st.secrets["mongodb"]

        # Establish a connection with MongoDB
        conn = MongoDBConnection("my_mongo_conn", mongo_uri=mongo_secrets["mongo_uri"])

        # tabs for CRUD operations
        tab_options = ["Create", "Read", "Update", "Delete"]
        create, read, update, delete = st.tabs(tab_options)

        # Create note
        with create:
            # Input fields to add a new note or update an existing note
            st.subheader("Create : Insert note into database")
            note_id = st.text_input("Note ID")
            title = st.text_input("Title")
            content = st.text_area("Content")

            # Add or Update a note
            if st.button("Save Note"):
                if title and content:
                    if conn.find_document("Notebook", "Notes", note_id):
                        update_data = {'title': title, 'content': content}
                        conn.update_document("Notebook", "Notes", note_id, update_data)
                        st.success("Note updated successfully!")
                    else:
                        document_data = {"_id": note_id, "title": title, "content": content}
                        conn.insert_document("Notebook", "Notes", document_data)
                        st.warning("Note saved successfully")

        # Read notes
        with read:
            st.subheader("Read : Fetch all notes and present in a table")
            notes_df = conn.get_all_documents("Notebook", "Notes")
            if len(notes_df) > 0:
                notes_df += 1
                st.dataframe(notes_df)
            else:
                st.warning('No notes found.')

        # Update notes
        with update:
            st.header("Update a Note")
            note_id = st.text_input("Enter the ID of the note to update:")
            update_title = st.text_input("New Title")
            update_content = st.text_area("New Content")
            if st.button("Update Note"):
                update_data = {"title": update_title, "content": update_content}
                conn.update_document("Notebook", "Notes", note_id, update_data)
                st.success("Note updated successfully!")

        # Delete a note
        with delete:
            st.subheader("Delete notes")
            note_id_to_delete = st.text_input("Enter Note ID to delete")
            if note_id_to_delete and st.button('Delete Note'):
                conn.delete_document("Notebook", "Notes", note_id_to_delete)
                st.success("Note deleted successfully!")


if __name__ == "__main__":
    main()
