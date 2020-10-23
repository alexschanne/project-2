// dropdown menu and submit button
var select = d3.select("select")
var rats = ["","Ed","Madison","Lucy","Lauren","Josh","Marco"]
rats.forEach( d =>{
    var opt = select.append("option");
    opt.property("value",d.toLowerCase());
    opt.text(d);

});


var button = d3.select(".btn")

button.on("click",runEnter)

function runEnter(){
    var dropdownMenu = d3.select("select");
        // Assign the value of the dropdown menu option to a variable
    var option = dropdownMenu.property("value");

    var url = `http://127.0.0.1:5000/rat/${option}`

    button.attr('href', url);
    window.location = url;

};

var heading = d3.select('#rat').text()
var new_header = heading.toString()
d3.select('#rat').text(`${new_header.toUpperCase()}`);

var rat =d3.select("text").text();

// Working with the data
const url = "/data"
d3.json(url).then((data) =>{
  
    
  
  
  var hits = data[0][rat]['hits'];
  var wrongs = data[0][rat]['wrong'];
  var errors = data[0][rat]['errors']
  var stim_count = data[0][rat]['stim_count'];
  var go_nogo = data[0][rat]['go_nogo'];
    
  var x = ['Left Side Localization Go Trial', 'Right Side Localization No Go Trial', 'Low Pitch Pitch Go Trial', 'High Pitch Pitch No Go Trial', 'Left Side/High Pitch Localization Normal Trial', 'Right Side/High Pitch Localization Normal Trial', 'Left Side/Low Pitch Localization Normal Trial', 'Right Side/Low Pitch Localization Normal Trial', 'Left Side/High Pitch Pitch Normal Trial', 'Right Side/High Pitch Pitch Normal Trial', 'Left Side/Low Pitch Pitch Normal Trial', 'Left Side/Low Pitch Pitch Normal Trial'];
  var trace1 = {
    labels: x,
    values: stim_count,
    type: 'pie'
  };
  
  var d = [trace1];
  
  var layout = {
    title: "Stimuli Tested",
    x: 0,
        height: 700,
        showlegend: true,
        margin: {
            l: 100,
            r: 100,
            t: 100,
            b: 100
        },
        legend: { x: 1, y: 0, xanchor: 'right', yanchor: 'top' }
  };
  
  Plotly.newPlot("pie", d, layout);

  

  var x =x;
  var trace2 = {
    x: x,
    y: hits,
    name: 'Hits',
    type: 'bar',
    marker: {
              color:'green'
          }
  };
  
  var trace3 = {
    x: x,
    y: wrongs,
    name: 'Misses',
    type: 'bar',
    marker: {
              color:'red'
          }
  };
  
  var trace4 = {
    x: x,
    y: errors,
    name: 'Errors',
    type: 'bar',
    marker: {
              color:'yellow'
          }
  };
  
  var d2 = [trace2, trace3, trace4];
  
  var layout = {
    barmode: 'grouped',
    title: "Rat Experiment",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 200
    },
    xaxis: {
      title: {
        text: 'Stimuli'
      }
    }
  };
  
  Plotly.newPlot('bar', d2, layout);
  
  var trace5 = {
    y: ["go_hit","go_miss","go_error","no_go_hit","no_go_miss","no_go_error"] ,
    x: go_nogo,
    type: 'bar',
    orientation: "h"
  };
  
  var d3 = [trace5];
  
  var layout = {
    title: "Go vs. No Go",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };
  
  Plotly.newPlot('go_nogo', d3, layout);
        







});