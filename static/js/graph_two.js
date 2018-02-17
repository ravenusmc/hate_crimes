//This file will contain the code that will change the historgram graphs. 

//This function will change the histogram graph
function changeHistogram(){ 

  //Getting the value based on what the user selected.
  let selected = document.getElementById('select_histogram').value;

  //Conditional statement to detemine which histogram will be shown. 
  if (selected == 'median') {
    document.getElementById('histogram_graph').src = "../static/graphs/median_income.png";
  }else if (selected == 'seasonal'){
    document.getElementById('histogram_graph').src = "../static/graphs/unemployed_season.png";
  }

}