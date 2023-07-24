import streamlit as st
from streamlit_mongodb.mongodb_connection import MongoDBConnection
def main():
    # Read secrets from secrets.toml
    #st.secrets.load_manifest("secrets.toml")
    mongo_secrets = st.secrets["mongodb"]

    # Establish a connection with MongoDB
    conn = MongoDBConnection("my_mongo_conn", mongo_uri=mongo_secrets["mongo_uri"])

    st.title("MongoDB Note-taking App")

    # Input fields to add a new note or update an existing note
    note_id = st.text_input("Note ID (Optional, for updates)")
    title = st.text_input("Title")
    content = st.text_area("Content")

    # Add or Update a note
    if st.button("Save Note"):
        if title and content:
            if note_id:
                update_data = {"title": title, "content": content}
                conn.update_document("Notebook","Notes", note_id, update_data)
                st.success("Note updated successfully!")
            else:
                document = {"title": title, "content": content}
                conn.insert_document("Notebook","Notes", document)
                st.success("Note added successfully!")

    # Show all notes
    st.subheader("All Notes:")
    notes_df = conn.get_all_documents("Notebook","Notes")
    st.dataframe(notes_df)

    # Delete a note
    if st.button("Delete Note"):
        note_id_to_delete = st.text_input("Enter Note ID to delete")
        if note_id_to_delete:
            conn.delete_document("Notebook","Notes", note_id_to_delete)
            st.success("Note deleted successfully!")

if __name__ == "__main__":
    main()
