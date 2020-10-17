function buildMetadata(sample) {
    // Use `d3.json` to fetch the metadata for a sample
    // @TODO: ADD DATA ource
    d3.json(url).then(function(sample){
  
      // Use d3 to select the panel with id of `#sample-metadata`
      var sample_metadata = d3.select("#sample-metadata");
  
      // Use `.html("") to clear any existing metadata
      sample_metadata.html("");
  
      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new tags for each key-value in the metadata.
      Object.entries(sample).forEach(function ([key, value]) {
        var row = sample_metadata.append("panel-body");
        row.text(`${key}: ${value} \n`);
      });
    });
  }
  
  function buildCharts(sample) {
  
    // @TODO: Use `d3.json` to fetch the sample data for the plots
    var url = `/samples/${sample}`;
    d3.json(url).then(function(data) {
  
      // @TODO: Build a Bubble Chart using the sample data
      var x_values = data.otu_ids;
      var y_values = data.sample_values;
      var m_size = data.sample_values;
      var m_colors = data.otu_ids; 
      var t_values = data.otu_labels;
  
      var trace1 = {
        x: x_values,
        y: y_values,
        text: t_values,
        mode: 'markers',
        marker: {
          color: m_colors,
          size: m_size
        } 
      };
    
      var data = [trace1];
  
      var layout = {
        xaxis: { title: "OTU ID"},
      };
  
      Plotly.newPlot('bubble', data, layout);
     
      // @TODO: Build a Bar Chart
      var barSpacing = 10; // desired space between each bar
      var scaleY = 10; // 10x scale on rect height
       // @TODO
        // Create code to build the bar chart using the tvData.
        chartGroup.selectAll(".bar")
        .data(tvData)
        .enter()
        .append("rect")
        .classed("bar", true)
        .attr("width", d => barWidth)
        .attr("height", d => d.hours * scaleY)
        .attr("x", (d, i) => i * (barWidth + barSpacing))
        .attr("y", d => chartHeight - d.hours * scaleY);
      }).catch(function(error) {
      console.log(error);
        
    });   
  }
  
  function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("/names").then((sampleNames) => {
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      const firstSample = sampleNames[0];
      buildCharts(firstSample);
      buildMetadata(firstSample);
    });
  }
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildCharts(newSample);
    buildMetadata(newSample);
  }
  
  // Initialize the dashboard
  init();
  
  