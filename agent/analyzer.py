from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List


class ContractInfo(BaseModel):
    parties: List[str]
    contract_type: str
    effective_date: str
    expiration_date: str
    renewal_terms: str


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


def analyze_contract(text):
    client = genai.Client()

    prompt = f"""
You are ContractLens, an AI contract analysis assistant.

Analyze the following contract carefully.

Extract:
1. Parties involved
2. Contract type
3. Effective date
4. Expiration date
5. Renewal terms
6. Payment terms
7. Fees
8. Penalties
9. Important obligations for each party
10. Deadlines associated with obligations
11. Clauses that may require human legal review

Do not invent information.
If something is not mentioned in the contract, say "Not specified".

This analysis is meant to assist human reviewers, not replace legal professionals.

CONTRACT TEXT:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ContractAnalysis,
        ),
    )

    return response.parsed.model_dump()
