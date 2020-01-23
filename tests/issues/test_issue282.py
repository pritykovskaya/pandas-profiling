"""
Test for issue 282:
https://github.com/pandas-profiling/pandas-profiling/issues/282
"""
import pandas as pd
from pandas_profiling import ProfileReport


def test_issue282():
    index = [
        "BJ110",
        "BJ126",
        "BJ163",
        "BJ054",
        "BJ017",
        "LP045",
        "BJ153",
        "AD013",
        "NL047",
        "BJ036",
        "AD026",
        "BJ018",
        "LP044",
        "LP006",
        "BO014",
        "BJ035",
        "BJ155",
        "TLL003",
        "BJ073",
        "BJ068",
        "BJ049",
        "TLL061",
        "NL010",
        "AD019",
        "LP003",
        "BJ107",
        "BJ023",
        "BJ012",
        "TLL067",
        "LP020",
        "AD031",
        "BJ172",
        "NL031",
        "LP032",
        "AD016",
        "BJ077",
        "BJ047",
        "BJ001",
        "BJ105",
        "BJ062",
        "AD022",
        "BJ106",
        "BJ102",
        "BJ022",
        "BJ010",
        "TLL007",
        "AD011",
        "LP018",
        "TLL004",
        "TLL030",
        "BJ005",
        "AD003",
        "BJ025",
        "LP005",
        "BJ144",
        "BJ080",
        "TLL062",
        "BJ166",
        "LP014",
        "NL005",
        "TLL038",
        "BJ072",
        "AD032",
        "BO001",
        "BO024",
        "BO005",
        "AD004",
        "TLL006",
        "BJ063",
        "BJ007",
        "LP007",
        "BJ159",
        "NL056",
        "NL059",
        "BJ115",
        "NL037",
        "BJ003",
        "BJ117",
        "AD025",
        "BJ050",
        "LP029",
        "BJ149",
        "AD002",
        "AD010",
        "BJ160",
        "BJ147",
        "BO023",
        "NL055",
        "NL038",
        "BO004",
        "BJ123",
        "NL051",
        "NL011",
    ]

    df = pd.DataFrame(
        index=index,
        data={"column_1": ["value"] * len(index), "column_2": [1.0] * len(index)},
    )
    report = ProfileReport(df)
    description = report.get_description()
    assert type(description) == dict
