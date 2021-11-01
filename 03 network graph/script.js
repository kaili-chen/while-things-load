var searchListElem, chart;

var displayData = {
  nodes: nodes,
  edges: edges
}

document.addEventListener("DOMContentLoaded", function(event) {
    drawNetwork();

    searchListElem = document.getElementById('searchList');
    populateSearchList();    
});


function drawNetwork() {
    // clear out current network if any
    var div = document.getElementById('network');
    while(div.firstChild){
        div.removeChild(div.firstChild);
    }
    chart = anychart.graph(displayData);
    chart.container("network").draw();
    chart.layout().iterationCount(0);

}

function addItemToSearchList(node) {
  if (searchListElem) {
    var li, input;
    input = document.createElement('input');
    input.className = 'form-check-input me-1';
    input.type = 'checkbox';
    input.value = node.id;
    input.checked = true;
    input.setAttribute("onclick","clickCheck(this)");

    li = document.createElement('li');
    li.className = 'list-group-item';
    // li.dataset.nation = node.nation;

    // li.innerText = 'test'
    li.appendChild(input);
    li.appendChild(document.createTextNode(node.id));
    
    searchListElem.appendChild(li);
  }
}


function populateSearchList() {
  nodes.forEach(function(node){
    addItemToSearchList(node);
  });
}


function search(input) {
    var input, filter, li, item, i, txtValue;
    filter = input.value.toUpperCase();
    // ul = document.getElementById("searc");
    // li = ul.getElementsByTagName("li");
    li = searchListElem.getElementsByTagName('li');
    for (i = 0; i < li.length; i++) {
      item = li[i];
      txtValue = item.textContent || item.innerText;
      
      // ((item.dataset.nation).toUpperCase().indexOf(filter) > -1)
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        li[i].style.display = "";
      } else {
        li[i].style.display = "none";
      }
    }
}


function clickCheck(checkbox) {
  if (checkbox.checked) {
    console.log(checkbox.value + ' checked');
    addNode(checkbox.value);
  } else {
    console.log(checkbox.value + ' unchecked');
    removeNode(checkbox.value);
  }
  
}

function removeNode(name) {
  nodesToKeep = displayData.nodes.filter(function(node){
    return node.id !== name;
  });
  
  edgesToKeep = displayData.edges.filter(function(edge){
    return edge.from !== name && edge.to !== name;
  });

  // changes global displayData
  displayData = {
    nodes: nodesToKeep,
    edges: edgesToKeep
  }

  drawNetwork();
}

function addNode(name) {
  // console.log(chart.nodes())
  nodeToAdd = nodes.find(node => {
    return node.id === name;
  });
  
  edgesToAdd = edges.filter(node => {
    return (node.from === name) || (node.to === name);
  })

  displayData.nodes.push(nodeToAdd);
  displayData.edges.push(...edgesToAdd);
  drawNetwork();
}