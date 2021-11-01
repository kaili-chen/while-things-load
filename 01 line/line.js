
var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  type: 'scatter',
  name: 'trace1'
};

var trace2 = {
  x: [1, 2, 3, 4],
  y: [16, 5, 11, 9],
  type: 'scatter',
  name: 'trace2'
};

mapping = {};
mapping[1] = trace1;
mapping[2] = trace2;

function addTrace(btn) {
  // console.log(btn.value);
  mappedValue= mapping[btn.value]
  // console.log(mappedValue)
  if (!isTraceInPlot(mappedValue.name)) {
    data = []
    data.push(mapping[btn.value])
   console.log(data)
    Plotly.addTraces('line-plot', data)
  } else {
    console.log("data already in plot, removing")
    removeTrace(mappedValue.name);
  }
}

function isTraceInPlot(traceName) {
  plotData = document.getElementById('line-plot').data;
  filtered = plotData.filter(d => d.name==traceName);
  console.log(filtered.length);
  return filtered.length > 0;
}

function removeTrace(traceName) {
  plotData = document.getElementById('line-plot').data;
  // console.log(plotData)
  dataIndex = plotData.findIndex(d => d.name === traceName)
  console.log(dataIndex);
  if (dataIndex > -1) {
    Plotly.deleteTraces('line-plot', dataIndex);
  }
  return filtered.length > 0;
}

// https://javascript.plainenglish.io/simple-async-search-bar-with-javascript-13652c90485e
function search(input) {
  var input, filter, ul, li, item, i, txtValue;
  filter = input.value.toUpperCase();
  ul = document.getElementById("tracesList");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
    item = li[i];
    txtValue = item.textContent || item.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}

document.addEventListener("DOMContentLoaded", function(event) {
  
  var data = [trace1];
  
  Plotly.newPlot('line-plot', data);

  plotData = document.getElementById('line-plot').data;
  // console.log(plotData);
  
})

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  // dark mode
  console.log('system dark');
}