/*
A KBase module: keenholdhcContigFilter2_min_max
*/

module keenholdhcContigFilter2_min_max {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_keenholdhcContigFilter2_min_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
