from dotenv import load_dotenv
from google import genai

load_dotenv()
import json
import difflib


def analyze_chunk(client, chunk):

    prompt = f"""
You are ContractLens, an AI contract analysis assistant.

Analyze ONLY the contract text below.

Return ONLY valid JSON.
Do not use markdown.
Do not add explanations outside the JSON.

Use exactly this structure:

{{
    "contract_info": {{
        "parties": [],
        "contract_type": "",
        "effective_date": "",
        "expiration_date": "",
        "renewal_terms": "",
        "termination_conditions": ""
    }},
    "financial_terms": {{
        "payment_terms": "",
        "fees": "",
        "penalties": ""
    }},
    "obligations": [
        {{
            "party": "",
            "obligation": "",
            "deadline": ""
        }}
    ],
    "review_items": [
        {{
            "clause": "",
            "reason": ""
        }}
    ]
}}

Rules:
- Do not invent information.
- If something is not mentioned, write "Not specified".
- Extract important obligations for each party.
- Extract deadlines associated with obligations.
- Identify clauses that may require human legal review.

CONTRACT TEXT:
{chunk}
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return json.loads(response.text)

    except Exception as e:

        print(f"Gemini request failed: {e}")
        raise


def analyze_contract(text):

    client = genai.Client()

    chunk_size = 20000

    chunks = [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    results = []

    for i, chunk in enumerate(chunks):

        print(
            f"Analyzing contract section "
            f"{i + 1} of {len(chunks)}..."
        )

        result = analyze_chunk(client, chunk)

        results.append(result)

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

        contract_info = result.get(
            "contract_info",
            {}
        )

        financial_terms = result.get(
            "financial_terms",
            {}
        )

        for party in contract_info.get(
            "parties",
            []
        ):

            if party not in parties:
                parties.append(party)

        if contract_info.get(
            "contract_type",
            "Not specified"
        ) != "Not specified":

            contract_type = contract_info[
                "contract_type"
            ]

        if contract_info.get(
            "effective_date",
            "Not specified"
        ) != "Not specified":

            effective_date = contract_info[
                "effective_date"
            ]

        if contract_info.get(
            "expiration_date",
            "Not specified"
        ) != "Not specified":

            expiration_date = contract_info[
                "expiration_date"
            ]

        if contract_info.get(
            "renewal_terms",
            "Not specified"
        ) != "Not specified":

            renewal_terms = contract_info[
                "renewal_terms"
            ]

        if contract_info.get(
            "termination_conditions",
            "Not specified"
        ) != "Not specified":

            termination_conditions = contract_info[
                "termination_conditions"
            ]

        if financial_terms.get(
            "payment_terms",
            "Not specified"
        ) != "Not specified":

            payment_terms = financial_terms[
                "payment_terms"
            ]

        if financial_terms.get(
            "fees",
            "Not specified"
        ) != "Not specified":

            fees = financial_terms[
                "fees"
            ]

        if financial_terms.get(
            "penalties",
            "Not specified"
        ) != "Not specified":

            penalties = financial_terms[
                "penalties"
            ]

        obligations.extend(
            result.get(
                "obligations",
                []
            )
        )

        review_items.extend(
            result.get(
                "review_items",
                []
            )
        )

    final_result = {

        "contract_info": {

            "parties": parties,

            "contract_type": contract_type,

            "effective_date": effective_date,

            "expiration_date": expiration_date,

            "renewal_terms": renewal_terms,

            "termination_conditions":
                termination_conditions,
        },

        "financial_terms": {

            "payment_terms": payment_terms,

            "fees": fees,

            "penalties": penalties,
        },

        "obligations": obligations,

        "review_items": review_items,
    }

    return final_result


def create_obligation_timeline(obligations):

    timeline = []

    for obligation in obligations:

        timeline.append(
            {
                "party": obligation["party"],

                "obligation":
                    obligation["obligation"],

                "deadline":
                    obligation["deadline"],
            }
        )

    return timeline


def track_contractual_deadlines(analysis):

    deadlines = []

    for obligation in analysis.get(
        "obligations",
        []
    ):

        deadline = obligation.get(
            "deadline",
            "Not specified"
        )

        if deadline != "Not specified":

            deadlines.append(
                {
                    "party":
                        obligation["party"],

                    "obligation":
                        obligation["obligation"],

                    "deadline":
                        deadline,
                }
            )

    return deadlines


def create_deadline_alerts(deadlines):

    alerts = []

    for item in deadlines:

        deadline = item["deadline"]

        alerts.append(
            {
                "party":
                    item["party"],

                "obligation":
                    item["obligation"],

                "deadline":
                    deadline,

                "alert":
                    f"Upcoming deadline: {deadline}",
            }
        )

    return alerts


def compare_contract_versions(
    old_text,
    new_text
):

    old_lines = old_text.splitlines()

    new_lines = new_text.splitlines()

    difference = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile="Old Contract",
        tofile="New Contract",
        lineterm="",
    )

    return list(difference)