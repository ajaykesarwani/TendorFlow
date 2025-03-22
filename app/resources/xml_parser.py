import xml.etree.ElementTree as ET

class XMLParser:
    NS = {
        'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
        'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'
    }

    @staticmethod
    def parse_xml(xml_file_path):
        try:
            tree = ET.parse(xml_file_path)
            return tree.getroot()
        except (FileNotFoundError, ET.ParseError):
            return None

    @staticmethod
    def extract_values(root):
        if root is None:
            return None

        def get_text(path):
            element = root.find(path, XMLParser.NS)
            return element.text if element is not None else "N/A"

        return {
            'street_name': get_text(".//cac:RealizedLocation/cac:Address/cbc:StreetName"),
            'city_name': get_text(".//cac:RealizedLocation/cac:Address/cbc:CityName"),
            'postal_zone': get_text(".//cac:RealizedLocation/cac:Address/cbc:PostalZone"),
            'country': get_text(".//cac:RealizedLocation/cac:Address/cac:Country/cbc:IdentificationCode"),
            'item_classification_codes': [elem.text for elem in root.findall(".//cac:MainCommodityClassification/cbc:ItemClassificationCode", XMLParser.NS)] or ["N/A"],
            'name': get_text(".//cac:ProcurementProject/cbc:Name"),
            'description': get_text(".//cac:ProcurementProject/cbc:Description"),
            'occurrence_date': get_text(".//cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate"),
            'occurrence_time': get_text(".//cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceTime"),
            'tender_submission_deadline': get_text(".//cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate"),
            'awarding_criterion': get_text(".//cac:AwardingCriterion/cac:SubordinateAwardingCriterion/cbc:AwardingCriterionTypeCode"),
            'note': get_text(".//cac:ProcurementProject/cbc:Note")
        }
