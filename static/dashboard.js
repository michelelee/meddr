



// area chart
// donations over time

$.get("/donations_over_time",
    donationsOverTime)

function donationsOverTime (result) {
    console.log(result)
    var donate_times = []
    var total_progress = 0
    _.each(result.donations, function(donation) {
        total_progress = total_progress + donation.donation_amt
        var donated_at = donation.donated_at
        donated_at = new Date(donated_at)
        console.log(donated_at)
        time = Date.UTC(donated_at.getFullYear(), 
                        donated_at.getMonth(), 
                        donated_at.getDate())
        coordinates.push([time, total_progress])
    })

    donationsOverTimeChart
}

// $(function donationsOverTimeChart() {
//     $('#container').highcharts({
//         chart: {
//             type: 'area'
//         },
//         title: {
//             text: 'Donations Over Time'
//         },
//         xAxis: {
//             allowDecimals: false,
//             labels: {
//                 formatter: function () {
//                     return this.value; // clean, unformatted number for year
//                 }
//             }
//         },
//         yAxis: {
//             title: {
//                 text: 'Donations towards the ' + campaign + "campaign"
//             },
//             labels: {
//                 formatter: function () {
//                     return this.value;
//                 }
//             }
//         },
//         tooltip: {
//             pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
//         },
//         plotOptions: {
//             area: {
//                 pointStart: 1940,
//                 marker: {
//                     enabled: false,
//                     symbol: 'circle',
//                     radius: 2,
//                     states: {
//                         hover: {
//                             enabled: true
//                         }
//                     }
//                 }
//             }
//         },
//         series: [{
//             name: 'USA',
//             data: [null, null, null, null, null, 6, 11, 32, 110, 235, 369, 640,
//                 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126,
//                 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662,
//                 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
//                 24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586,
//                 22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950,
//                 10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104]
//         }, {
//             name: 'USSR/Russia',
//             data: [null, null, null, null, null, null, null, null, null, null,
//                 5, 25, 50, 120, 150, 200, 426, 660, 869, 1060, 1605, 2471, 3322,
//                 4238, 5221, 6129, 7089, 8339, 9399, 10538, 11643, 13092, 14478,
//                 15915, 17385, 19055, 21205, 23044, 25393, 27935, 30062, 32049,
//                 33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000, 37000,
//                 35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
//                 21000, 20000, 19000, 18000, 18000, 17000, 16000]
//         }]
//     });
// });


// // column chart
// // donors by demographics
// // donations by campaign/issue area
// // donors other interests - other issue areas they've donated to

// $(function () {
//     $('#container').highcharts({
//         chart: {
//             type: 'column'
//         },
//         title: {
//             text: 'Monthly Average Rainfall'
//         },
//         subtitle: {
//             text: 'Source: WorldClimate.com'
//         },
//         xAxis: {
//             categories: [
//                 'Jan',
//                 'Feb',
//                 'Mar',
//                 'Apr',
//                 'May',
//                 'Jun',
//                 'Jul',
//                 'Aug',
//                 'Sep',
//                 'Oct',
//                 'Nov',
//                 'Dec'
//             ],
//             crosshair: true
//         },
//         yAxis: {
//             min: 0,
//             title: {
//                 text: 'Rainfall (mm)'
//             }
//         },
//         tooltip: {
//             headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
//             pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
//                 '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
//             footerFormat: '</table>',
//             shared: true,
//             useHTML: true
//         },
//         plotOptions: {
//             column: {
//                 pointPadding: 0.2,
//                 borderWidth: 0
//             }
//         },
//         series: [{
//             name: 'Tokyo',
//             data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

//         }, {
//             name: 'New York',
//             data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

//         }, {
//             name: 'London',
//             data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

//         }, {
//             name: 'Berlin',
//             data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]

//         }]
//     });
// });


// // stacked column
// // donations to campaigns you support (by 501(c))

// $(function () {
//     $('#container').highcharts({
//         chart: {
//             type: 'column'
//         },
//         title: {
//             text: 'Stacked column chart'
//         },
//         xAxis: {
//             categories: ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
//         },
//         yAxis: {
//             min: 0,
//             title: {
//                 text: 'Total fruit consumption'
//             },
//             stackLabels: {
//                 enabled: true,
//                 style: {
//                     fontWeight: 'bold',
//                     color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
//                 }
//             }
//         },
//         legend: {
//             align: 'right',
//             x: -30,
//             verticalAlign: 'top',
//             y: 25,
//             floating: true,
//             backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
//             borderColor: '#CCC',
//             borderWidth: 1,
//             shadow: false
//         },
//         tooltip: {
//             formatter: function () {
//                 return '<b>' + this.x + '</b><br/>' +
//                     this.series.name + ': ' + this.y + '<br/>' +
//                     'Total: ' + this.point.stackTotal;
//             }
//         },
//         plotOptions: {
//             column: {
//                 stacking: 'normal',
//                 dataLabels: {
//                     enabled: true,
//                     color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
//                     style: {
//                         textShadow: '0 0 3px black'
//                     }
//                 }
//             }
//         },
//         series: [{
//             name: 'John',
//             data: [5, 3, 4, 7, 2]
//         }, {
//             name: 'Jane',
//             data: [2, 2, 3, 2, 1]
//         }, {
//             name: 'Joe',
//             data: [3, 4, 4, 2, 5]
//         }]
//     });
// });



// // add map of zipcodes if possible