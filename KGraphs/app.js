var express = require('express');
var app = express();
app.use(express.static('.'));

app.get('/',  function (req, res) {
  res.send('Hello World!');
});

app.get('/indexado', function(req, res){
  res.sendFile('/home/jesus/Documentos/Proyects/KGraphs/index.html');
});

app.get('/barData', funtion(req, res){
  res.sendFile('/home/jesus/Documentos/Proyects/KGraphs/barData2.json')
});
app.get('/user', function(req, res){
    res.send("Got a PUT request at /user");
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
