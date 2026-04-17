import streamlit as st


def count_sequences(file):
    count = 0
    for line in file:
        if line.decode("utf-8").startswith(">"):
            count += 1
    return count


st.set_page_config(page_title="FASTA Sequence Counter")
st.image("Banner.png", use_container_width=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### FASTA Sequence Counter")
st.write("Upload a FASTA file to count the number of sequences.")

uploaded_file = st.file_uploader("Upload FASTA file", type=["fasta", "fa", "txt"])

if uploaded_file is not None:
    total = count_sequences(uploaded_file)
    st.success(f"Total FASTA sequences: {total}")

    if st.checkbox("Show file preview"):
        uploaded_file.seek(0)
        content = uploaded_file.read().decode("utf-8")
        st.text_area("FASTA Content", content, height=300)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "<b>The Biosphere Initiative</b> | Computational Biology Tools<br>"
    "Developed by Navadeeep Chandran"
    "</div>",
    unsafe_allow_html=True
)
