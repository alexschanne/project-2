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