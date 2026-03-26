import streamlit as st
from pathlib import Path

st.set_page_config(page_title="FileForge", layout="centered")

st.title("📁 FileForge - File Management System")

# ==========================================
# Utility: List Files & Folders
# ==========================================
def list_files():
    base_path = Path.cwd()
    items = list(base_path.rglob("*"))
    return [str(item) for item in items]


# Sidebar Menu
menu = st.sidebar.selectbox(
    "Select Operation",
    ["Create File", "Read File", "Update File", "Delete File"]
)

# ==========================================
# CREATE FILE
# ==========================================
if menu == "Create File":
    st.header("📄 Create File")

    file_name = st.text_input("Enter file name (with extension)")
    content = st.text_area("Enter file content")

    if st.button("Create"):
        try:
            file_path = Path(file_name)

            if file_path.exists():
                st.warning("File already exists.")
            else:
                file_path.write_text(content)
                st.success("File created successfully!")
        except Exception as e:
            st.error(f"Error: {e}")


# ==========================================
# READ FILE
# ==========================================
elif menu == "Read File":
    st.header("📖 Read File")

    files = list_files()
    selected_file = st.selectbox("Select file", files)

    if st.button("Read"):
        try:
            file_path = Path(selected_file)

            if not file_path.exists() or not file_path.is_file():
                st.warning("Invalid file selected.")
            else:
                content = file_path.read_text()
                st.text_area("File Content", content, height=300)
        except Exception as e:
            st.error(f"Error: {e}")


# ==========================================
# UPDATE FILE
# ==========================================
elif menu == "Update File":
    st.header("✏️ Update File")

    files = list_files()
    selected_file = st.selectbox("Select file", files)

    option = st.radio(
        "Choose update type",
        ["Rename", "Overwrite", "Append"]
    )

    try:
        file_path = Path(selected_file)

        if option == "Rename":
            new_name = st.text_input("Enter new file name")
            if st.button("Rename"):
                file_path.rename(new_name)
                st.success("File renamed successfully!")

        elif option == "Overwrite":
            new_content = st.text_area("Enter new content")
            if st.button("Overwrite"):
                file_path.write_text(new_content)
                st.success("File overwritten successfully!")

        elif option == "Append":
            append_content = st.text_area("Enter content to append")
            if st.button("Append"):
                with file_path.open("a") as f:
                    f.write("\n" + append_content)
                st.success("Content appended successfully!")

    except Exception as e:
        st.error(f"Error: {e}")


# ==========================================
# DELETE FILE
# ==========================================
elif menu == "Delete File":
    st.header("🗑️ Delete File")

    files = list_files()
    selected_file = st.selectbox("Select file", files)

    confirm = st.checkbox("I confirm deletion")

    if st.button("Delete"):
        try:
            file_path = Path(selected_file)

            if not confirm:
                st.warning("Please confirm deletion.")
            elif not file_path.exists() or not file_path.is_file():
                st.warning("Invalid file selected.")
            else:
                file_path.unlink()
                st.success("File deleted successfully!")

        except Exception as e:
            st.error(f"Error: {e}")