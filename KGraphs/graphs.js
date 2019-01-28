

var paragraphs = document.getElementsByTagName("p");

var chart = d3.select(".chart");
var bar = chart.selectAll("div");

var circle = d3.selectAll("circle");
circle.style("fill", "steelblue");
circle.attr("r", 30);

circle.attr("cx", function() {
  return Math.random() * 720; });
circle.attr("cy", function(){
  return Math.random() * 100
});

circle.data([32, 57, 112]);
circle.attr("r", function(d) { return Math.sqrt(d); });

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var myObj = JSON.parse(this.responseText);
    document.getElementById("JSON").innerHTML = myObj.name;
  }
};
xmlhttp.open("GET", "barData2.json", true);
xmlhttp.send();
