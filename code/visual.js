function main() {
    var width = 1000;
    var height = 1000;
    // create svg object
    var svg = d3.select('body').append('svg')
                    .attr('width', width)
                    .attr('height', height);
    
    // download csv files
    csv_file_11 = "data_cleaned/11_cleaned_listings.csv";
    d3.csv(csv_file_11).then(function(data) {
        // Do something with the loaded data
        console.log(data);
    });
}

main();