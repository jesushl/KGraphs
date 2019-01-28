google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawVisualization);
function drawVisualization() {
        // Some raw data (not necessarily accurate)
        var data = google.visualization.arrayToDataTable([['Pretunta', 'Resultado', 'Mercado', 'Esperado'], ['¿Cómo calificas la atención recibida?', 100.0, 29, 90], ['¿Qué tanto ha profundizado en tus necesidades?', 100.0, 41, 98], ['¿Hasta el momento ¿Qué tanto hemos cumplido con la promesa de venta?', 100.0, 34, 87], ['¿Siempre haz encontrado a personas que te atiendan y se ocupen de ti cuando tú lo necesitas?', 85.71428571428571, 47, 82], ['¿Cómo calificas nuestra oferta de valor?', 100.0, 42, 76]]);//

        var options = {
          title : 'NPS',
          vAxis: {title: 'Calificacion'},
          hAxis: {title: 'Pregunta'},
          seriesType: 'bars',
          series  :{  1 : { type : 'line'}, 2 : { type : 'line'}},//
          orientation : 'horizontal',
          textStyle: {
            fontName: 'Times-Roman',
            fontSize: 18,
            bold: true,
            italic: false,
            // The color of the text.
            color: '#871b47',
            // The color of the text outline.
            auraColor: '#d799ae',
            // The transparency of the text.
            opacity: 0.8
            },

          };
        var chart = new google.visualization.ComboChart(document.getElementById('multiGraph'));//
        chart.draw(data, options);
      }
