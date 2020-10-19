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

// Working with the data
const url = "/data"
d3.json(url).then((data) =>{
    console.log(data)
    
    var rat =d3.select("text").text()
    console.log(rat)
    console.log(data[0][rat].side)
    // var trial_number = data[0][rat]['trial'];
    var correct_side = data[0][rat]['side'];
    var hits = data[0][rat]['hits'];
    var wrongs = data[0][rat]['wrongs'];
    

    var left = correct_side.filter(function(obj) {
        return obj === "left";
    });
    var right = correct_side.filter(function(obj) {
        return obj === "right";
    });

    var trace1 = {
          labels: ["left", "right"],
          values: [left.length, right.length],
          type: 'pie'
        };
        console.log(left.length)
        console.log(right.length)
        var d = [trace1];
        
        var layout = {
          title: "Pie Chart",
        };
        
        Plotly.newPlot("pie", d, layout);

  

  var x = ['le_lc_go', 'ri_lc_no', 'lo_pc_go', 'hi_pc_no', 'le_hi_lc', 'ri_hi_lc', 'le_lo_lc', 'ri_lo_lc', 'le_hi_pc', 'ri_hi_pc', 'le_lo_pc', 'ri_lo_pc'];
  var trace2 = {
    y: x,
    x: hits,
    name: 'Hits',
    type: 'bar',
    orientation: "h"
  };
  
  var trace3 = {
    y: x,
    x: wrongs,
    name: 'Misses',
    type: 'bar',
    orientation: "h"
  };
  
  var d2 = [trace2, trace3];
  
  var layout = {barmode: 'group'};
  
  Plotly.newPlot('bar', d2, layout);
    
        







  });