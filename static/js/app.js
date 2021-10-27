function init()
{  
  console.log(data)
    //Build the drop down
    var Ticker_Dropdown = d3.select("#selDataset")    
    var Ticker = data['names']
    for (var i in Ticker)
    {
    var sel_option = Ticker_Dropdown.append("option").text(Ticker[i])
    sel_option.attr("value", Ticker[i])
    }
    
}
 
init()