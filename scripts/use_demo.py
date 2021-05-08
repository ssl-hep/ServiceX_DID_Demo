import argparse

def run_against_uproot(endpoint: str):
    'Run a simple query, print results'
    ds = ServiceXSourceUpROOT("data15_13TeV:data15_13TeV.00282784.physics_Main.deriv.DAOD_PHYSLITE.r9264_p3083_p4165_tid21568807_00", "CollectionTree")
data = ds.Select("lambda e: {'JetPT': e['AnalysisJetsAuxDyn.pt']}") \
    .AsParquetFiles('junk.parquet') \
    .value()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('servicex_endpoint', type=str, help='The endpoint url for ServiceX')
    args = parser.parse_args()

    run_against_uproot(args.servicex_endpoint)