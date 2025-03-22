import streamlit as st
from xml_parser import XMLParser
from groq_client import LLMClient

st.set_page_config(page_title="Tender Flow", page_icon="📄", layout="wide")

xml_file_path = "C:\\Users\\Ajay\\Desktop\\Freiheit\\Tendor\\app\\resources\\data.xml"
root = XMLParser.parse_xml(xml_file_path)
values = XMLParser.extract_values(root) if root else None
llm = LLMClient()

st.title("Tender Flow 📄")
if values:

    st.subheader("Ausschreibung Details")
    st.write(f"**Titel:** {values['name']}")
    st.write(f"**Vergabestelle:** N/A")
    st.write(f"**Veröffentlicht am:** {values['occurrence_date']}")
    st.write(f"**Angebotsfrist:** N/A")
    st.write(f"**CPV-Code:** {', '.join(values['item_classification_codes'])}")
    st.write(f"**Zussamenfassung:** N/A")
    with st.expander("📌 Ausschreibung öffnen"):
        st.write(f"**Ausschreibungstitel:** N/A")
        st.write(f"**Veröffentlichtungsdatum:** N/A")
        st.write(f"**Teilnahme-/Angebotsfrist:** N/A")
        st.write(f"**Lieferbeginn:** N/A")
        st.write(f"**Geschäftszeichen:** N/A")
        st.write(f"**Hauptklassifizierung:** N/A")
        st.write(f"**Erfüllungsort:** N/A")
        st.write(f"**Beschreibung:** {values['description']}")
        st.write(f"**Auftraggebe:** N/A")
        st.write(f"**Rolle:** N/A")
        st.write(f"**Name:** N/A")
        st.write(f"**Straße:** {values['street_name']}")
        st.write(f"**PLZ, Stadt:** {values['postal_zone']}, {values['city_name']}")
        st.write(f"**Land:** {values['country']}")

    with st.expander("📌 Fragen"):
        questions = {
            "Wann ist die Deadline?": values['tender_submission_deadline'],
            "Welche Projektreferenzen sind erforderlich?": values['note'],
            "Müssen bestimmte Standards eingehalten werden?": values['awarding_criterion'],
            "Liste der Anforderungen": values['description'],
            "Welche Zertifikate muss ich vorweisen können?": values['description'],
            "Gibt es bei dieser Ausschreibung Besonderheiten?": values['description']
        }
        
        for question, context in questions.items():
            with st.spinner(f"Analysiere: {question}..."):
                answer = llm.ask_llm(question, context)
            st.write(f"**{question}**: {answer}")
else:
    st.error("XML file not found or could not be parsed.")