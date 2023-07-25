import streamlit as st
from streamlit_mongodb.mongodb_connection import MongoDBConnection
def main():
    # Read secrets from secrets.toml

    mongo_secrets = st.secrets["mongodb"]

    # Establish a connection with MongoDB
    conn = MongoDBConnection("my_mongo_conn", mongo_uri=mongo_secrets["mongo_uri"])

    st.title("MongoDB Note-taking App")

    # tabs for CRUD operations
    tab_options = ["Create", "Read", "Update", "Delete"]
    create,read,update,delete = st.tabs(tab_options)

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
                if conn.find_document("Notebook","Notes",note_id):
                    update_data = {'title':title,'content':content}
                    conn.update_document("Notebook","Notes", note_id, update_data)
                    st.success("Note updated successfully!")
                else:
                    document_data = {"_id": note_id, "title": title, "content": content}
                    conn.insert_document("Notebook", "Notes", document_data)
                    st.warning("Note saved successfully")


    # Read notes
    with read:
        st.subheader("Read : Fetch all notes and present in a table")
        notes_df = conn.get_all_documents("Notebook","Notes")
        if len(notes_df)>0:
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
            conn.update_document("Notebook","Notes", note_id, update_data)
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
