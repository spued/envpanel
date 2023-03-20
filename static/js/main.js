

const ctx = document.getElementById('mainChart');

$( document ).ready(function() {

const graph_data = $('#graph_data').val().split('|');
//console.log(graph_data);
var time_labels = [];
var pm25_data = [];
var pm10_data = [];
var temp_data = [];
var humid_data = [];
var noise_data = [];
for(data of graph_data){
  let _data = data.split(',');
  //console.log(_data);
  time_labels.push(_data[0]);
  pm25_data.push(_data[1]);
  pm10_data.push(_data[2]);
  temp_data.push(_data[3]);
  humid_data.push(_data[4]);
  noise_data.push(_data[5]);
}

new Chart(ctx, {
        type: 'line',
        data: {
            labels: time_labels,
            datasets: [
            {
               label: 'PM2.5',
               data: pm25_data,
               borderWidth: 1
            },
            {
               label: 'PM10',
               data: pm10_data,
               borderWidth: 1
            },
            {
               label: 'Temperature',
               data: temp_data,
               borderWidth: 1
            },
            {
               label: 'Humidity',
               data: humid_data,
               borderWidth: 1
            },
            {
               label: 'Noise',
               data: noise_data,
               borderWidth: 1,
            }
            ]
         },
         options: {
             scales: {
                y: {
                    beginAtZero: true
                }
             }
         }
   });
});
