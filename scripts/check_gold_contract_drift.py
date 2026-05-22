# -*- coding: utf-8 -*-
"""CI check: a gold table's live schema must not drift from its published ODCS contract.

Structural check only -- we diff column name/type sets, we do not attempt a
semantic diff of the contract prose.
"""
import sys


def extract_contract_columns(contract_doc):
    """Pure: pull {column_name: logicalType} out of a parsed ODCS contract dict."""
    columns = {}
    for table in contract_doc.get("schema", []):
        for prop in table.get("properties", []):
            columns[prop["name"]] = prop.get("logicalType")
    return columns


def diff_contract_against_live_schema(contract_columns, live_columns):
    """Pure: compare contract's declared columns against the live table schema.

    ``live_columns`` is {column_name: logicalType}. Returns a dict
    describing any drift; empty 'missing'/'type_mismatch' means no drift.
    """
    missing = sorted(set(contract_columns) - set(live_columns))
    type_mismatch = sorted(
        name
        for name in set(contract_columns) & set(live_columns)
        if contract_columns[name] != live_columns[name]
    )
    return {"missing": missing, "type_mismatch": type_mismatch}


def has_drift(diff_result):
    return bool(diff_result["missing"] or diff_result["type_mismatch"])


def main(argv=None):
    # In CI this loads the .odcs.yaml contract and the live Unity Catalog
    # schema; kept out of the pure functions above so they stay testable
    # with no Spark and no catalog access.
    import yaml
    from greenroute.common import spark_session

    argv = argv if argv is not None else sys.argv[1:]
    contract_path, table_name = argv[0], argv[1]
    with open(contract_path) as f:
        contract_doc = yaml.safe_load(f)
    spark = spark_session()
    live_columns = {f.name: f.dataType.simpleString() for f in spark.table(table_name).schema.fields}
    diff_result = diff_contract_against_live_schema(extract_contract_columns(contract_doc), live_columns)
    if has_drift(diff_result):
        print("METRIC contract_drift_detected=1 table=%s" % table_name)
        print(diff_result)
        return 1
    print("METRIC contract_drift_detected=0 table=%s" % table_name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
