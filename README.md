# 📄 TenderFlow - Government Tender Data Extraction & Analysis

TenderFlow is a powerful tool designed to extract, parse, and analyze government tender data obtained via the [Swagger UI Interface](https://oeffentlichevergabe.de/documentation/swagger-ui/opendata/index.html#/opendata/getExportAsEforms). The application processes XML data containing published tender notices and presents the extracted information in a clean and structured GUI built with Streamlit.

## ✨ Features

- **XML Parsing**: Extracts key details such as tender title, deadline, location, and classification codes.
- **LLM-Powered Q&A**: Provides answers to common tender-related queries using the Groq API.
- **Clean & Responsive UI**: Displays extracted tender information in a user-friendly layout.
- **Error Handling**: Ensures missing or insufficient data is properly indicated.

## 📌 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/tenderflow.git
cd tenderflow


### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt

3️⃣ Configure API Keys
Create a .env file in the project root and add:
```bash
GROQ_API_KEY=your_api_key_here

4️⃣ Run the Application
```bash 
streamlit run app.py

🛠️ Project Structure

├── app.py               # Main Streamlit application
├── xml_parser.py        # XML parsing and data extraction
├── groq_client.py       # LLM API interaction for question answering
├── resources/
│   ├── data.xml         # Sample XML data file
├── requirements.txt     # Required Python dependencies
├── .env.example         # Sample environment variable file
└── README.md            # Project documentation

🔍 Example Usage
Upon running the application, the parsed XML data will be displayed with details such as:

Tender Title

Publication Date

Submission Deadline

Location & Address

CPV Codes

Tender Description

Users can also interact with the LLM-powered Q&A feature to extract insights from the parsed data.

⚠️ Handling Missing Data
If the requested information is missing from the XML file, the system will return:

"N/A" or "Insufficient data available" instead of blank responses.

Ensures robustness and prevents errors during data retrieval.

🚀 Future Enhancements
Support for multiple XML file formats.

Improved filtering and search options.

Multi-language support for extracted data.

