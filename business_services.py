
import os
import json
import requests
from datetime import datetime as pydatetime, timedelta, timezone
from typing import Optional, Callable, Any, Set
from dotenv import load_dotenv

load_dotenv()
def fetch_flight_status(
    airline_code: str,
    flight_number: str
) -> str:
    """
    Returns the status of a specified flight for a particular airline. airline_code and flight_number parameters are mandatory. If you find any required information missing, please ask clarifying questions.

    :param airline_code: The airline code, e.g. Qatar is "QR", Emirates is "EK", Lufthansa is "LH". (mandatory)
    :param flight_number: The flight number, e.g. "123". (mandatory)
    :return: A JSON string containing the "status" or an "error" key/value.
    """
    try:
        # actual API call to fetch flight status
        if airline_code == "QR" and flight_number == "123":
            return json.dumps({"status": "Delayed", "reason": "Weather"})  # Dummy response
        elif airline_code == "QR" and flight_number == "456":
            return json.dumps({"status": "On time"})  # Dummy response
        elif airline_code == "EK" and flight_number == "789":
            return json.dumps({"status": "Delayed", "reason": "Mechanical problem"})  # Dummy response
        else:
            return json.dumps({"status": "Unknown airline code or unknown combination"})  # Dummy response
    except Exception as e:
        return json.dumps({"error": f"Unexpected issue - {type(e).__name__}: {e}"})

def fetch_baggage_allowance(
        airline_code: str,
        class_of_travel: str
) -> str:
    """
    Returns the baggage allowance of a specified airlines for a particular class. airline_code and flight_number parameters are mandatory. If you find any required information missing, please ask clarifying questions.

    :param airline_code: The IATA airline code, e.g. "QR", "LH", "UA". (mandatory)
    :param class_of_travel: The airline class, e.g. "economy", "business", "first", "premium_economy". (mandatory)
    :return: A JSON string containing the "baggage allowance" or an "error" key/value.
    """
    try:
        # actual API call to fetch baggage allowance
        if airline_code in ["QR", "EK", "LH", "UA"]:
            if class_of_travel.lower() == "economy":
                return json.dumps({"allowance": "1 piece, 23kg"})  # Dummy response
            elif class_of_travel.lower() == "premium economy":
                return json.dumps({"allowance": "2 pieces, 23kg each"})  # Dummy response
            elif class_of_travel.lower() == "business":
                return json.dumps({"allowance": "2 pieces, 23kg each"})  # Dummy response
            elif class_of_travel.lower() == "first":
                return json.dumps({"allowance": "3 pieces, 32kg each"})  # Dummy response
        else:
            return json.dumps({"status": "Unknown airline code or class of travel"})  # Dummy response
    except Exception as e:
        return json.dumps({"error": f"Unexpected issue - {type(e).__name__}: {e}"})

def fetch_gate_information(
        airline_code: str,
        flight_number: str
) -> str:
    """
    Provides the gate details for a specific flight from a designated airline. airline_code and flight_number parameters are mandatory. If you find any required information missing, please ask clarifying questions.

    :param airline_code: The airline code, e.g. "QR". (mandatory)
    :param flight_number: The flight number, e.g. "123". (mandatory)
    :return: A JSON string containing the "gate information" or an "error" key/value.
    """
    try:
        # actual API call to fetch gate information
        if airline_code == "QR" and flight_number == "123":
            return json.dumps({"gate": "A1", "terminal": "1"})  # Dummy response
        elif airline_code == "QR" and flight_number == "456":
            return json.dumps({"gate": "B2", "terminal": "2"}) # Dummy response
        elif airline_code == "EK" and flight_number == "789":
            return json.dumps({"gate": "C3", "terminal": "3"})  # Dummy response
        else:
            return json.dumps({"status": "Unknown airline code or flight number"})  # Dummy response
    except Exception as e:
        return json.dumps({"error": f"Unexpected issue - {type(e).__name__}: {e}"})
    
# make functions callable a callable set from enterprise-streaming-agent.ipynb
business_fns: Set[Callable[..., Any]] = {
    fetch_flight_status,
    fetch_baggage_allowance,
    fetch_gate_information,
}