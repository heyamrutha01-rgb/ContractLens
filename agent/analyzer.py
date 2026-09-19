from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List
import time


class ContractInfo(BaseModel):
    parties: List[str]
    contract_type: str
    effective_date: str
    expiration_date: str
    renewal_terms: str
    termination_conditions: str


class FinancialTerms(BaseModel):
    payment_terms: str
    fees: str
    penalties: str


class Obligation(BaseModel):
    party: str
    obligation: str
    deadline: str


class ReviewItem(BaseModel):
    clause: str
    reason: str


class ContractAnalysis(BaseModel):
    contract_info: ContractInfo
    financial_terms: FinancialTerms
    obligations: List[Obligation]
    review_items: List[ReviewItem]


def analyze_chunk(client, chunk):
    prompt = f"""
You are ContractLens, an AI contract analysis assistant.

Analyze ONLY the contract section below.

Extract:
1. Parties involved
2. Contract type
3. Effective date
4. Expiration date
5. Renewal terms
6. Termination conditions
7. Payment terms
8. Fees
9. Penalties
10. Important obligations for each party
11. Deadlines associated with obligations
12. Clauses that may require human legal review

Do not invent information.

If something is not mentioned in this section, say "Not specified".

CONTRACT SECTION:
{chunk}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ContractAnalysis,
                ),
            )

            return response.parsed

        except Exception:
            if attempt == 2:
                raise

            print(
                f"Gemini request failed. Retrying... ({attempt + 1}/3)"
            )
            time.sleep(5)


def analyze_contract(text):
    client = genai.Client()

    chunk_size = 20000

    chunks = [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    results = []

    for i, chunk in enumerate(chunks):
        try:
            print(
                f"Analyzing contract section "
                f"{i + 1} of {len(chunks)}..."
            )

            result = analyze_chunk(client, chunk)
            results.append(result)

        except Exception as e:
            print(
                f"Section {i + 1} could not be analyzed. "
                f"Skipping this section."
            )
            print(f"Reason: {e}")

    if not results:
        raise RuntimeError(
            "No contract sections could be analyzed."
        )

    parties = []
    obligations = []
    review_items = []

    contract_type = "Not specified"
    effective_date = "Not specified"
    expiration_date = "Not specified"
    renewal_terms = "Not specified"
    termination_conditions = "Not specified"

    payment_terms = "Not specified"
    fees = "Not specified"
    penalties = "Not specified"

    for result in results:

        for party in result.contract_info.parties:
            if party not in parties:
                parties.append(party)

        if result.contract_info.contract_type != "Not specified":
            contract_type = result.contract_info.contract_type

        if result.contract_info.effective_date != "Not specified":
            effective_date = result.contract_info.effective_date

        if result.contract_info.expiration_date != "Not specified":
            expiration_date = result.contract_info.expiration_date

        if result.contract_info.renewal_terms != "Not specified":
            renewal_terms = result.contract_info.renewal_terms

        if (
            result.contract_info.termination_conditions
            != "Not specified"
        ):
            termination_conditions = (
                result.contract_info.termination_conditions
            )

        if result.financial_terms.payment_terms != "Not specified":
            payment_terms = result.financial_terms.payment_terms

        if result.financial_terms.fees != "Not specified":
            fees = result.financial_terms.fees

        if result.financial_terms.penalties != "Not specified":
            penalties = result.financial_terms.penalties

        obligations.extend(
            [
                obligation.model_dump()
                for obligation in result.obligations
            ]
        )

        review_items.extend(
            [
                item.model_dump()
                for item in result.review_items
            ]
        )

    final_result = {
        "contract_info": {
            "parties": parties,
            "contract_type": contract_type,
            "effective_date": effective_date,
            "expiration_date": expiration_date,
            "renewal_terms": renewal_terms,
            "termination_conditions": termination_conditions,
        },
        "financial_terms": {
            "payment_terms": payment_terms,
            "fees": fees,
            "penalties": penalties,
        },
        "obligations": obligations,
        "obligation_timeline": create_obligation_timeline(obligations), 
        "review_items": review_items,
    }

    return final_result


def create_obligation_timeline(obligations):
    timeline = []

    for obligation in obligations:
        timeline.append(
            {
                "party": obligation["party"],
                "obligation": obligation["obligation"],
                "deadline": obligation["deadline"],
            }
        )

    return timeline

def create_contract_summary(analysis):
    contract_info = analysis["contract_info"]
    financial_terms = analysis["financial_terms"]

    summary = {
        "parties": contract_info["parties"],
        "contract_type": contract_info["contract_type"],
        "effective_date": contract_info["effective_date"],
        "expiration_date": contract_info["expiration_date"],
        "renewal_terms": contract_info["renewal_terms"],
        "termination_conditions": contract_info["termination_conditions"],
        "payment_terms": financial_terms["payment_terms"],
        "fees": financial_terms["fees"],
        "penalties": financial_terms["penalties"],
    }

    return summary

def track_upcoming_renewal(analysis):
    renewal_terms = analysis["contract_info"]["renewal_terms"]
    expiration_date = analysis["contract_info"]["expiration_date"]

    return {
        "expiration_date": expiration_date,
        "renewal_terms": renewal_terms,
        "renewal_status": (
            "Renewal information available"
            if renewal_terms != "Not specified"
            else "Renewal information not specified"
        ),
    }
    
def track_contractual_deadlines(analysis):
    deadlines = []

    for obligation in analysis["obligations"]:
        deadline = obligation["deadline"]

        if deadline != "Not specified":
            deadlines.append(
                {
                    "party": obligation["party"],
                    "obligation": obligation["obligation"],
                    "deadline": deadline,
                }
            )

    return deadlines 

def create_deadline_alerts(deadlines):
    alerts = []

    for item in deadlines:
        deadline = item["deadline"]

        alerts.append(
            {
                "party": item["party"],
                "obligation": item["obligation"],
                "deadline": deadline,
                "alert": f"Upcoming deadline: {deadline}",
            }
        )

    return alerts

import difflib


def compare_contract_versions(old_text, new_text):
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()

    differences = list(
        difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile="Old Contract",
            tofile="New Contract",
            lineterm="",
        )
    )

    return differences
