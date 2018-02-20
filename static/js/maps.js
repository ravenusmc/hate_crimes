//The code in this file will be for the maps.html file and will mainly contain a lot 
//of the D3.JS for creating the maps. 

//This function will change the map based on what the user selects.
function selectMap() {

    let value = document.getElementById('select_map').value;

    d3.select("svg").remove();
    
    if (value == 'FBI'){
        let dataColumn = 'avg_hatecrimes_per_100k_fbi';
        createMap(dataColumn);
    }else if (value == 'hate_crimes_SPLC') {
        let dataColumn = 'hate_crimes_per_100k_splc';
        createMap(dataColumn);
    }else if (value == 'median_income'){
        let dataColumn = 'median_household_income';
        createMap(dataColumn);
    }else if (value == 'share_unemployed') {
        let dataColumn = 'share_unemployed_seasonal';
        createMap(dataColumn);
    }else if (value == 'metro_areas'){
        let dataColumn = 'share_population_in_metro_areas';
        createMap(dataColumn);
    }else if (value == 'hs_degree'){
        let dataColumn = 'share_population_with_high_school_degree';
        createMap(dataColumn);
    }
}


function createMap(dataColumn){


        d3.csv("/my/data/endpoint", function(data) {

        var width = 800;
        var height = 800;
        var svg = d3.select("#us-map")
                    .append("svg")
                    .attr("width",width)
                    .attr("height",height);

        var projection = d3.geo.albersUsa().translate([width/2,height/2]);
        projection = projection.scale(1000)
        var path = d3.geo.path().projection(projection);

        //Setting up basic look of the map
        d3.json("/json",function(data) {
          svg.append("path")
            .datum(data)
            .attr('d',path)
            .attr('fill',"rgb(237,248,233)")
            .attr('stroke','black');
        });

        //Setting up the color for the map as well as the range. 
        var color = d3.scale.quantize()
                .range(["rgb(237,248,233)","rgb(186,228,179)","rgb(116,196,118)","rgb(49,163,84)","rgb(0,109,44)"]);

        //Set input domain for color scale
        color.domain([
            d3.min(data, function(d) { return d[dataColumn]; }),
            d3.max(data, function(d) { return d[dataColumn]; })
        ]);

        //I have to use a geoJSON file to match up the state name with its geographical location
        d3.json("/json", function(json) {
            //Merge the data and GeoJSON
            //Loop through once for each data value
            for (var i = 0; i < data.length; i++) {
                //Grab state name
                var dataState = data[i].state;
                //Grab data value, and convert from string to float
                var dataValue = parseFloat(data[i][dataColumn]);
                //Find the corresponding state inside the GeoJSON
                for (var j = 0; j < json.features.length; j++) {
                    var jsonState = json.features[j].properties.name;
                    if (dataState == jsonState) {
                        //Copy the hate crime value into the JSON
                        json.features[j].properties.value = dataValue;
                        //Stop looking through the JSON
                        break;
                    }
                }
            }

            //Bind data and create one path per GeoJSON feature
            svg.selectAll("path")
               .data(json.features)
               .enter()
               .append("path")
               .attr("d", path)
               .style("fill", function(d) {
                    //Get data value
                    var value = d.properties.value;
                    if (value) {
                        //If value exists…
                        return color(value);
                    } else {
                        //If value is undefined…
                        return "#ccc";
                    }
               })
               .append("title")
               .text(function(d){
                    console.log(d);
                    return "State: " + d.properties.name + " Value: " + d.properties.value;
                });
        })
    });
}















//Setting up the variables for the map
// var width = 800;
// var height = 800;
// var svg = d3.select("#us-map").append("svg")
//             .attr("width",width)
//             .attr("height",height);

// var projection = d3.geo.albersUsa().translate([width/2,height/2]);
// projection = projection.scale(1000)
// var path = d3.geo.path().projection(projection);

// //Setting up basic look of the map
// d3.json("/json",function(data) {
//   svg.append("path")
//     .datum(data)
//     .attr('d',path)
//     .attr('fill',"rgb(237,248,233)")
//     .attr('stroke','black');
// });

// //Getting the data over to javascript
// d3.csv("/my/data/endpoint", function(data) {

//     //Setting up the color for the map as well as the range. 
//     var color = d3.scale.quantize()
//             .range(["rgb(237,248,233)","rgb(186,228,179)","rgb(116,196,118)","rgb(49,163,84)","rgb(0,109,44)"]);

//     //Set input domain for color scale
//     color.domain([
//         d3.min(data, function(d) { return d.avg_hatecrimes_per_100k_fbi; }),
//         d3.max(data, function(d) { return d.avg_hatecrimes_per_100k_fbi; })
//     ]);

//     //I have to use a geoJSON file to match up the state name with its geographical location
//     d3.json("/json", function(json) {
//         //Merge the data and GeoJSON
//         //Loop through once for each data value
//         for (var i = 0; i < data.length; i++) {
//             //Grab state name
//             var dataState = data[i].state;
//             //Grab data value, and convert from string to float
//             var dataValue = parseFloat(data[i].avg_hatecrimes_per_100k_fbi);
//             //Find the corresponding state inside the GeoJSON
//             for (var j = 0; j < json.features.length; j++) {
//                 var jsonState = json.features[j].properties.name;
//                 if (dataState == jsonState) {
//                     //Copy the hate crime value into the JSON
//                     json.features[j].properties.value = dataValue;
//                     //Stop looking through the JSON
//                     break;
//                 }
//             }
//         }

//         //Bind data and create one path per GeoJSON feature
//         svg.selectAll("path")
//            .data(json.features)
//            .enter()
//            .append("path")
//            .attr("d", path)
//            .style("fill", function(d) {
//                 //Get data value
//                 var value = d.properties.value;
//                 if (value) {
//                     //If value exists…
//                     return color(value);
//                 } else {
//                     //If value is undefined…
//                     return "#ccc";
//                 }
//            });
//     })
// });