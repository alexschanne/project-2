

const url = "/data"
d3.json(url).then((data) =>{
    console.log(data)
    var trial_number = data[0]['trial'];
    var correct_side = data[0]['side'];
    var hits = data[0]['hits'];
    var wrongs = data[0]['wrongs'];
    

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