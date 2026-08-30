#!/usr/bin/env python3
"""
Deterministic pre/post-checker for common Cisco lab configuration mistakes.
Input: cases.csv
Output: rule_check_results.csv
"""

import pandas as pd
import re
from ipaddress import ip_address, ip_network

def check_case(row):
    text = " ".join(str(row.get(c, "")) for c in ["symptom","topology_note","show_outputs","expected_fault"]).lower()
    checks = []

    patterns = {
        "duplicate_ip": r"duplicate|same ip|ip conflict",
        "wrong_mask": r"wrong subnet mask|incorrect mask|mask mismatch",
        "gateway_mismatch": r"wrong .*gateway|gateway.*wrong|incorrect pc default gateway",
        "interface_down": r"administratively down|err-disabled|interface.*down",
        "missing_vlan": r"vlan \d+ missing|missing vlan",
        "missing_route": r"missing route|no .*route|route.*not found",
        "trunk_problem": r"trunk|native vlan mismatch|allowed vlan",
        "dhcp_problem": r"dhcp|helper-address|pool exhausted",
        "dns_problem": r"dns",
        "acl_problem": r"acl|access-list|deny tcp",
        "nat_problem": r"nat|pat|translations",
        "wireless_problem": r"wireless|ssid|wifi|wi-fi|channel"
    }

    for name, pattern in patterns.items():
        if re.search(pattern, text):
            checks.append(name)

    expected = str(row.get("concept_tag","")).lower()
    result = "PASS" if expected in " ".join(checks) else "REVIEW"
    return {"case_id": row["case_id"], "expected_concept": row["concept_tag"],
            "detected_checks": ", ".join(checks) if checks else "none",
            "result": result}

df = pd.read_csv("cases.csv")
out = pd.DataFrame([check_case(r) for _, r in df.iterrows()])
out.to_csv("rule_check_results.csv", index=False)
print(out.to_string(index=False))
print("\nSaved: rule_check_results.csv")
