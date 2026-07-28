/*
A KBase module: keenholdhcContigFilter2
This sample module contains one small method that filters contigs.
*/

module keenholdhcContigFilter2 {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_keenholdhcContigFilter2(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
